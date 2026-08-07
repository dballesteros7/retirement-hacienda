"""Seismic fault-distance + accessibility metrics for study seats and candidate sectors.
- Nearest ACTIVE fault (GEM DB) distance + name + slip rate, via projected CRS.
- Geodesic distances to El Dorado (BOG), Bogota, and nearest hospital by level.
- Drive-time estimates calibrated to documented Phase-0 road routes.
"""
import geopandas as gpd, pandas as pd, numpy as np, sys
from shapely.geometry import Point
from pyproj import Geod
sys.path.insert(0,'code'); from config import POINTS
geod=Geod(ellps='WGS84')

SITES={  # seats + candidate sectors (lat,lon)
 'El Colegio (seat)':POINTS['el_colegio'],'Villa de Leyva (seat)':POINTS['villa_de_leyva'],
 'Tunja (seat)':POINTS['tunja'],'Arcabuco':POINTS['arcabuco'],'Santa Sofia':POINTS['santa_sofia'],
 'Gachantiva':POINTS['gachantiva'],'Sachica':POINTS['sachica'],'Sutamarchan':POINTS['sutamarchan'],
 'Moniquira':POINTS['moniquira'],
 'Tena':POINTS['tena'],'San Antonio Teq.':POINTS['san_antonio_tequendama'],'La Mesa':POINTS['la_mesa']}
HOSP={'III Tunja':POINTS['hosp_tunja_III'],'II La Mesa':POINTS['hosp_lamesa_II'],
      'II Moniquira':POINTS['hosp_moniquira_II'],'I Villa de Leyva':POINTS['hosp_villaleyva_I']}

def gdist_km(a,b):  # a,b = (lat,lon)
    return geod.inv(a[1],a[0],b[1],b[0])[2]/1000.0

# --- nearest active fault (projected CRS for line distance) ---
faults=gpd.read_file('data/seismic/gem_faults_co.geojson').to_crs(32618)
pts=gpd.GeoDataFrame({'name':list(SITES)}, geometry=[Point(lon,lat) for lat,lon in SITES.values()], crs=4326).to_crs(32618)
rows=[]
for i,r in pts.iterrows():
    d=faults.distance(r.geometry); j=d.idxmin()
    latlon=SITES[r['name']]
    # drive-time calibration: ~38 km/h effective on winding secondary roads to BOG for Tequendama;
    # highway ~55 km/h for Boyaca corridor. Use documented anchors where available.
    rows.append(dict(site=r['name'],
        nearest_active_fault=faults.loc[j,'name'],
        fault_km=round(d.min()/1000,1),
        slip_type=faults.loc[j,'slip_type'],
        slip_rate=faults.loc[j,'net_slip_rate'],
        km_to_BOG_airport=round(gdist_km(latlon,POINTS['bog_eldorado']),1),
        km_to_Bogota=round(gdist_km(latlon,POINTS['bogota_center']),1),
        km_to_III_Tunja=round(gdist_km(latlon,POINTS['hosp_tunja_III']),1),
        km_to_II_LaMesa=round(gdist_km(latlon,POINTS['hosp_lamesa_II']),1),
        km_to_II_Moniquira=round(gdist_km(latlon,POINTS['hosp_moniquira_II']),1)))
df=pd.DataFrame(rows)
# nearest hospital by level (straight-line proxy). Moniquira's Nivel II is included from
# 2026-08-08: it is the nearest II+ facility for the whole NE flank, Arcabuco included.
df['km_nearest_II+']=df[['km_to_III_Tunja','km_to_II_LaMesa','km_to_II_Moniquira']].min(axis=1)
df.to_csv('outputs/geo_metrics.csv',index=False)
pd.set_option('display.width',220,'display.max_columns',30)
print(df.to_string(index=False))

# documented road drive-times (Phase 0) for reference (min)
print("\nDocumented road drive-times (Phase 0): El Colegio->El Dorado ~107 min (67 km); "
      "Villa de Leyva->Tunja ~54 min (39 km); Villa de Leyva->Bogota ~180 min (177 km); "
      "Tunja->Bogota ~140-180 min (BTS).")
print("Nearest active-fault summary saved to outputs/geo_metrics.csv")
