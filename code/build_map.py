"""Interactive Leaflet (folium) map: boundaries, active faults, candidate sectors, shortlisted
parcels, reference points. Tiles + Leaflet load client-side in the user's browser."""
import folium, geopandas as gpd, json
from folium import FeatureGroup, LayerControl, Marker, PolyLine, CircleMarker
from folium.features import DivIcon

# --- candidate sectors: (lat,lon, dict of popup metrics) ---
SEC = {
 "Arcabuco":        (5.7597,-73.4372, dict(g="flank",elev=2600,ai="1.48 (humid)",fault=64,bog=141,hosp="26 (Tunja III)",land="11–18k",note="WET NE FLANK — best water security; +609mm surplus. Scorecard #1 region.")),
 "Gachantivá":      (5.7558,-73.5478, dict(g="flank",elev=2450,ai="~1.4 (wet flank)",fault=55,bog=134,hosp="32 (Tunja III)",land="4–78k",note="Wet flank; cheapest buildable land in study; paved Gachantivá–VdL road.")),
 "Santa Sofía":     (5.7133,-73.6019, dict(g="flank",elev=2387,ai="~1.3 (wet flank)",fault=52,bog=127,hosp="33 (Tunja III)",land="12–25k",note="Wet flank; large cheap parcels with nacimientos.")),
 "Villa de Leyva":  (5.6339,-73.5250, dict(g="vdl",elev=2149,ai="0.63 (dry-subhumid)",fault=63,bog=124,hosp="21 (Tunja III)",land="41–390k",note="Best climate/beauty, but WATER-CONSTRAINED (10 deficit mo; El Niño→rationing), heritage limits, most expensive.")),
 "Sáchica":         (5.5847,-73.5447, dict(g="dry",elev=2150,ai="0.43 (semi-arid)",fault=64,bog=118,hosp="22 (Tunja III)",land="38–368k",note="Dry SW valley — avoid unless water is fully solved.")),
 "Tunja":           (5.5353,-73.3678, dict(g="tunja",elev=2782,ai="0.50 (semi-arid)",fault=59,bog=126,hosp="1.5 (in-city III)",land="15–108k",note="Best everyday services (Nivel III hospital, capital) + strongest road pipeline; but cold ~13°C, driest, no airport.")),
 "El Colegio / Mesitas":(4.5797,-74.4442, dict(g="teq",elev=1100,ai="0.73 (sub-humid)",fault=35,bog=36,hosp="6 (La Mesa II)",land="49–130k",note="Warm ~23°C templado; BEST airport access (~1h47); but HIGH landslide susceptibility + chronic access-corridor closures.")),
 "Tena":            (4.6558,-74.3906, dict(g="teq",elev=1384,ai="~sub-humid",fault=32,bog=27,hosp="9 (La Mesa II)",land="18–38k",note="Cheapest Tequendama land; very airport-close; verify slope.")),
 "San Antonio Teq.":(4.6167,-74.3500, dict(g="teq",elev=1540,ai="~sub-humid",fault=27,bog=24,hosp="13 (La Mesa II)",land="11–105k",note="Closest to El Dorado; steep, landslide-prone descent.")),
 "La Mesa":         (4.6320,-74.4620, dict(g="teq",elev=1200,ai="~sub-humid",fault=35,bog=36,hosp="0.3 (Nivel II)",land="75–250k",note="Tequendama hub; Nivel II hospital in-town; priciest Tequendama land.")),
}
GCOL={"flank":"#2c7a4b","vdl":"#d9932b","dry":"#b0ب0b0".replace("ب","b"),"tunja":"#6c7a89","teq":"#3a7bd5"}
# Shortlisted parcels, grouped BY MUNICIPALITY at the municipal seat.
# Deliberate: listings give vereda names only, never coordinates or cadastral boundaries, so a
# per-parcel pin would be an invented position. Getting exact coords from the agencies is an open
# item (see CLAUDE.md). Each pin's popup lists that municipality's live candidates.
PARCEL_GROUPS = [
 ("Moniquirá — the warm flank", 5.8759, -73.5733, [
   ("H · geotech lote", "COP 720 M · 8.0 ha · 9,000/m²",
    "Best building land found; soil + water studies handed over; fenced; negotiable",
    "fincaraiz.com.co/lote-en-venta-en-moniquira/193363278"),
   ("G · Papayal", "COP 390 M · 9.11 ha · 4,281/m²",
    "Cheapest usable land; real quebrada — but limestone karst, and the vereda aqueduct is IRCA high-risk",
    "fincaraiz.com.co/finca-en-venta-en-papayal-moniquira/192742687"),
   ("N · finca panelera", "COP 1,700 M · 40.96 ha · 4,150/m²",
    "Working trapiche + 2 houses + own aljibes; the ONLY candidate above the 9.38 ha UAF, so the only divisible one",
    "fincaraiz.com.co/finca-en-venta-en-moniquira/192463144"),
   ("K · Neval y Cruces lots", "COP 170 M · 5,000–8,821 m² each",
    "Individually titled lots — each with its own matrícula; services already in",
    "fincaraiz.com.co/lote-en-venta-en-neval-y-cruces-moniquira/193893121"),
   ("E · San Cristóbal (⚠ mis-tagged)", "COP 750 M · 8.5 ha",
    "Listing text says San Cristóbal, the URL says Neval y Cruces — verify on the matrícula",
    "fincaraiz.com.co/finca-en-venta-en-neval-y-cruces-moniquira/192899845"),
 ]),
 ("Arcabuco — the cool highland", 5.7597, -73.4372, [
   ("A · Peñas Blancas (with house)", "COP 400 M · 2.97 ha · 13,472/m²",
    "4-bed casa campestre, fireplace, quebrada + potable tank; 1.3 km off the paved road",
    "fincaraiz.com.co/finca-en-venta-en-arcabuco/193601271"),
   ("B · Peñas Blancas (blank)", "COP 270 M · 2.43 ha · 11,102/m²",
    "Cheapest highland; nacimiento + quebrada + reservorios; visibly browns off in the dry season",
    "fincaraiz.com.co/finca-en-venta-en-arcabuco/192742902"),
   ("D · Monte Suárez", "COP 1,600 M · 8.93 ha",
    "Best finished house in the set — but its head touches SFF Iguaque. Clear the boundary first",
    "fincaraiz.com.co/finca-en-venta-en-monte-suarez-arcabuco/192742895"),
 ]),
 ("Gachantivá — the cool highland", 5.7558, -73.5478, [
   ("C · La Hoya", "COP 230 M · 5.45 ha · 4,216/m²",
    "Lushest and wettest, with a visible spring — but dense bracken regrowth and a steep basin",
    "fincaraiz.com.co/finca-en-venta-en-la-hoya-gachantiva/192743485"),
 ]),
]
REF={"El Dorado Intl (BOG)":(4.7016,-74.1469,"International gateway — the fly-in/out airport"),
     "Hosp. San Rafael Tunja (Nivel III)":(5.5410,-73.3560,"Only 3rd-level hospital in Boyacá"),
     "Hosp. Pedro León, La Mesa (Nivel II)":(4.6300,-74.4640,"Tequendama referral hospital"),
     "SFF Iguaque (páramo water source, ~3800m)":(5.6850,-73.4560,"Water factory feeding Villa de Leyva; protected — build outside its buffer")}

m=folium.Map(location=[5.15,-74.0],zoom_start=8,tiles=None,control_scale=True)
folium.TileLayer("OpenStreetMap",name="Street").add_to(m)
folium.TileLayer("https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png",attr="OpenTopoMap (CC-BY-SA)",name="Terrain (relief)").add_to(m)
folium.TileLayer("https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",attr="Esri",name="Satellite").add_to(m)
folium.TileLayer("CartoDB positron",name="Light").add_to(m)

# municipal boundaries
try:
    gj=json.load(open("data/admin/municipios_study.geojson"))
    def bstyle(f):
        nm=(f["properties"].get("NOMBRE_MPI") or "").title()
        c={"Arcabuco":"#2c7a4b","Gachantiva":"#2c7a4b","Gachantivá":"#2c7a4b","Santa Sofia":"#2c7a4b","Santa Sofía":"#2c7a4b",
           "Villa De Leyva":"#d9932b","Sachica":"#b0b0b0","Sáchica":"#b0b0b0","Tunja":"#6c7a89"}.get(nm,"#3a7bd5")
        return {"color":c,"weight":2,"fillColor":c,"fillOpacity":0.06}
    fg=FeatureGroup(name="Municipal boundaries",show=True)
    folium.GeoJson(gj,style_function=bstyle,tooltip=folium.GeoJsonTooltip(fields=["NOMBRE_MPI"],aliases=["Municipio:"])).add_to(fg)
    fg.add_to(m)
except Exception as e: print("boundaries:",e)

# active faults
fg_f=FeatureGroup(name="Active faults (GEM DB)",show=False)
gf=gpd.read_file("data/seismic/gem_faults_co.geojson")
for _,r in gf.iterrows():
    g=r.geometry
    if g is None: continue
    lines=[g] if g.geom_type=="LineString" else list(g.geoms) if g.geom_type=="MultiLineString" else []
    for ln in lines:
        pts=[(y,x) for x,y in ln.coords]
        PolyLine(pts,color="#c0392b",weight=1.8,opacity=0.7,
                 tooltip=f"{r.get('name','fault')} · {r.get('slip_type','')}").add_to(fg_f)
fg_f.add_to(m)

# candidate sectors
fg_s=FeatureGroup(name="Candidate sectors",show=True)
for name,(lat,lon,d) in SEC.items():
    col=GCOL.get(d["g"],"#3a7bd5")
    html=(f"<b>{name}</b><br><span style='color:#555'>{d['note']}</span><hr style='margin:5px 0'>"
          f"Elev: {d['elev']} m &nbsp;|&nbsp; Water AI: <b>{d['ai']}</b><br>"
          f"Nearest active fault: {d['fault']} km<br>"
          f"To El Dorado (BOG): {d['bog']} km (straight-line)<br>"
          f"To hospital: {d['hosp']} km<br>Land: {d['land']} COP/m²")
    CircleMarker([lat,lon],radius=9,color=col,fill=True,fill_color=col,fill_opacity=0.85,
                 popup=folium.Popup(html,max_width=290),tooltip=name).add_to(fg_s)
fg_s.add_to(m)

# shortlisted parcels
fg_p=FeatureGroup(name="Shortlisted parcels (by municipality)",show=True)
for gname,glat,glon,items in PARCEL_GROUPS:
    rows="".join(
        f"<div style='margin:7px 0;padding-left:8px;border-left:3px solid #2c7a4b'>"
        f"<b>{n}</b><br><span style='color:#b5613a'>{pr}</span><br>"
        f"<span style='color:#555;font-size:12px'>{ft}</span><br>"
        f"<a href='https://{u}' target='_blank'>listing &#8599;</a></div>"
        for n,pr,ft,u in items)
    html=(f"<b style='font-size:14px'>{gname}</b><br>"
          f"<span style='color:#666;font-size:12px'>{len(items)} live candidate(s)</span>{rows}"
          f"<div style='color:#999;font-size:11px;margin-top:6px'>Pin = municipal seat. Listings give "
          f"vereda names only — no coordinates or cadastral boundaries — so parcels are NOT plotted "
          f"individually. Exact coordinates are an open diligence item.</div>")
    Marker([glat,glon],icon=folium.Icon(color="green",icon="home",prefix="fa"),
           popup=folium.Popup(html,max_width=330),
           tooltip=f"{gname} ({len(items)})").add_to(fg_p)
fg_p.add_to(m)

# reference points
fg_r=FeatureGroup(name="Reference (airport, hospitals, water)",show=True)
for nm,(lat,lon,desc) in REF.items():
    ic="plane" if "Dorado" in nm else ("tint" if "Iguaque" in nm else "plus-square")
    cc="red" if "Dorado" in nm else ("blue" if "Iguaque" in nm else "purple")
    Marker([lat,lon],icon=folium.Icon(color=cc,icon=ic,prefix="fa"),
           popup=folium.Popup(f"<b>{nm}</b><br>{desc}",max_width=250),tooltip=nm).add_to(fg_r)
fg_r.add_to(m)

# legend
legend=("<div style='position:fixed;bottom:24px;left:14px;z-index:9999;background:#fff;padding:10px 12px;"
 "border:1px solid #ccc;border-radius:6px;font:12px/1.5 -apple-system,Arial;box-shadow:0 1px 5px rgba(0,0,0,.2)'>"
 "<b>Candidate sectors</b><br>"
 "<span style='color:#2c7a4b'>●</span> Ricaurte wet NE flank (recommended)<br>"
 "<span style='color:#d9932b'>●</span> Villa de Leyva town belt<br>"
 "<span style='color:#6c7a89'>●</span> Tunja (services anchor)<br>"
 "<span style='color:#3a7bd5'>●</span> El Colegio / Tequendama<br>"
 "<span style='color:#b0b0b0'>●</span> Dry SW valley (avoid)<br>"
 "<span style='color:green'>⌂</span> shortlisted real parcels &nbsp; <span style='color:#c0392b'>—</span> active faults</div>")
m.get_root().html.add_child(folium.Element(legend))
LayerControl(collapsed=False).add_to(m)
m.fit_bounds([[4.45,-74.6],[5.85,-73.25]])
m.save("outputs/hacienda_map.html")
print("Saved outputs/hacienda_map.html")
