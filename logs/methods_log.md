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

## Source corpus
Full cited source lists (name + URL + access date 2026-07-19) are in: `docs/phase0_verification.md` (seismic, climate, water, landslide, services/heritage) and `docs/phase1_research_synthesis.md` (security, economy/prices, development, legal/co-ownership, climate normals, projections, seismic detail). Primary/official sources preferred: SGC, IDEAM, IGAC, MinSalud REPS, ANT, SNR, Corpoboyacá/CAR Cundinamarca, ANI/INVÍAS, DANE, Mincultura, GEM. No coordinates, prices, or hazard values were fabricated; gaps are marked "unknown / needs field or primary pull."
