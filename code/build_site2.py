"""Assemble the GitHub Pages bundle and give the five pages one coherent navigation.

Each page has one job, and the nav says so:
  index      the decision      — shortlist, costs, the community plan
  report     why here          — the regional evidence and the ranking
  dossier    which parcel      — twelve candidates, every photo reviewed
  scorecard  weigh it yourself — the interactive tool
  map        where             — the geography

Previously only index and dossier carried the nav, so report/scorecard/map were dead ends.
All five now get it, with a you-are-here state. The folium map gets a floating pill instead of
a full bar, because folium positions its container absolutely and a bar would overlap it.
"""
import os, shutil, zipfile

SITE = "outputs/site"
os.makedirs(SITE, exist_ok=True)

PAGES = [("index.html", "Overview", "the decision"),
         ("report.html", "Report", "why here"),
         ("dossier.html", "Dossier", "which parcel"),
         ("scorecard.html", "Scorecard", "weigh it up"),
         ("map.html", "Map", "where")]

NAV_CSS = (
 "<style>"
 ".sitenav{background:#5b7a5b;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;"
 "display:flex;flex-wrap:wrap;justify-content:center;gap:2px;padding:7px 10px}"
 ".sitenav a{color:#e8efe6;text-decoration:none;font-size:13px;padding:5px 13px;border-radius:16px;white-space:nowrap}"
 ".sitenav a small{opacity:.62;font-size:11.5px;margin-left:5px}"
 ".sitenav a:hover{background:rgba(255,255,255,.13)}"
 ".sitenav a.here{background:#fff;color:#3f5f3f;font-weight:700}"
 ".sitenav a.here small{opacity:.62}"
 "</style>")


def nav(current):
    links = "".join(
        f"<a href='{h}' class='{'here' if h == current else ''}'>{lbl}<small>{sub}</small></a>"
        for h, lbl, sub in PAGES)
    return NAV_CSS + f"<div class='sitenav'>{links}</div>"


def inject(html, current):
    """Put the nav immediately after <body>, whatever attributes the tag carries."""
    i = html.lower().find("<body")
    if i == -1:
        return nav(current) + html
    j = html.index(">", i) + 1
    return html[:j] + nav(current) + html[j:]


# ---- index: overview -------------------------------------------------------------------------
ov = open("outputs/hacienda_overview.html", encoding="utf-8").read()
open(f"{SITE}/index.html", "w", encoding="utf-8").write(inject(ov, "index.html"))

# ---- report + scorecard: nav injected, content untouched --------------------------------------
for src, dst in [("outputs/final_report.html", "report.html"),
                 ("outputs/scorecard_interactive.html", "scorecard.html")]:
    open(f"{SITE}/{dst}", "w", encoding="utf-8").write(
        inject(open(src, encoding="utf-8").read(), dst))

# ---- dossier ----------------------------------------------------------------------------------
open(f"{SITE}/dossier.html", "w", encoding="utf-8").write(
    inject(open("outputs/arcabuco_dossier.html", encoding="utf-8").read(), "dossier.html"))

# ---- map: floating pill, so folium's absolutely-positioned container is not overlapped ---------
PILL = ("<style>.mapnav{position:fixed;top:12px;left:50%;transform:translateX(-50%);z-index:99999;"
        "background:rgba(91,122,91,.96);border-radius:20px;padding:6px 8px;display:flex;gap:2px;"
        "font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;"
        "box-shadow:0 2px 10px rgba(0,0,0,.25)}"
        ".mapnav a{color:#e8efe6;text-decoration:none;font-size:12.5px;padding:4px 11px;border-radius:14px}"
        ".mapnav a:hover{background:rgba(255,255,255,.15)}"
        ".mapnav a.here{background:#fff;color:#3f5f3f;font-weight:700}</style>")
mp = open("outputs/hacienda_map.html", encoding="utf-8").read()
pill_links = "".join(f"<a href='{h}' class='{'here' if h == 'map.html' else ''}'>{lbl}</a>"
                     for h, lbl, _ in PAGES)
i = mp.lower().find("<body")
j = mp.index(">", i) + 1
mp = mp[:j] + PILL + f"<div class='mapnav'>{pill_links}</div>" + mp[j:]
open(f"{SITE}/map.html", "w", encoding="utf-8").write(mp)

open(f"{SITE}/README.md", "w").write(
 "# Retirement Hacienda — shared site\n\n"
 "Static site, no build step at serve time. Five pages, one job each:\n\n"
 "| page | question it answers |\n|---|---|\n"
 "| `index.html` | the decision — shortlist, costs, the community plan |\n"
 "| `report.html` | why here — regional evidence and the ranking |\n"
 "| `dossier.html` | which parcel — twelve candidates, every photo reviewed |\n"
 "| `scorecard.html` | what if we weight it differently |\n"
 "| `map.html` | where |\n\n"
 "Regenerate everything with `./build.sh` from the repo root. "
 "Published via GitHub Pages (Deploy from branch: main / root).\n")

z = "outputs/hacienda_site.zip"
with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as f:
    for fn in sorted(os.listdir(SITE)):
        f.write(f"{SITE}/{fn}", fn)

print("Site files:", sorted(os.listdir(SITE)))
for h, lbl, sub in PAGES:
    size = os.path.getsize(f"{SITE}/{h}") / 1e6
    print(f"  {h:16s} {size:6.2f} MB   {lbl} — {sub}")
print("zip:", round(os.path.getsize(z) / 1e6, 2), "MB")
