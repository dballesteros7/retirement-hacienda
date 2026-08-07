"""Re-download the source geodata that is gitignored (large), and rebuild the small
derived files the pipeline actually uses. Run once after a fresh clone if
data/admin/municipios_study.geojson or data/seismic/gem_faults_co.geojson is missing."""
import requests, json, os, sys
sys.path.insert(0, "code")
from data_inputs import GEM_FAULTS_URL, MPIO_GEOJSON_URL, DANE

os.makedirs("data/admin", exist_ok=True); os.makedirs("data/seismic", exist_ok=True)

def dl(url, path):
    r = requests.get(url, timeout=120); r.raise_for_status()
    open(path, "wb").write(r.content); return len(r.content)

# municipal boundaries -> filter to the study municipalities
print("municipal boundaries…", dl(MPIO_GEOJSON_URL, "data/admin/mpio_co.json"), "bytes")
gj = json.load(open("data/admin/mpio_co.json"))
feats = gj["features"] if isinstance(gj, dict) else gj
codes = set(DANE.values())
sub = [f for f in feats if str(f["properties"].get("MPIOS")) in codes]
json.dump({"type": "FeatureCollection", "features": sub},
          open("data/admin/municipios_study.geojson", "w"))
print("  matched municipalities:", len(sub))

# GEM active faults -> filter to the Colombia bbox
print("GEM active faults…", dl(GEM_FAULTS_URL, "data/seismic/gem_faults_world.geojson"), "bytes")
gf = json.load(open("data/seismic/gem_faults_world.geojson"))
def pts(geom):
    c, t = geom["coordinates"], geom["type"]
    lines = [c] if t == "LineString" else (c if t == "MultiLineString" else [])
    for ln in lines:
        for p in ln: yield p[0], p[1]
co = [f for f in gf["features"]
      if any((-80 <= x <= -71) and (2 <= y <= 9) for x, y in pts(f["geometry"]))]
json.dump({"type": "FeatureCollection", "features": co},
          open("data/seismic/gem_faults_co.geojson", "w"))
print("  Colombia-region faults:", len(co))
print("Done.")
