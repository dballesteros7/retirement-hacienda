# Research Brief — Retirement Hacienda Site Selection, Colombian Central Highlands

**Focus municipalities:** Mesitas del Colegio (El Colegio, Cundinamarca) · Villa de Leyva (Boyacá) · Tunja (Boyacá)
**Prepared for:** an autonomous research agent with web access, computer use, and code execution (geospatial + modeling).
**Horizon:** ~30 years. **Use case:** a group of friends (Europe-based owners) buying rural land to build and eventually retire to a hacienda.

---

## 0. How to use this brief

You are grounding a real land-purchase decision. Work in phases, cite every source with URL + access date, and **never invent coordinates, parcels, prices, or hazard values** — mark unknowns explicitly. Save all fetch scripts, data, and analysis code with a manifest so the work is reproducible. Produce mappable, parcel-level outputs, not just prose. Where you disagree with the "established findings" in §3, say so and show the evidence — treat them as hypotheses to validate, not ground truth.

Phased execution:
- **Phase 0 — Verify** the anchor findings in §3 against primary data.
- **Phase 1 — Layer analysis** (workstreams A–J) per municipality.
- **Phase 2 — Ground on real parcels** (workstream K): identify concrete sectors/veredas and, where possible, actual listings with coordinates, and run the layers on them.
- **Phase 3 — Synthesize**: weighted scorecard + sensitivity, maps, per-site fact sheets, ranked recommendation.

---

## 1. Mission

Decide **where** (municipality → vereda/sector → candidate parcel) best satisfies a weighted set of criteria for a 30-year hacienda, and produce the evidence to defend the choice. Rank the three municipalities, but also **surface superior nearby sectors or alternatives** if the terrain/data warrant (e.g., a wetter side of a valley, a lower-landslide sector), staying within the Bogotá-orbit central highlands.

## 2. Requester context (affects weighting)

- Owners are **Europe-based** and will fly in/out → weight **international-airport (El Dorado, BOG) access** and **non-resident ownership logistics** more heavily than a local buyer would.
- **Group purchase among friends** → include a workstream on **co-ownership legal structures** (e.g., SAS, fiducia mercantil, copropiedad) and their tax/succession implications for non-resident co-owners.
- Priorities the requester has emphasized, in rough order: **pleasant climate, water/natural-resource security, geological stability, security/governance, economy/cost, vital services, development trajectory.** Treat these as default weights but run sensitivity analysis (§5).

## 3. Established findings — start here, validate, don't re-derive

All three sit in the calm Cundiboyacense highlands and share two advantages over Colombia's coffee axis: **all are volcano-free**, and **all fall in the *intermediate* seismic band** (Eastern Cordillera crustal faults — Boyacá, Soapaga; plus the deep Boyacá–Santander intermediate seismic source), not the "high" band. They form a **climate gradient**, each with one signature risk:

| Municipality | Elevation (approx) | Climate | Signature risk | Services note |
|---|---|---|---|---|
| Mesitas del Colegio / El Colegio | ~1,000–1,320 m | Warm, 25–28 °C | **Landslides / rockfall** on the Bogotá–La Mesa–Mesitas access corridor (chronic rainy-season closures) | Thin locally; leans on La Mesa (2nd-level hospital) + Bogotá; **closest to El Dorado (~1.5–2 h)** |
| Villa de Leyva | ~2,150 m | Mild, ~17–18 °C, semi-arid, sunny | **Water scarcity** (town supplied by ~2 small sources; documented tourist-season shortages) | No sizeable hospital; relies on Tunja (~45 min) + Bogotá; no nearby commercial airport (BOG ~3.5 h); heritage building rules |
| Tunja | ~2,820 m | **Cold**, ~13 °C | Cold climate; **no commercial airport** | **Best everyday services** (capital, San Rafael hospital, universities); BTS dual carriageway ~1.5 h to Bogotá |

Working hypothesis to test: **base the hacienda near Villa de Leyva for climate/beauty, using Tunja (~45 min) as the services/hospital anchor**; the counter-case is airport frequency favoring Mesitas. Universal gates: build to **NSR-10**; the make-or-break item everywhere is a **secured on-property, legally-concessioned water source**; plus a **slope-stability/geotech** study at Mesitas and **heritage/POT construction limits** at Villa de Leyva.

## 4. Anchor locations (approximate — geocode and verify via IGAC)

- Mesitas del Colegio / El Colegio: ~**4.58° N, 74.44° W**
- Villa de Leyva: ~**5.633° N, 73.533° W**
- Tunja: ~**5.535° N, 73.367° W**
- Reference points to compute distances/isochrones to: **El Dorado Intl (BOG)** in Bogotá; nearest hospitals by complexity level; departmental capitals.

## 5. Decision criteria & scoring model

Build a transparent, weighted multi-criteria model (e.g., weighted sum or AHP). For each candidate location, score these criteria 0–100 with documented rubrics:

1. **Climate now + 2050/2080 comfort** (temp band, seasonality, extreme-heat/rain days) — §E
2. **Water security now + projected** (availability, dry-season deficit, concession feasibility) — §C
3. **Seismic hazard** (PGA/spectral, fault proximity, NSR-10 params) — §D
4. **Landslide/flood hazard** (susceptibility, access-road resilience) — §B
5. **Natural resources** (soil quality/agri capability, solar potential) — §A/C
6. **Security & governance trajectory** (municipal-level) — §G
7. **Economy & cost** (land COP/m², cost of living, taxes) — §H
8. **Vital-services access** (drive-time to hospital by level, to BOG, utilities/fiber) — §F
9. **Development trajectory** (infrastructure pipeline, POT growth) — §I
10. **Legal/tenure feasibility** (title, baldío, POT/zoning, water rights, heritage) — §J

Deliver the model with **default weights (from §2) AND a sensitivity analysis** showing how the ranking shifts under alternative weightings (e.g., "climate-first" vs. "services-first" vs. "cost-first"). Make weights user-adjustable in the final artifact.

---

## 6. Workstreams

For each: **Question → Method → Data sources → Tools → Deliverable.** Run per municipality and per candidate sector.

### A. Terrain & buildable-land analysis
- **Q:** Where is land gentle, stable, and buildable vs. steep/exposed? Elevation bands, slope, aspect, ruggedness.
- **Method:** Derive slope, aspect, hillshade, Topographic Ruggedness Index, and Topographic Wetness Index from a DEM; classify buildable polygons (e.g., slope < 15–20°, stable aspect, off drainage lines); produce elevation profiles across the gradient.
- **Data:** Copernicus GLO-30 DEM, SRTM 30 m, ALOS AW3D30; IGAC cartography.
- **Tools:** Python — `rasterio`, `richdem`/`whitebox`, `numpy`, `geopandas`, `GDAL`; QGIS optional.
- **Deliverable:** Slope/aspect/elevation rasters + buildable-land GeoJSON per sector, with area statistics.

### B. Landslide & mass-movement susceptibility (priority: Mesitas/Tequendama)
- **Q:** Which sectors and access roads are exposed to landslides/rockfall, and how resilient is road access over a year?
- **Method:** Combine slope + lithology + rainfall + land cover into a susceptibility index (heuristic weighted-overlay and/or a simple ML classifier trained on known events); overlay the Bogotá–La Mesa–Mesitas corridor and geolocate documented closure/rockfall points; estimate expected days/year of access disruption.
- **Data:** SGC "amenaza/susceptibilidad por movimientos en masa"; IDEAM precipitation; DEM; UNGRD emergency records; Cundinamarca risk-management reports/news for event geolocation.
- **Tools:** `geopandas`, `rasterio`, `scikit-learn`, `shapely`.
- **Deliverable:** Susceptibility layer + an **access-road resilience assessment** per municipality.

### C. Hydrology & water security (priority: Villa de Leyva)
- **Q:** Is there a viable, legally securable on-property water source? Where is it wet vs. semi-arid? What is the dry-season deficit, now and projected?
- **Method:** Delineate catchments and flow accumulation from the DEM; estimate water availability from precipitation, streamflow, spring density, and groundwater/aquifer potential; compute a monthly water balance (P − PET) and dry-season deficit; distinguish the semi-arid valley floors (e.g., Villa de Leyva/Sáchica) from wetter páramo-fed flanks (e.g., Iguaque, Santa Sofía/Arcabuco side); assess **water-concession feasibility** and existing concessions, plus protected river buffers (rondas hídricas).
- **Data:** IDEAM (DHIME station data, precip, ENSO/ONI), CHIRPS, ERA5-Land, HydroSHEDS/MERIT Hydro; SGC hydrogeology; **Corpoboyacá** (Boyacá) and **CAR Cundinamarca** for concessions/rondas hídricas; the documented Villa de Leyva supply figures (Río Cane ~40 L/s, quebrada La Colorada ~5 L/s, pozo San Roque ~15 L/s) as a baseline to verify.
- **Tools:** `xarray`/`rioxarray`, `richdem`, `pysheds`, `geopandas`, a simple Thornthwaite/Hargreaves PET model.
- **Deliverable:** Water-availability map, dry-season risk index, and per-sector concession-feasibility notes.

### D. Seismic hazard (site-specific)
- **Q:** What are the design-relevant ground-motion parameters and fault distances at each site?
- **Method:** Pull PGA/spectral-acceleration and hazard curves at each coordinate; map active faults (Boyacá, Soapaga; for Cundinamarca also Bituima–Cambao/frontal systems) and compute distances; note the Boyacá–Santander intermediate source; translate to **NSR-10** seismic design parameters (Aa, Av; microzonation if published) and construction cost implications.
- **Data:** SGC national seismic-hazard consultation system (amenazasismica.sgc.gov.co); SGC active-faults database; NSR-10 tables.
- **Tools:** `requests`/API or map-export parsing; `geopandas`.
- **Deliverable:** Per-site seismic parameter table + fault-proximity map.

### E. Climate baseline & projections ("climate models")
- **Q:** What is the climate now at the specific elevations, and how does each site — and each site's signature risk — change by mid- and end-century?
- **Method:** Use **published downscaled CMIP6 ensembles** (do not attempt to run a raw GCM). Extract baseline and future ΔT, ΔP, dry-season length, extreme-heat days, and extreme-rainfall indices for **≥2 scenarios (SSP2-4.5 and SSP5-8.5)** at **mid-century (2041–2060)** and **end-century (2081–2100)**, reporting the **multi-model range**, not a single value. Be **elevation-aware** (lapse-rate adjust to parcel elevations; the gradient spans ~1,000 / 2,150 / 2,820 m). Then reason about each signature risk under warming: Mesitas (more intense rainfall → landslide frequency?), Villa de Leyva (drier → worse water stress? re-run the §C water balance under future precip/PET), Tunja (warming → frost reduction / more comfortable?).
- **Data:** WorldClim v2 + WorldClim CMIP6; CHELSA v2 + CHELSA CMIP6; NASA NEX-GDDP-CMIP6 (via AWS/Microsoft Planetary Computer); IDEAM station records and national climate-change scenarios for validation.
- **Tools:** `xarray`, `xclim`, `rioxarray`, `dask`; Planetary Computer / AWS Open Data access.
- **Deliverable:** Per-site "climate now vs. 2050 vs. 2080" tables (with ranges) + a **climate-resilience verdict per municipality**, explicitly framed around the elevation gradient and each signature risk.

### F. Vital-services accessibility (routing / isochrones)
- **Q:** How long to the nearest hospital *by complexity level*, to El Dorado, and to a major city — and what utilities/fiber exist?
- **Method:** Build isochrones and point-to-point drive-times from candidate sectors; classify hospitals by level (2nd/3rd/4th); assess grid power, water, mobile/fiber coverage.
- **Data:** OpenStreetMap (roads); MinSalud **REPS** registry (facilities + complexity level); airport coordinates; MinTIC coverage data.
- **Tools:** `osmnx` + `networkx`, or a routing engine (OSRM / OpenRouteService / Valhalla); `folium` for maps.
- **Deliverable:** Isochrone maps + a services-access scorecard per sector.

### G. Security & governance (municipal, not departmental)
- **Q:** What is the security level and *trajectory* at municipality level?
- **Method:** Compile recent homicide/extortion/displacement indicators and any armed-group presence; assess 3–5 year trend and near-term outlook (note the post-2026-election governance transition and the struggles of "Total Peace"); ground findings at municipality level and flag uncertainty.
- **Data:** Defensoría del Pueblo (alertas tempranas), Policía Nacional / DANE crime stats, ACLED, InSight Crime, FIP, Indepaz.
- **Deliverable:** Per-municipality security read + trajectory, with sourced caveats.

### H. Economy & cost
- **Q:** What does land actually cost per sector, and what are the carrying costs/taxes?
- **Method:** Benchmark land and finca prices (COP/m²) per vereda from current listings; compile cost-of-living, **predial** (property tax), and the national **wealth-tax** exposure for non-residents; note valorization trends and their drivers.
- **Data:** FincaRaíz, Metrocuadrado, Lamudi, Ciencuadras (listings); DANE; DIAN/tax references; municipal predial schedules.
- **Tools:** Polite scraping/queries (`requests`, `pandas`); respect robots/ToS; record listing URLs + dates.
- **Deliverable:** Price benchmark tables + a 30-year carrying-cost model.

### I. Development trajectory
- **Q:** Which infrastructure/POT changes will reshape access and value over 10–30 years?
- **Method:** Geolocate committed/planned projects with timelines (e.g., BTS Briceño–Tunja–Sogamoso corridor, INVÍAS/ANI road upgrades, any airport/utility works, POT expansion zones) and assess access/value impact per sector.
- **Data:** ANI, INVÍAS, municipal POTs, departmental development plans, credible news.
- **Deliverable:** Project map + per-sector impact assessment.

### J. Legal / tenure / land-use feasibility
- **Q:** Can a clean, buildable, water-securable parcel actually be acquired here — and how?
- **Method:** Document the due-diligence workflow and red-flags: title chain via **SNR/VUR** (Certificado de Tradición y Libertad), **ANT** baldío check, **POT** zoning (residential/agro vs. forest reserve/protected/ronda hídrica), **heritage** construction constraints (Villa de Leyva Pueblo Patrimonio), and the **water-concession** process (CAR / Corpoboyacá). Include the **group co-ownership structures** (SAS / fiducia / copropiedad) and non-resident tax/succession implications. Apply the checklist to any parcels found in §K.
- **Deliverable:** A due-diligence workflow + red-flag checklist; parcel-level flags where applicable. (Frame as process, not legal advice; final steps require a Colombian abogado/notario.)

### K. Ground on real parcels
- **Q:** What concrete, mappable options exist?
- **Method:** Identify **3–6 real candidate sectors/veredas per municipality** (and, where possible, actual listed parcels with coordinates), then run workstreams A–J on them. Cross-check listing claims (water, access, area) against the geospatial layers — flag mismatches.
- **Data:** Real-estate portals (for parcels/coordinates) + all layers above.
- **Deliverable:** A shortlist of concrete, mapped candidates with pros/cons and scores.

---

## 7. Final deliverables

1. **Interactive map** (Leaflet/`folium` HTML) with all layers toggleable and candidate parcels marked.
2. **Weighted scorecard** (with adjustable weights + sensitivity analysis) ranking municipalities and candidate parcels.
3. **Per-site fact sheets** (one page each) covering all 10 criteria with sources.
4. **Ranked recommendation** with explicit reasoning and the top 3–5 grounded parcels.
5. **Data appendix**: all layers as GeoJSON/GeoTIFF/CSV, plus a **methods log** and **reproducible code + data-fetch scripts + manifest**.

## 8. Grounding, citation & reproducibility rules

- Cite every datum with **source + URL + access date**; prefer **primary/official** sources (SGC, IDEAM, IGAC, MinSalud REPS, ANT, SNR, Corpoboyacá/CAR, ANI/INVÍAS, DANE).
- **No fabrication** of coordinates, prices, parcels, or hazard values — mark gaps as "unknown / needs field survey."
- Report **ranges and uncertainty** (especially climate projections); never present a single downscaled value as certainty.
- Keep raw data + code so results can be re-run; log assumptions.

## 9. Acceptance criteria (definition of done)

- [ ] Each of A–K completed for all three municipalities, with ≥3 grounded candidate sectors each.
- [ ] Climate analysis reports ≥2 SSPs × 2 horizons with model ranges, elevation-aware.
- [ ] Water balance quantifies dry-season deficit per sector (now + projected) and concession feasibility.
- [ ] Landslide susceptibility + access-road resilience delivered for Mesitas.
- [ ] Drive-times to hospital-by-level and to El Dorado computed for every candidate sector.
- [ ] Scorecard + sensitivity analysis + interactive map produced.
- [ ] Every quantitative claim traceable to a cited source; all code reproducible.

## 10. Suggested stack & data directory

**Python:** `geopandas`, `rasterio`, `rioxarray`, `xarray`, `xclim`, `richdem`/`whitebox`, `pysheds`, `shapely`, `osmnx`, `networkx`, `folium`, `scikit-learn`, `pandas`, `requests`, `dask`. **Routing:** OSRM / OpenRouteService / Valhalla. **GIS:** QGIS (optional).

**Data portals to locate and use** (find current endpoints):
- Geology/hazard: **Servicio Geológico Colombiano** — seismic hazard (amenazasismica.sgc.gov.co), faults, mass-movement susceptibility.
- Climate/hydrology: **IDEAM** (DHIME, national climate scenarios); **WorldClim** (worldclim.org); **CHELSA** (chelsa-climate.org); **NASA NEX-GDDP-CMIP6** (AWS / Microsoft Planetary Computer); **CHIRPS**; **ERA5-Land**.
- Terrain/cadastre: **IGAC** (Colombia en Mapas, Datos Abiertos); **Copernicus DEM**, **SRTM**, **ALOS AW3D30**; **HydroSHEDS/MERIT Hydro**.
- Services/roads: **OpenStreetMap**; **MinSalud REPS**; **MinTIC** coverage.
- Tenure/legal: **SNR/VUR**, **ANT**, municipal **POT**, **Corpoboyacá**, **CAR Cundinamarca**.
- Security: **Defensoría del Pueblo**, **ACLED**, **InSight Crime**, **FIP**, **Indepaz**, **DANE**.
- Property/economy: **FincaRaíz**, **Metrocuadrado**, **Lamudi**, **Ciencuadras**; **DANE**; **DIAN**.
- National open data hub: **datos.gov.co**.

## 11. Caveats & scope

Much source material is in Spanish; some datasets require registration. DEM resolution (~30 m) limits fine slope work — flag where higher-resolution or field survey is needed. Climate projections carry deep structural uncertainty; present ensembles and ranges. This is **decision-support, not legal, financial, or engineering advice**: title work needs a Colombian lawyer/notary, and any parcel needs on-site geotechnical, hydrogeological, and structural surveys before purchase or construction.
