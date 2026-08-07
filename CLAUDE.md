# Retirement Hacienda — project context

Working repo for a real land-purchase decision: a group of Europe-based friends buying rural land in the Colombian central highlands to build and eventually retire to a hacienda. ~30-year horizon.

This file is the handoff brief. Read it first; it tells you what has been decided, what is still open, how to rebuild every artifact, and how to publish.

---

## 1. Where the analysis landed

**Recommendation: buy on the wet north-east flank of the Ricaurte valley — Arcabuco / Gachantivá / Santa Sofía (Boyacá)** — rather than in Villa de Leyva's town belt. This ranked #1 under *every* weighting tested (default, climate-first, water-first, services-first, cost-first).

Why: water. A radiation-aware (Hargreaves) monthly water balance shows the wet flank at aridity index **1.48 (humid, ~609 mm surplus, 1 deficit month)**, resilient even under an El Niño drought, while every valley-floor option runs a chronic seasonal deficit and goes to 12 deficit months in a drought — the mechanism behind Villa de Leyva's documented 2016 rationing. The flank is also the cheapest land (~4–18k COP/m² vs ~110k in Villa de Leyva town), keeps a mild climate, sits in a low-crime province, and has no heritage-construction overlay.

Live alternatives: **El Colegio / Mesitas (Tequendama)** if airport access dominates (~1 h 47 to El Dorado vs ~3 h from Boyacá) — but confirmed high landslide susceptibility and chronic access-corridor closures. **Tunja** is the services/hospital anchor (only Nivel III hospital in Boyacá), not the residence — cold ~13 °C, no nearby airport.

**Corrections to the original brief that stuck** (see `docs/phase0_verification.md`): Mesitas is a pleasant ~23 °C *templado* mean, not "warm 25–28 °C"; Villa de Leyva's water constraint is tighter than stated (~54 L/s for ~30k people + tourists); Boyacá↔Bogotá is ~3 h, not ~1.5 h; Villa de Leyva's Río Cane concession is 34 L/s (40 L/s is plant capacity).

### The property-level fork (from the Arcabuco deep dive)

Nine real listings were photo-scrutinized in-browser. Two tracks emerged — **pick the climate first, then the parcel**:

- **Cool green highland (~2,100–2,700 m, ~13–16 °C)** — Arcabuco & Gachantivá. The original wet-flank thesis: lush, cool, beautiful. But **steep** — net-buildable flat area and protected-boundary proximity are the binding constraints. Top picks: **A** Peñas Blancas w/ house (COP 400 M, 2.97 ha), **C** Gachantivá/La Hoya (COP 230 M, 5.45 ha — cheapest, wettest, but how much is buildable?), **B** Peñas Blancas blank (COP 270 M).
- **Warm Moniquirá flank (~1,700 m, ~19 °C)** — north on paved Ruta 62. The **gentlest, cheapest, most genuinely buildable land found**, with abundant water — at the cost of a warm subtropical lifestyle and ~40 min more distance. Top picks: **G** Papayal (COP 390 M, 9.11 ha, flattest land in the whole search), **H** geotech-lote (COP 720 M, 8 ha, soil+water studies already done, fenced).

Full per-parcel reads: `docs/arcabuco_scrutiny.md`, `docs/arcabuco_inventory.md`, rendered in `dossier.html`.

### Two constraints that gate every Arcabuco-area parcel

1. **Protected land.** Arcabuco's high south-west third is **SFF Iguaque national park + the delimited Páramo Iguaque-Merchán** (MADS Res. 1555/2016; Ley 1930/2018 bans new construction). The wettest, most forested, spring-fed parcels are often exactly the ones near this edge — *a listing's charm can be its legal poison*. Overlay every candidate on the park, the páramo, the Serranía El Peligro reserve, and ~30 m ronda-hídrica setbacks before any offer. This is the open question on candidate **D** (Monte Suárez).
2. **UAF ≈ 9.9 ha** subdivision floor in Arcabuco → you cannot carve small lots. Buy **one titled parcel held in a shared Colombian SAS** (exits transfer shares, no partition risk, shares outside the non-resident wealth-tax base; wealth-tax exposure is ~nil at these parcel values).

---

## 2. Repo layout

```
/                        repo root = the PUBLISHED SITE (GitHub Pages serves from main / root)
  index.html             overview (friend-facing landing page)
  report.html            full site-selection report
  scorecard.html         interactive weighted scorecard
  map.html               interactive Leaflet map
  dossier.html           Arcabuco property dossier (9 parcels, photos)
  CLAUDE.md              this file
  build.sh               regenerates every artifact, then copies the site to root
  requirements.txt
  code/                  the analysis + build pipeline (Python)
  data/                  input geodata (municipal boundaries, GEM active faults)
  docs/                  the research corpus (markdown, all cited)
  outputs/               build products (incl. outputs/shots/ = browser screenshots used by the dossier)
  logs/methods_log.md    method + reproducibility log
```

`docs/` is the source of truth for prose; `report.html` is generated from `docs/final_report.md`. Edit the markdown, not the HTML.

### Pipeline (what generates what)

| Script | Reads | Writes |
|---|---|---|
| `code/water_balance.py` | `code/data_inputs.py` (IDEAM normals) | `water_balance_summary.csv`, `fig_water_balance.png` |
| `code/geo_metrics.py` | `data/seismic/gem_faults_co.geojson` | `geo_metrics.csv` (fault distances, accessibility) |
| `code/scorecard.py` | inline scores | `scorecard_scores.csv`, `scorecard_data.json` |
| `code/build_scorecard_html.py` | `scorecard_data.json` | `scorecard_interactive.html` |
| `code/build_map.py` | `data/admin/*`, `data/seismic/*` | `hacienda_map.html` |
| `code/build_report_html.py` | `docs/final_report.md`, `fig_water_balance.png` | `final_report.html` |
| `code/build_overview.py` | `scorecard_data.json`, `fig_water_balance.png` | `hacienda_overview.html` |
| `code/build_dossier2.py` | `outputs/shots/*.jpg` | `arcabuco_dossier.html` |
| `code/build_site2.py` | the above | `outputs/site/*` (then `build.sh` copies to root) |

`code/data_inputs.py` holds every captured numeric input (climate normals, projection ranges, NSR-10 seismic values, DANE codes) with a source + reliability flag on each. **That file is where new hard data goes.**

---

## 3. How to rebuild and publish

```bash
pip install -r requirements.txt      # geopandas, rasterio, folium, matplotlib, markdown, …
./build.sh                           # regenerates every artifact + refreshes the site at repo root
git add -A && git commit -m "…" && git push
```

GitHub Pages (Deploy from branch → `main` → `/root`) republishes in ~1 minute:
**https://dballesteros7.github.io/retirement-hacienda/** · dossier at `/dossier.html`.

The `code/`, `data/`, `docs/`, `outputs/` folders sit in the repo but are ignored by Pages, which only serves the root `*.html`. So source and site live together with no extra configuration.

---

## 4. What the cloud sandbox could NOT do — and you probably can

The original analysis ran in a sandbox whose network was allow-listed to PyPI + GitHub only. Several planned methods were blocked and were substituted with published data (all disclosed in `logs/methods_log.md`). **On a local machine with normal internet, these unlock — they are the highest-value next steps:**

- **Download a real DEM** (Copernicus GLO-30 from AWS, or OpenTopography) for the Arcabuco AOI → compute actual **slope / aspect / buildable-land polygons**. This directly answers the single biggest open question: *how many gentle, clear hectares does each parcel really have?* Terrain is currently read visually from photos + OpenTopoMap contours.
- **Routing** (OSRM / OpenRouteService / Valhalla) → real drive-time isochrones to El Dorado, Tunja's Nivel III hospital, Villa de Leyva. Current drive-times are documented values + straight-line distances.
- **The blocked property portals** — Metrocuadrado, Mercado Libre, Properati, Ciencuadras — were unreachable. FincaRaíz was the only searchable source, so the ~12-listing inventory is almost certainly incomplete, especially for Chíquiza/Iguaque. A manual or scripted sweep would widen the pool.
- **Official Colombian portals** (SGC seismic-hazard, IGAC, Corpoboyacá, IDEAM DHIME) were egress-blocked → exact NSR-10 Aa/Av for El Colegio & Villa de Leyva, precise SGC mass-movement susceptibility, and the protected-area polygons are still unverified. **Getting the Corpoboyacá / Parques Nacionales SFF Iguaque + páramo shapefiles and overlaying the candidate parcels is the highest-value legal check available computationally.**

---

## 5. Open items

- [ ] Overlay each shortlisted parcel on SFF Iguaque / páramo Iguaque-Merchán / Serranía El Peligro / rondas hídricas (esp. **D — Monte Suárez**).
- [ ] Compute real slope + buildable polygons per candidate from a downloaded DEM (esp. **C — La Hoya**, whose buildable share is the open question, and **G — Papayal**, to confirm the flat impression).
- [ ] Exact NSR-10 **Aa/Av** for El Colegio and Villa de Leyva (NSR-10 Apéndice A-4 / SGC portal).
- [ ] Widen inventory via the blocked portals + a direct approach to the listing agencies (**ATOS Inmobiliaria** holds most Arcabuco/Moniquirá raw land; **Casa 360** has H; **Rubén Quiroga** has I).
- [ ] Decide the climate fork (cool highland vs warm Moniquirá) with the group — the scorecard at `scorecard.html` is the tool for that conversation.
- [ ] Draft outreach to the agencies for exact coordinates, Certificado de Tradición y Libertad, and water-concession papers on the top parcels.
- [ ] Optional: replace the dossier's embedded FincaRaíz listing photos with links, if rehosting third-party listing images on a public site is a concern.

---

## 6. Working rules for this project

- **Never fabricate** coordinates, prices, parcels, or hazard values. Mark gaps "unknown / needs field survey." This is grounding a real purchase.
- **Cite every datum** with source + URL + access date. Prefer primary/official: SGC, IDEAM, IGAC, MinSalud REPS, ANT, SNR, Corpoboyacá / CAR Cundinamarca, ANI/INVÍAS, DANE, Mincultura, Parques Nacionales, GEM.
- **Report ranges and uncertainty**, especially for climate projections — never a single downscaled value as certainty.
- Treat every listing claim ("own water", "paved access", "X hectares") as **the seller's claim** until a surveyor confirms it. Portal listings in this market are frequently mis-tagged to the wrong municipality — several were caught during the inventory.
- This is **decision-support, not legal, engineering, or financial advice.** Title work needs a Colombian abogado/notario; any parcel needs on-site geotechnical, hydrogeological, and structural survey before purchase or construction.
- Keep `docs/` as the prose source of truth and regenerate HTML via `build.sh`; log new methods and sources in `logs/methods_log.md`.
