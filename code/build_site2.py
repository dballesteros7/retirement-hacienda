"""Rebuild the GitHub Pages site bundle, now including the Arcabuco dossier + updated nav."""
import os, shutil, zipfile
SITE="outputs/site"; os.makedirs(SITE, exist_ok=True)

NAV=("<div style='background:#5b7a5b;color:#fff;text-align:center;padding:9px;font-size:13.5px;font-family:-apple-system,Arial'>"
     "Our Hacienda &nbsp;·&nbsp; <a href='index.html' style='color:#fff'>Overview</a> &nbsp;·&nbsp; "
     "<a href='report.html' style='color:#fff'>Report</a> &nbsp;·&nbsp; "
     "<a href='scorecard.html' style='color:#fff'>Scorecard</a> &nbsp;·&nbsp; "
     "<a href='map.html' style='color:#fff'>Map</a> &nbsp;·&nbsp; "
     "<a href='dossier.html' style='color:#fff;font-weight:700'>Arcabuco dossier</a></div>")

# index = overview, footer links swapped to relative + dossier, nav injected
ov=open("outputs/hacienda_overview.html",encoding="utf-8").read()
old="The full report (with all the evidence and sources) and the interactive map are in our shared Claude artifacts."
new=("Explore the full detail: <a href='report.html' style='color:var(--sage);font-weight:600'>full report</a> · "
     "<a href='scorecard.html' style='color:var(--sage);font-weight:600'>scorecard</a> · "
     "<a href='map.html' style='color:var(--sage);font-weight:600'>map</a> · "
     "<a href='dossier.html' style='color:var(--sage);font-weight:600'>Arcabuco property dossier</a>.")
ov=ov.replace(old,new).replace("<body>","<body>"+NAV)
open(f"{SITE}/index.html","w",encoding="utf-8").write(ov)

# interactive pages copied unchanged (avoid touching folium/scorecard JS)
for src,dst in [("outputs/final_report.html","report.html"),
                ("outputs/scorecard_interactive.html","scorecard.html"),
                ("outputs/hacienda_map.html","map.html")]:
    shutil.copyfile(src, f"{SITE}/{dst}")

# dossier page = arcabuco dossier with nav injected
dos=open("outputs/arcabuco_dossier.html",encoding="utf-8").read().replace("<body>","<body>"+NAV,1)
open(f"{SITE}/dossier.html","w",encoding="utf-8").write(dos)

open(f"{SITE}/README.md","w").write("# Retirement Hacienda — shared site\nStatic site (no build step). index.html is the overview; report/scorecard/map/dossier are linked from the top nav. Publish/refresh with GitHub Pages (Deploy from branch: main / root).\n")

z="outputs/hacienda_site.zip"
with zipfile.ZipFile(z,"w",zipfile.ZIP_DEFLATED) as f:
    for fn in sorted(os.listdir(SITE)): f.write(f"{SITE}/{fn}", fn)
print("Site files:", sorted(os.listdir(SITE)))
print("dossier.html:", round(os.path.getsize(f'{SITE}/dossier.html')/1e6,2),"MB · zip:", round(os.path.getsize(z)/1e6,2),"MB")
