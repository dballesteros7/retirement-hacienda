# Methods log & reproducibility — Hacienda site selection

**Run date:** 2026-07-19 · **Analyst:** Claude (Cowork) · **Mode:** hybrid (real computation where feasible + authoritative published data), phased delivery.

## Environment constraints (shaped the method — disclosed for honesty)
This ran in a sandbox whose **outbound network is allow-listed to PyPI, GitHub (raw + api.github.com), and the WebFetch/WebSearch service.** Direct downloads from S3, OpenTopography, Microsoft Planetary Computer, Overpass, OSRM, Nominatim, WorldClim mirrors, IDEAM/SGC portals and elevation/climate APIs were **blocked** (proxy 403/ProxyError). Consequences:
- **No 30 m DEM was downloadable** → terrain/slope/buildable-land and DEM-derived hydrology were *not* self-computed. Terrain & landslide criteria are scored from published SGC/EOT susceptibility + documented events, and flagged for a field/GIS survey (the brief explicitly anticipates this where DEM resolution/access is limiting).
- **No live routing engine** → drive-times use documented Google-Maps-class values (Phase 0) + computed straight-line distances; isochrones were not generated.
- Climate rasters (WorldClim/CHELSA/NEX-GDDP) unreachable → the water balance runs on **point monthly normals** (IDEAM-anchored, via WebFetch) and projections use **published IDEAM/CMIP6/AR6 ranges** rather than self-extracted grids.
- **Reachable and used:** GEM Global Active Faults DB (GitHub raw), Colombia municipal boundaries (santiblanko/colombia.geojson, GitHub raw), and broad official/secondary text via WebFetch.

## Pipeline (all under `code/`, outputs under `outputs/`)
1. `config.py` — reference points, AOIs, CRS, slope thresholds.
2. `data_inputs.py` — captured numeric inputs (IDEAM monthly normals; projection ranges; NSR-10 Aa/Av; fault coords; DANE codes) — every value cited, low-reliability flagged.
3. `water_balance.py` — Thornthwaite **and** radiation-aware Hargreaves PET; single-bucket soil store (WHC 100 mm); baseline + 2050 + 2085-high + El Niño (P×0.6) scenarios → `water_balance_summary.csv`, `fig_water_balance.png`.
4. `geo_metrics.py` — nearest active-fault distance (GEM DB, projected CRS) + geodesic distances to El Dorado/Bogotá/hospitals → `geo_metrics.csv`.
5. `scorecard.py` + `build_scorecard_html.py` — weighted MCDA (10 criteria × 4 options), 5 weighting scenarios → `scorecard_scores.csv`, `scorecard_data.json`, `scorecard_interactive.html`.
6. `build_map.py` — folium/Leaflet map (boundaries, GEM faults, candidate sectors, shortlisted parcels, reference points; client-side terrain/satellite tiles) → `hacienda_map.html`.
7. `build_report_html.py` — renders `docs/final_report.md` → `outputs/final_report.html` with the water-balance figure embedded.

To re-run: `cd /home/claude/hacienda && python3 code/water_balance.py && python3 code/geo_metrics.py && python3 code/scorecard.py && python3 code/build_scorecard_html.py && python3 code/build_map.py && python3 code/build_report_html.py`.

## Key computed results
- **Water balance (Hargreaves AI):** Arcabuco 1.48 (humid, +609 mm) ≫ El Colegio 0.73 > Villa de Leyva 0.63 > Tunja 0.50 > Sáchica 0.43; valley floors → 12 deficit months under El Niño.
- **Seismic:** nearest cataloged active fault ≥26 km at every site (GEM DB); all NSR-10 intermediate.
- **Accessibility:** El Dorado 24–36 km from Tequendama sites vs 117–141 km from Boyacá sites.
- **Scorecard:** Ricaurte wet NE flank ranks #1 under all five weightings (74.6–77.7).

---

# Revision 2026-08-08 — Moniquirá added, and the sandbox limits lifted

**Run date:** 2026-08-08 · **Mode:** local machine, unrestricted network — several of the blocks above no longer apply.

### Why
The property phase surfaced a warm-flank track (Moniquirá) and the group leaned toward it, but **Moniquirá was never in the analysis**: absent from `NORMALS` (no water balance), absent from `DANE` (no fault/accessibility metrics, no map polygon), absent from the scorecard. The decision was heading for the one option that had never been scored.

### Newly reachable, and used
- **ESA Copernicus GLO-30 DEM** (AWS Open Data) — the download that was blocked in July. New stage `code/slope_analysis.py` clips the two AOIs, reprojects to UTM 18N at 30 m, computes slope and classifies it against the thresholds already in `config.py`. Tile cached under `data/dem/` (gitignored, regenerable).
- **Corpoboyacá POMCA Medio y Bajo Suárez** (Consorcio POMCA 2015) — per-subcatchment mean annual precipitation, mean slope and elevation, plus the IUA / IRH / IVH water-stress indices.
- **Moniquirá PDM 2020-2023** — UAF, hospital level, rural water quality (IRCA), hazards, roads, veredas.
- **NASA POWER climatology API** — used for temperature reconciliation and diurnal range only.
- **Property portals blocked in July** (Metrocuadrado, Properati, Mercado Libre, Ciencuadras) — all reachable; a FincaRaíz sweep of Moniquirá returned 22 lotes/fincas.

### Method decisions worth recording
- **POWER was deliberately NOT used to reset the existing sites' DTR.** Its cells resolve Villa de Leyva and Sáchica to one grid box (identical values) and place El Colegio at 1,790 m against an actual ~1,100 m. Adopting its ~9 °C ranges would have flattened the semi-arid signal this model exists to preserve. Moniquirá takes DTR = 10, the project's existing humid-site convention, corroborated by POWER (9.1) and climate-data.org's own spread (~9.9).
- **climate-data.org magnitudes were NOT used.** Calibration check against the corpus's high-reliability IDEAM normal: its Villa de Leyva page reads **1,767 mm / 13.4 °C vs IDEAM's 997 mm / 16.9 °C** — +77% wet and 3.5 °C cold, because its municipal grid point sits up on the surrounding highlands. Only its monthly *shape* was used, rescaled to official POMCA annual totals.
- **A unit-attribution trap, documented so it is not repeated.** POMCA's subcatchment "Río Moniquirá" (24010214) reads 1,127.2 mm/yr, but has a **mean elevation of 2,560 m** and contains Río Sáchica and Río Cane as child basins — it is the whole Villa de Leyva drainage, not Moniquirá. Its water-stress flags (Moderado IUA, Bajo IRH, highest IVH, "cuidado al seguir otorgando concesiones") likewise apply to that unit, whose two worst micro-basins are named as **Río Sáchica (Muy Alto)** and **Río Cane (Alta)** — i.e. the POMCA independently corroborates *Villa de Leyva's* documented water problem. Moniquirá's own units (24010213/230/231/215) read 1,827.6–1,896.2, mean **1,860 mm/yr**.
- **Independent cross-checks that passed.** Arcabuco's corpus value 1,826 mm vs POMCA's Río Ubazá (its drainage) 1,896 mm → agree to 4%. DEM mean slope vs POMCA's mean-slope-per-unit table: Arcabuco 17.7° vs 16.2°; Moniquirá 12.1° vs 9.9–13.3°.

### Bugs found and fixed
- `DANE['santa_sofia']` was **15690 = Santa María** (280.9 km², Boyacá's Llanos flank) instead of **15696** (74.6 km²); `DANE['sutamarchan']` was **15762 = Sora** (30.4 km²) instead of **15776** (105.6 km²). Both had been pulling the wrong polygon into the map since the first build. Verified against the source `mpio.json`.

### Key computed results (new)
- **Water:** Moniquirá AI **1.31** (humid), 0 deficit months, +439 mm surplus — but **10 deficit months under El Niño vs Arcabuco's 3**. Near-identical rainfall (1,860 vs 1,826 mm); the separation is PET (1,421 vs 1,233 mm) from being 4.8 °C warmer.
- **Slope, in the elevation band where parcels trade:** Moniquirá 77.6% ≤15° / median 10.2° / **4.8% >25°**; Arcabuco 68.1% / 10.5° / **12.5% >25°**. Medians are effectively tied — the difference is that Arcabuco holds **2.6× more steep ground**.
- **Services:** Moniquirá's Nivel I+II regional hospital is the nearest II+ facility for the whole flank, cutting Arcabuco 25.8→19.8 km, Gachantivá 31.9→13.6 km, Santa Sofía 33.2→18.3 km.
- **Scorecard:** with Moniquirá added, the wet flank leads four of five weightings; **Moniquirá wins services-first** (72.9 vs 72.8) and is within 0.3 on climate-first.

### Addendum, same day — full photo scrutiny, cost model, masterplan

- **All 12 candidates' galleries downloaded and reviewed image by image (207 photos).** Gallery URLs are not in the rendered DOM on first load; they sit in the embedded JSON as `cdn2.infocasas.com.uy/repo/img/<hash>_infocdn__<id>-<n>-<ts>png.png` (note the hyphens in the filename — a character class excluding `-` silently returns only the hero image). Listing agency and posting date parse out of the "ingresada por X el DATE" string.
- **Findings that changed conclusions:** E is mis-tagged (text says vereda San Cristóbal, URL says Neval y Cruces); G shows limestone **karst** (ravine, outcrop, cave recess) with consequences for foundations, septic siting and groundwater; H is the best building land, not merely lowest-risk; N is a working panela farm with a trapiche, two houses and own aljibes; M's springs are *veranera* (dry-season reliable); L holds an already-granted water concession; **six candidates are ATOS listings uploaded 12 Aug 2025 and unsold twelve months later**.
- **`code/masterplan.py` (build stage 4/11)** costs a 400 m² programme — one 160 m² casa comunal plus three 80 m² satellites — on parcels H, G and N, with a phased schedule and an indicative site layout honouring the 30 m ronda hídrica, gravity-fed water and septic separation. Karst adds a 45 M contingency on G.
- **2026 unit rates used** (published national/regional figures, not quotes — access date 2026-08-08): finished construction COP 3.1–3.8 M/m² (used 3.5); obra gris 1.85–2.25 M/m²; rural access uplift 2–8% (used 5%); potabilisation plant for a small complex COP 11–15.5 M (used 13) plus ~600 k/yr maintenance; well drilling COP 150–250 k per metre; pozo séptico COP 5–10 M each; solar COP 3.5–5.0 M per kWp plus COP 8–14 M for a 5 kWh lithium battery; Starlink kit COP 1,599,000 and COP 150–250 k/month; buyer-side notarial + registro + beneficencia 2.15–2.5% of price. EUR shown at the **2026 average ~4,300 COP/EUR** and labelled as such — live quotes for EUR/COP disagreed materially across aggregators, so no single "current" rate was adopted.
- **Result:** on H, all-in ≈ COP 2,788 M (≈ COP 929 M per household across three); phases 0–2 put the group on the land, living, at ≈ COP 2,042 M with contingency. Running costs ≈ COP 26 M/yr including a part-time caretaker.

### Still not done
Routing/isochrones (drive-times remain documented values + straight lines); protected-area polygons (SFF Iguaque, páramo, Serranía El Peligro, Moniquirá's 13 municipal reserves) still not overlaid; NSR-10 Aa/Av for El Colegio, Villa de Leyva and Moniquirá still unverified; slope is area-level because listings remain vereda-level.

---

## Source corpus
Full cited source lists (name + URL + access date 2026-07-19) are in: `docs/phase0_verification.md` (seismic, climate, water, landslide, services/heritage) and `docs/phase1_research_synthesis.md` (security, economy/prices, development, legal/co-ownership, climate normals, projections, seismic detail). Primary/official sources preferred: SGC, IDEAM, IGAC, MinSalud REPS, ANT, SNR, Corpoboyacá/CAR Cundinamarca, ANI/INVÍAS, DANE, Mincultura, GEM. No coordinates, prices, or hazard values were fabricated; gaps are marked "unknown / needs field or primary pull."
