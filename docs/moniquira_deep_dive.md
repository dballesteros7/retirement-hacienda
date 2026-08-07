# Moniquirá deep dive (2026-08-08)

Commissioned because the group is leaning to the warm flank. The finding that prompted it: **Moniquirá had never been analysed.** It was absent from `code/data_inputs.py` (no climate normals → no water balance), absent from `DANE` (no fault/accessibility metrics, no map polygon), and absent from the scorecard — even though CLAUDE.md called the scorecard "the tool for that conversation" about the climate fork. The warm side of the fork was not in it.

Everything below is now in the pipeline. Sources are primary where available: Corpoboyacá's POMCA Medio y Bajo Suárez (Consorcio POMCA 2015), the Moniquirá PDM 2020-2023, ESA Copernicus GLO-30, NASA POWER, IDEAM via the existing corpus.

---

## 1. Water — the one place Moniquirá genuinely loses

| | rain | PET | AI | normal year | **El Niño (P×0.60)** |
|---|---|---|---|---|---|
| Arcabuco (2,600 m, 14.0 °C) | 1,826 mm | 1,233 mm | **1.48** humid | 1 deficit month, 609 mm surplus | **137 mm, 3 months** |
| Moniquirá (1,700 m, 18.8 °C) | 1,860 mm | 1,421 mm | **1.31** humid | **0 deficit months**, 439 mm surplus | **305 mm, 10 months** |

**They get the same rain.** What separates them is heat: 4.8 °C warmer ⇒ PET 15% higher ⇒ the soil store empties much faster once rain fails. In a normal year Moniquirá is comfortably humid and needs no defending. In a drought year it goes to 10 deficit months where Arcabuco goes to 3. For a 30-year horizon the drought year is the one that matters — it is the mechanism that produced Villa de Leyva's 2016 rationing.

### A unit-attribution trap, documented so nobody repeats it

POMCA's subcuenca table lists **"Río Moniquirá" (24010214) at 1,127.2 mm/yr**, which looks like a damning number for the warm flank. It is not Moniquirá's rainfall. That subcuenca has a **mean elevation of 2,560 m** and its child micro-basins include **Río Sáchica (2401021408)** and **Río Cane (2401021409)** — it is the whole Villa de Leyva / Sáchica / Ráquira drainage, whose semi-arid highlands (VdL 997 mm, Sáchica 726 mm) drag the area-average down. Using 1,127 mm for Moniquirá would understate it by ~40%.

The units that actually contain the Moniquirá parcels are the low ones around the town: Qda Agua Blanca (24010213) 1,827.6 · Dir Q Agua Blanca–R Moniquirá (24010230) 1,846.5 · Dir R Moniquirá–R Ubazá (24010231) 1,869.6 · Río Ubazá (24010215) 1,896.2 → **mean 1,860 mm/yr**.

Cross-check: Arcabuco drains via **Río Pómeca (2401021501)**, a child of Río Ubazá, whose POMCA value 1,896.2 agrees with the corpus's independently-sourced Arcabuco 1,826 mm to **4%**.

Same trap, opposite direction: POMCA's water-stress flags on "Río Moniquirá" — Moderado IUA (the basin's highest use-conflict), Bajo IRH, highest IVH shortage vulnerability, and "*tener cierto cuidado al seguir otorgando concesiones*" — are flags on **that same Villa de Leyva-inclusive unit**. Its two worst micro-basins are named: **Río Sáchica (IUA Muy Alto)** and **Río Cane (Alta)** — i.e. the POMCA independently confirms the *Villa de Leyva* water problem this project already documented. It is not evidence against Moniquirá. The moderate-aridity flag covers **0.31% of the basin**, in the southern zone of that unit.

### What *is* a real Moniquirá water problem: potability

Moniquirá PDM 2020-2023, from the 2018 Diagnóstico Sanitario — 23 rural supplies, **only 3 with a working treatment plant**; the other 15 unmonitored ones have "*bocatoma, tanque de reserva y sistema de conducción*" and nothing else. Of the 4 aqueducts the Secretaría de Salud does monitor, **all four are IRCA "Riesgo Alto", none has any potabilisation or disinfection**. One of them is:

> *Asociación de Suscriptores acueducto de las Veredas Tierra de Castro, Tierra de González, **Papayal** y Colorado (IRCA Riesgo Alto)*

**Papayal is parcel G's vereda, and "punto de agua veredal" is G's headline water claim.** The urban plant by contrast is IRCA 0.29% (no risk) with 70% municipal coverage. Read: water is *abundant*, not *potable* — budget for treatment, and don't price a rural aqueduct connection as a solved problem.

---

## 2. Terrain — the "flattest land" claim, tested

Copernicus GLO-30 (ESA, 30 m), clipped to each track and restricted to the elevation band where parcels actually trade, so neither flank is scored against its own páramo tops or river gorges.

| in parcel elevation band | ≤15° buildable | median slope | **>25° steep** |
|---|---|---|---|
| Arcabuco / Gachantivá, 2,000–2,750 m | 68.1% | 10.5° | **12.5%** |
| Moniquirá, 1,500–2,000 m | 77.6% | 10.2° | **4.8%** |

The dossier's "gentlest, most genuinely buildable land" is **half right**. Median slopes are effectively identical (10.2° vs 10.5°) — typical ground on both flanks is gentle. The real difference is the tail: **Arcabuco has 2.6× more genuinely steep land**. The "Arcabuco is steep" impression comes from the whole-AOI number (27.4% >25°), which includes the Iguaque massif where nothing is for sale.

So the fork is not flat-vs-steep. It is: **on the highland, parcel selection matters much more**, because you are 2.6× more likely to be shown a difficult site.

Independent check against POMCA's own mean-slope-per-unit table: Arcabuco's Río Pómeca 29.0% (16.2°) vs this DEM's 17.7°; the Moniquirá units 17.4–23.7% (9.9–13.3°) vs this DEM's 12.1°. Two unrelated methods agree.

**Limit:** listings are located at *vereda* level, with no coordinates or cadastral boundaries. This is an area-level characterisation of the two tracks. It cannot tell you how many flat hectares parcel G or C has — that still needs coordinates and a topographic survey.

---

## 3. Services — Moniquirá's strongest card

**Hospital Regional de Moniquirá E.S.E.** offers **Nivel I *and II*** with **118 servicios habilitados**, plus 4 private IPS, clinical labs and rehabilitation centres (PDM 2020-2023). Departmental reporting through 2025-26 describes it consolidating as the referral centre for the Ricaurte province, Boyacá and southern Santander, with growth into higher-complexity surgery (neurosurgery, orthopaedics, joint replacement).

This corrects the original report, which treated Tunja as the only hospital anchor. Recomputed straight-line distance to the nearest Nivel II-or-better facility:

| | was (Tunja III) | now (Moniquirá II) |
|---|---|---|
| Arcabuco | 25.8 km | **19.8 km** |
| Gachantivá | 31.9 km | **13.6 km** |
| Santa Sofía | 33.2 km | **18.3 km** |
| Moniquirá | 44.2 km | **0 km** |

Tunja remains the only **Nivel III** in Boyacá, so it stays the anchor for genuinely complex care. But for a retirement horizon, day-to-day and second-level care sits in Moniquirá — and it improves the *highland* option too.

Access: **Ruta 62** (Tunja–Moniquirá–Santander) is an INVÍAS national corridor, paved, condition "aceptable". Against that, the municipality estimates **only ~40% of its roads are in optimal condition**, across 268 km of tertiary rural road — the last-mile matters.

---

## 4. Hazards — a wider set than the highland's

From the Moniquirá PDM 2020-2023 and POMCA:

- **Wildfire — the one nobody had on the list.** POMCA (p.296): Moniquirá and Barbosa have large areas of **high wildfire hazard, and those zones "rodean casi en su totalidad los cascos urbanos"**. Recurrent in veredas **Colorado Alto, Colorado Medio, Monjas Alto, Tierra de González (sector Reserva El Peligro), La Capilla and Coralina**. Note there is a live listing in vereda Colorado.
- **Flood / avenidas torrenciales.** Río Moniquirá overtops in the urban sector — meanders plus occupied riverbed; critical in La Niña years; 2011 events cited. Flash floods from quebradas in both rural and urban areas.
- **Mass movement.** Present, driven by deforestation and agricultural-frontier expansion.
- **Seismic.** "Zona de sismicidad media" (NSR-10 **INTERMEDIA**); ~45.1 km to the nearest catalogued active fault (Alto del Trigo) vs Arcabuco's ~64.3 km — nearer, but both are comfortable distances. **Exact Aa/Av still UNVERIFIED** (NSR-10 Apéndice A-4). The PDM itself flags widespread non-compliance with NSR-10 in existing local construction — relevant if you buy a built house rather than build.

---

## 5. Legal and tenure

- **UAF = 9.38 ha** (MinAgricultura, via PDM) — essentially the same constraint as Arcabuco's ~9.9 ha. G (9.11 ha), H (8.0 ha) and E (8.5 ha) all sit *below* it. Note 5,354 of Moniquirá's 5,651 rural predios (95%) are already under 10 ha, so sub-UAF parcels exist and trade freely — the UAF blocks *new* subdivision, not the purchase of an existing titled parcel. Same conclusion as before: **one titled parcel, held in a shared SAS**.
- **No national park, no páramo, no heritage overlay** — genuinely simpler than Arcabuco, where SFF Iguaque and the delimited Páramo Iguaque-Merchán gate everything.
- But **13 municipal forest reserves**, every one designated *Conservación Hídrica*, in veredas González, Monjas, Pila Grande, San Vicente and Tierra de González; and the **Serranía El Peligro** reserve edge reaches Tierra de González. Overlay still required — just against a different set.
- **EOT Acuerdo 021 of 2004** — as dated as Arcabuco's. Confirm current zoning at Planeación before assuming residencial-campestre is permitted.
- **Vereda-name collisions are a live trap here.** Moniquirá's own vereda list includes **"La Hoya"** and **"La Capilla"** — names that also exist in Gachantivá and Villa de Leyva, where parcels C and F respectively were placed. Portal mis-tagging has already been caught repeatedly in this project; verify the municipality on the matrícula, not the listing slug.

---

## 6. Where the scorecard lands

With Moniquirá added as its own unit:

| weighting | 1st | 2nd |
|---|---|---|
| Default | Ricaurte 75.9 | **Moniquirá 74.7** |
| Climate-first | Ricaurte 75.0 | **Moniquirá 74.7** |
| Water-first | Ricaurte 77.7 | **Moniquirá 73.7** |
| **Services & airport-first** | **Moniquirá 72.9** | Ricaurte 72.8 |
| Cost-first | Ricaurte 78.0 | **Moniquirá 76.5** |

**The lean is defensible.** Moniquirá is second by a hair almost everywhere, wins on services, and is a dead heat on climate (0.3 points). It loses clearly on exactly one axis — water, and specifically drought resilience. That is the trade to decide consciously, not a reason to drop it.

---

## 7. Inventory refresh (2026-08-08)

All nine July parcels re-checked: **live, with prices unchanged** (A 400M · B 270M · C 230M · D 1,600M · E 750M · G 390M · H 720M).

The portals blocked in the original sandbox — Metrocuadrado, Properati, Mercado Libre, Ciencuadras — are all reachable now. A FincaRaíz sweep of Moniquirá returns **22 lotes/fincas**. New entries relevant to a group hacienda, **none yet photo-scrutinised**:

| # | Vereda / note | Price | Area | COP/m² | Why it matters |
|---|---|---|---|---|---|
| K | Neval y Cruces — **titled lots** | 170 M (5,000 m²) | 5,000 / 5,357 / 6,000 / 7,400 / 8,821 m² | ~34,000 | Each lot has **its own matrícula inmobiliaria**; power, acueducto, gas, quebrada; 4 km from town, 2.8 paved. A different answer to the UAF problem — but verify the subdivision is lawful. |
| L | Alto Cantando | 1,070 M | 7.76 ha | 13,798 | 2,500 guava trees, 3BR house, and an **existing concesión de agua** on the quebrada — the hardest permission to obtain, already in hand. |
| N | (unnamed) | 1,700 M | **40.96 ha** | **4,150** | Same COP/m² as G at 4.5× the size, and **above the 9.38 ha UAF** — the only found parcel that could lawfully be subdivided. |
| M | near vía Togüi | 1,860 M | 18 ha | 10,333 | 350 m² cabaña, 3 nacimientos, own transformer, 15 min to Barbosa. |
| O | Colorado | 320 M | 1.63 ha | 19,671 | Small — and Colorado is a **wildfire-recurrent vereda** per the PDM. |

Also present: a 69 ha finca at 3,600 M (5,217/m²), a luxury turnkey at La Laja (2,600 M), and gated-lot projects at San Cristóbal / Condominio Venecia (~160,000/m²) that are the wrong product for this group.

**N and K are the two worth a look before committing to G.**
