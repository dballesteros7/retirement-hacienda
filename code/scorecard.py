"""Weighted multi-criteria scorecard (MCDA) + sensitivity, and interactive HTML generator.
Scores (0-100, higher=better) are analyst judgments anchored to the Phase-0/1 cited evidence
and the computed water-balance / seismic / accessibility metrics. Weights are user-adjustable.
"""
import json, pandas as pd

# criterion key, label, default weight, short method note
CRITERIA = [
 ("climate","Climate comfort (now + 2050/80)",16),
 ("water","Water security (now + projected)",16),
 ("seismic","Seismic hazard",8),
 ("landslide","Landslide / flood & access",9),
 ("resources","Natural resources (soil, solar)",6),
 ("security","Security & governance",13),
 ("economy","Economy & cost",11),
 ("services","Vital-services access",10),
 ("development","Development trajectory",6),
 ("legal","Legal / tenure feasibility",5),
]
UNITS = ["Ricaurte wet NE flank","El Colegio / Mesitas","Tunja","Villa de Leyva (town belt)"]

# scores[unit] = {crit: (score, rationale)}
S = {
"Ricaurte wet NE flank": {
 "climate":(72,"~14-16 °C at 2400-2600 m (Arcabuco/Gachantivá/Santa Sofía); mild but cooler & cloudier than the valley floor; comfortable, warms modestly (+1.6/2.4 °C)."),
 "water":(88,"Computed AI 1.48 (humid), ~609 mm surplus, only 1 deficit month; resilient even under an El Niño drought (3 mo). Springs/streams common (listings cite nacimientos)."),
 "seismic":(72,"NSR-10 intermediate; ~52-64 km to nearest cataloged active fault (Alto del Trigo). Build to NSR-10 DMO."),
 "landslide":(70,"Hillier terrain (some mass-movement susceptibility on slopes) but OFF the chronic Bogotá-corridor closure routes; paved Arcabuco link completed 2025."),
 "resources":(78,"Good soils, abundant water, forest; decent solar; productive agro land."),
 "security":(80,"Ricaurte province: decade-low Boyacá homicides, no armed groups; rural setting avoids the tourist-town property crime of Villa de Leyva town."),
 "economy":(86,"Cheapest buildable rural land in the study (≈4,000-18,000 COP/m²); low cost of living; low tourism premium."),
 "services":(55,"Nivel I clinics local; Tunja Nivel III ~40-60 min; El Dorado ~3 h; no airport (Paipa ~1 h, intermittent). Thinner everyday services."),
 "development":(72,"Paved Villa de Leyva–Arcabuco (2025) + Occidente road package improve access; rising rural energy/connectivity."),
 "legal":(68,"No heritage overlay; water concession more feasible (surplus). Must verify UAF/baldío and that the parcel is outside SFF Iguaque buffer / rondas hídricas."),
},
"El Colegio / Mesitas": {
 "climate":(80,"Warm ~23 °C templado (mean, not the 25-28 °C the brief implied); pleasant year-round; warms toward mid-20s — still comfortable, not oppressive."),
 "water":(68,"Computed AI 0.73 (sub-humid) but high PET from warmth → 9 deficit months; many parcels cite streams/springs on the humid Tequendama slope. Own source still needed."),
 "seismic":(68,"NSR-10 intermediate; nearer active faults (~26-35 km: Usme/Honda) than the Boyacá sites, still comfortable distance."),
 "landslide":(35,"HIGH SGC mass-movement susceptibility; chronic rainy-season closures on both Bogotá corridors; fault-controlled 2008 disaster in-municipality. The signature risk."),
 "resources":(78,"Fertile warm-climate land (coffee/fruit), high productivity, humid."),
 "security":(68,"Cundinamarca = safest department, but peri-Bogotá organized-crime spillover: Aug-2025 Mesitas massacre, documented finca theft. On-site security advised."),
 "economy":(63,"Mid land prices (≈49,000-130,000 COP/m²), deep/liquid market; Tena & San Antonio cheaper (7,000-38,000). Moderate carrying cost."),
 "services":(78,"La Mesa Nivel II ~15 min; Bogotá Nivel III/IV ~1.5 h; El Dorado ~1 h 47 (best airport access of all options)."),
 "development":(63,"Bogotá-weekender demand + condominio zoning, but the flagship road program is defensive stabilization of a landslide corridor; no transformational upgrade."),
 "legal":(72,"Suburban/condominio zoning already exists (easier to build); no heritage overlay; water concession via CAR Cundinamarca. 1999 PBOT is dated."),
},
"Tunja": {
 "climate":(60,"Cold ~13 °C altiplano; less 'pleasant' for a warm-climate retirement; warming (+1.6/2.4 °C) mildly improves comfort / reduces frost."),
 "water":(52,"Computed AI 0.50 (semi-arid) — the driest town (≈653 mm/yr); 12 deficit months; a rural parcel needs a secured source (city itself is reservoir-fed)."),
 "seismic":(65,"NSR-10 intermediate but at the top of the band (Aa 0.20); Boyacá fault passes ~10 km (mapped, not cataloged-active); slightly higher design demand."),
 "landslide":(82,"Altiplano — low landslide/flood exposure; resilient access on the BTS corridor."),
 "resources":(68,"Altiplano agriculture, high solar; colder growing conditions."),
 "security":(86,"Safest option: 4 homicides in 2025 (lowest of any Colombian capital), no armed-group presence, institutional/university city."),
 "economy":(60,"Mid prices; thin, mis-tagged rural inventory; lower tourism premium than Villa de Leyva."),
 "services":(72,"Nivel III hospital in-city, universities, full capital services — best everyday services; but El Dorado ~2.5-3 h and no commercial airport."),
 "development":(83,"Strongest pipeline: mature Bogotá–Tunja doble calzada + new Tunja–Duitama (opening 2026-27) + Paipa air service ~30 min to Bogotá."),
 "legal":(74,"Straightforward capital-city tenure/permitting; standard rural due diligence; no heritage overlay."),
},
"Villa de Leyva (town belt)": {
 "climate":(85,"Mild ~17-18 °C, sunny, semi-arid — the most-cited 'ideal' Andean climate; stays pleasant under warming. Best climate/beauty of all options."),
 "water":(45,"Computed AI 0.63 (dry-subhumid), 10 deficit months; severe El Niño vulnerability (12 mo, ~990 mm deficit) — the driver of 2016 rationing. Thin municipal supply; own source essential and harder to secure."),
 "seismic":(72,"NSR-10 intermediate; ~63 km to nearest cataloged active fault. Standard DMO design."),
 "landslide":(80,"Flat valley floor — low landslide/flood exposure."),
 "resources":(70,"Very sunny (high solar) but semi-arid soils; scenic but drier land."),
 "security":(72,"Decade-low department homicides, but persistent tourist-town property crime, a Feb-2025 targeted robbery-murder of a foreign resident, and a 2026 construction-licensing corruption case (permit-process risk)."),
 "economy":(45,"Most expensive land (median ≈110,000 COP/m², to 390,000 near town); highest cost of living; rising catastral/predial base."),
 "services":(60,"Nivel I hospital local; Tunja Nivel III ~50 min; El Dorado ~3 h; no airport (Paipa ~1 h intermittent). Good town amenities/tourism services."),
 "development":(74,"Tourism-driven value growth + improved access, but water scarcity caps buildability and a pending PBOT revision adds entitlement timing risk."),
 "legal":(55,"Heritage PEMP + BIC constraints (materials/heights/colours) near the historic core & influence zone; SFF Iguaque buffer proximity; over-subscribed water → concession harder; licensing-integrity flag."),
},
}

WEIGHT_PRESETS = {
 "Default (brief priority)": {k:w for k,_,w in CRITERIA},
 "Climate-first": {"climate":30,"water":15,"seismic":6,"landslide":8,"resources":4,"security":11,"economy":6,"services":8,"development":5,"legal":7},
 "Water-first": {"climate":13,"water":30,"seismic":6,"landslide":9,"resources":5,"security":11,"economy":7,"services":6,"development":4,"legal":9},
 "Services & airport-first": {"climate":11,"water":12,"seismic":6,"landslide":8,"resources":3,"security":12,"economy":8,"services":24,"development":8,"legal":8},
 "Cost-first": {"climate":12,"water":15,"seismic":5,"landslide":8,"resources":3,"security":10,"economy":28,"services":7,"development":5,"legal":7},
}

def totals(weights):
    wsum=sum(weights.values())
    out={}
    for u in UNITS:
        out[u]=round(sum(S[u][k][0]*weights[k] for k,_,_ in CRITERIA)/wsum,1)
    return dict(sorted(out.items(), key=lambda kv:-kv[1]))

print("=== Rankings under each weighting scenario ===")
for name,w in WEIGHT_PRESETS.items():
    t=totals(w)
    print(f"\n{name}:")
    for i,(u,v) in enumerate(t.items(),1): print(f"  {i}. {u:28s} {v}")

# CSV of scores
rows=[]
for u in UNITS:
    r={"unit":u}; r.update({k:S[u][k][0] for k,_,_ in CRITERIA}); r["TOTAL_default"]=totals(WEIGHT_PRESETS["Default (brief priority)"])[u]
    rows.append(r)
pd.DataFrame(rows).to_csv("outputs/scorecard_scores.csv",index=False)

# ---- interactive HTML ----
payload={"criteria":[{"key":k,"label":l,"w":w} for k,l,w in CRITERIA],
         "units":UNITS,
         "scores":{u:{k:{"v":S[u][k][0],"r":S[u][k][1]} for k,_,_ in CRITERIA} for u in UNITS},
         "presets":WEIGHT_PRESETS}
open("outputs/scorecard_data.json","w").write(json.dumps(payload,ensure_ascii=False))
print("\nSaved outputs/scorecard_scores.csv + scorecard_data.json")
