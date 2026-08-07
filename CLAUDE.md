# Retirement Hacienda — project context

Working repo for a real land-purchase decision: a group of Europe-based friends buying rural land in the Colombian central highlands to build and eventually retire to a hacienda. ~30-year horizon.

This file is the handoff brief. Read it first; it tells you what has been decided, what is still open, how to rebuild every artifact, and how to publish.

---

## 1. Where the analysis landed

**Recommendation: buy on the wet north-east flank of the Ricaurte valley — Arcabuco / Gachantivá / Santa Sofía (Boyacá)** — rather than in Villa de Leyva's town belt. This ranked #1 under *every* weighting tested (default, climate-first, water-first, services-first, cost-first).

Why: water. A radiation-aware (Hargreaves) monthly water balance shows the wet flank at aridity index **1.48 (humid, ~609 mm surplus, 1 deficit month)**, resilient even under an El Niño drought, while every valley-floor option runs a chronic seasonal deficit and goes to 12 deficit months in a drought — the mechanism behind Villa de Leyva's documented 2016 rationing. The flank is also the cheapest land (~4–18k COP/m² vs ~110k in Villa de Leyva town), keeps a mild climate, sits in a low-crime province, and has no heritage-construction overlay.

Live alternatives: **El Colegio / Mesitas (Tequendama)** if airport access dominates (~1 h 47 to El Dorado vs ~3 h from Boyacá) — but confirmed high landslide susceptibility and chronic access-corridor closures. **Tunja** is the services/hospital anchor (only Nivel III hospital in Boyacá), not the residence — cold ~13 °C, no nearby airport.

**Corrections to the original brief that stuck** (see `docs/phase0_verification.md`): Mesitas is a pleasant ~23 °C *templado* mean, not "warm 25–28 °C"; Villa de Leyva's water constraint is tighter than stated (~54 L/s for ~30k people + tourists); Boyacá↔Bogotá is ~3 h, not ~1.5 h; Villa de Leyva's Río Cane concession is 34 L/s (40 L/s is plant capacity).

### The property-level fork — measured (revised 2026-08-08)

Nine real listings were photo-scrutinized in-browser; all re-verified 8 Aug 2026 as **live at unchanged prices**. Two tracks are on the table. **v3 rescoped the dossier to these two** and dropped F (Villa de Leyva — water-constrained side) and I (Santa Sofía — 0.72 ha, too small).

The original framing was "cool-but-steep vs warm-and-flat". With a real DEM and the Corpoboyacá POMCA, that is only half right:

- **Terrain is nearly a tie.** In the elevation band where parcels actually trade, median slope is **10.2° (Moniquirá) vs 10.5° (Arcabuco)**. The difference is the tail — Arcabuco holds **2.6× more land above 25°** (12.5% vs 4.8%). So the highland isn't steep on average; it has more bad pockets, which means **parcel selection matters far more there**. The old "Arcabuco is steep" line came from the whole-area figure (27.4% >25°), which includes the Iguaque massif where nothing is sold.
- **Water is the one real gap, and it favours Arcabuco.** Both get the same rain (1,826 vs 1,860 mm). Moniquirá is 4.8 °C warmer ⇒ PET 1,421 vs 1,233 mm ⇒ an El Niño drought takes it to **10 deficit months vs Arcabuco's 3**. In a *normal* year Moniquirá has **zero** deficit months and a 439 mm surplus — it is genuinely humid. The gap is drought resilience.
- **Services favour Moniquirá decisively.** **Hospital Regional de Moniquirá E.S.E., Nivel I *and II*, 118 servicios habilitados** — and it is the nearest second-level care for the highland too (Arcabuco 19.8 km, Gachantivá 13.6 km, both closer than Tunja).
- **Cost is a tie** — G/Papayal ~4,300 COP/m² and C/La Hoya ~4,200, one on each flank.

**Cool highland** top picks: **A** Peñas Blancas w/ house (400 M, 2.97 ha), **C** Gachantivá/La Hoya (230 M, 5.45 ha), **B** Peñas Blancas blank (270 M).
**Warm flank** top picks: **G** Papayal (390 M, 9.11 ha), **H** geotech-lote (720 M, 8 ha), plus two new finds — **N** (1,700 M, **40.96 ha**, same COP/m² as G and the only parcel above the UAF, so the only lawfully divisible one) and **K** (Neval y Cruces lots with **individual matrículas already issued**).

Full per-parcel reads: `docs/arcabuco_scrutiny.md`, `docs/arcabuco_inventory.md`, the Moniquirá analysis in `docs/moniquira_deep_dive.md`, all rendered in `dossier.html`.

### Where the scorecard lands now

Adding Moniquirá as its own unit means the wet flank **no longer wins every weighting**: it leads four of five, Moniquirá takes **services-first** (72.9 vs 72.8), and climate-first is a 0.3-point dead heat. Water-first is the only clear separation (77.7 vs 73.7). **The group's lean toward Moniquirá is defensible** — the trade to settle consciously is health services now vs drought resilience over 30 years.

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
| `code/slope_analysis.py` | Copernicus GLO-30 tile → `data/dem/` (cached, gitignored) | `slope_summary.csv`, `fig_slope.png` |
| `code/masterplan.py` | inline 2026 unit rates | `masterplan_summary.csv`, `masterplan_budget_*.csv`, `masterplan_phases.csv`, `fig_masterplan.png` |
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

- ✅ **DONE 2026-08-08 — real DEM.** Copernicus GLO-30 now downloads and drives `code/slope_analysis.py` (build stage 3/10). Result above. **Caveat that remains:** listings are located at *vereda* level with no coordinates or cadastral boundaries, so slope is **area-level, not per-parcel** — it says which flank is gentler, not how many flat hectares parcel G or C has.
- ✅ **DONE 2026-08-08 — Corpoboyacá.** The POMCA Medio y Bajo Suárez is reachable and now supplies per-subcatchment precipitation, mean slope and the IUA/IRH/IVH water indices. The Moniquirá PDM 2020-2023 supplies UAF, hospital level, IRCA water quality, hazards and roads.
- ✅ **DONE 2026-08-08 — the blocked portals.** Metrocuadrado, Mercado Libre, Properati and Ciencuadras are all reachable. A FincaRaíz sweep of Moniquirá returned 22 lotes/fincas and five group-relevant new entries (K, L, M, N, O). **Chíquiza/Iguaque was not swept** — still open.
- **Routing** (OSRM / OpenRouteService / Valhalla) → real drive-time isochrones to El Dorado, Tunja's Nivel III hospital, Moniquirá's Nivel II. Current drive-times are still documented values + straight-line distances. **Still open.**
- **Protected-area polygons** (SGC, IGAC, Parques Nacionales SFF Iguaque + páramo, Moniquirá's 13 municipal reserves, Serranía El Peligro) are **still not overlaid**, and exact NSR-10 Aa/Av for El Colegio, Villa de Leyva and Moniquirá is **still unverified**. This is now the highest-value remaining computational check.

---

## 5. Open items

- [ ] Overlay each shortlisted parcel on SFF Iguaque / páramo Iguaque-Merchán / Serranía El Peligro / rondas hídricas (esp. **D — Monte Suárez**) **and** Moniquirá's 13 municipal *Conservación Hídrica* reserves. Still the highest-value legal check.
- [x] ~~Compute real slope from a DEM~~ — done at **area level** (stage 3/10). **Still open per-parcel:** needs coordinates from the agencies, then a clip per boundary. C (La Hoya) and G (Papayal) remain the two that matter.
- [ ] Exact NSR-10 **Aa/Av** for El Colegio, Villa de Leyva **and Moniquirá** (Apéndice A-4 / SGC portal).
- [x] ~~Widen inventory via the blocked portals~~ — done for Moniquirá (22 listings, 5 new group-relevant). **Still open:** Chíquiza/Iguaque, and a direct approach to the agencies (**ATOS Inmobiliaria** holds most Arcabuco/Moniquirá raw land; **Casa 360** has H; **Rubén Quiroga** has I).
- [x] ~~Photo-scrutinise every candidate~~ — done 2026-08-08, all 207 photos across 12 listings, in `docs/candidate_scrutiny.md`.
- [ ] **Ask ATOS for E's matrícula** — the listing text says vereda **San Cristóbal**, the URL says Neval y Cruces. One of them is wrong.
- [ ] **Get a geotechnical + hydrogeological survey on G before any offer.** The photos show limestone **karst** (ravine, outcrop, cave recess): voids under foundations, fast unpredictable groundwater, and septic fields that can reach the aquifer quickly. Budgeted at a 45 M contingency in `masterplan.py`.
- [ ] **Ask Casa 360 for H's existing soil + water studies.** They already exist and answer the buildability question for free — the strongest single reason to look at H first.
- [ ] **Open negotiations below asking on the ATOS six** (G, B, C, D, E, O) — all uploaded 12 Aug 2025 and unsold twelve months later; D offers permuta, H says negotiable.
- [ ] **Chase the two new Moniquirá finds before committing to G:** **N** (40.96 ha at G's price/m², the only parcel above the 9.38 ha UAF → the only lawfully divisible one) and **K** (Neval y Cruces lots with individual matrículas already issued — verify the subdivision is lawful).
- [ ] **Decide the climate fork with the group.** Both flanks are now scored: the wet flank leads four of five weightings, Moniquirá wins services-first, climate-first is a 0.3-point tie. The real trade is **Moniquirá's Nivel II hospital now vs Arcabuco's drought resilience over 30 years**. `scorecard.html` is the tool for that conversation — and it finally contains both sides of the fork.
- [ ] **If Moniquirá:** price a potable-water treatment system into the build budget. Rural supply there is abundant but **not potable** — all four monitored aqueducts are IRCA "Riesgo Alto" with no treatment, including the Papayal one behind G's water claim.
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
