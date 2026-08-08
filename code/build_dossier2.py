"""Arcabuco + Moniquira property dossier v3 (2026-08-08).

This page answers ONE question: which parcel. The regional argument - which flank, and why - lives
in the report (docs/final_report.md, section 5); the build costs and community layout live on the
overview (code/masterplan.py + build_overview.py). Keeping those separate is deliberate: the three
pages had drifted into re-arguing each other. Prose sources: docs/candidate_scrutiny.md and
docs/arcabuco_scrutiny.md. Villa de Leyva (F) and Santa Sofia (I) are dropped from the tracks.
"""
import base64
S = "outputs/shots"


def img(fn):
    return "data:image/jpeg;base64," + base64.b64encode(open(f"{S}/{fn}", "rb").read()).decode()


I = {
 "A": img("screenshot-1784473887655-0.jpg"), "Clead": img("screenshot-1784473887656-1.jpg"),
 "Cspring": img("screenshot-1784473958903-2.jpg"), "B": img("screenshot-1784474148823-6.jpg"),
 "topo_regio": img("screenshot-1784474065523-4.jpg"),
 "D": img("screenshot-1784475339222-0.jpg"), "E": img("screenshot-1784475378771-3.jpg"),
 "G": img("screenshot-1784475444227-5.jpg"), "H": img("screenshot-1784475471382-6.jpg"),
 "topo_moni": img("screenshot-1784475532278-8.jpg"),
}


def card(cls, badge, badgecls, title, meta, url, imgs, paras, flag):
    ims = "".join(f'<img src="{s}" alt="">' for s in imgs)
    if len(imgs) > 1:
        ims = f'<div class="imgrow">{ims}</div>'
    ps = "".join(f"<p>{p}</p>" for p in paras)
    return f"""<div class="cand {cls}"><div class="ch"><h3>{title}</h3><span class="badge {badgecls}">{badge}</span></div>
    <div class="meta">{meta} · <a href="{url}" target="_blank">listing ↗</a></div>{ims}{ps}
    <p class="flag"><b>Verify on the ground:</b> {flag}</p></div>"""


WARM = (
card("top warm", "most buildable value", "gold", "G · Moniquirá — Papayal (best buildable value)",
 "9.11 ha · <b>COP 390 M</b> (~4,300/m²) · no house · ~1,700 m · <i>ATOS Inmobiliaria</i>",
 "https://www.fincaraiz.com.co/finca-en-venta-en-papayal-moniquira/192742687", [I["G"]],
 ["<b>Photos (all 10 reviewed):</b> a broad <b>flat valley-bottom pasture</b> and gentle silvopasture with mature shade trees and grazing cattle — genuinely usable ground. The <b>quebrada is real</b>: one frame shows a clear stream running over cobbles in deep shade, the kind that looks perennial.",
  "<b>But two frames change the picture.</b> One shows a <b>deep ravine with near-vertical rock walls</b>, another an <b>exposed limestone outcrop with a cave recess</b>, and a third a steep forested cone rising straight off the pasture. This is <b>karst</b>, and it means possible voids under foundations, groundwater moving fast and unpredictably through fissures, and septic fields that can reach the aquifer far quicker than in clay. Against that, \"el 90% del terreno es aprovechable\" is a seller's number — a real share is gorge and steep forest.",
  "<b>Leverage:</b> listed by ATOS on 12 Aug 2025 — <b>twelve months unsold</b>. Re-checked 8 Aug 2026: live, price unchanged at COP 390 M."],
 "<b>the water and the ground, in that order.</b> G's headline claim is \"punto de agua veredal\" — and the Papayal vereda aqueduct is named in the Moniquirá PDM as <b>IRCA \"Riesgo Alto\" with no treatment and no disinfection</b>. Then a <b>geotechnical and hydrogeological survey before any offer</b>, because of the karst — not after. Then the flat impression across the full 9 ha, access, title/UAF (9.38 ha).")
+
card("top warm", "lowest diligence risk", "gold", "H · Moniquirá — lote (geotech already done)",
 "8.0 ha · <b>COP 720 M</b> · no house · ~1,700 m · <i>Casa 360</i>",
 "https://www.fincaraiz.com.co/lote-en-venta-en-moniquira/193363278", [I["H"]],
 ["<b>Photos (all 15 reviewed) — the best building land in the whole search.</b> Open, closely-grazed, gently-sloping ridgetop pasture, fenced post-and-wire, scattered mature spreading trees hung with Spanish moss and bromeliads, and a long panorama over the valley to distant blue ranges. <b>No rock outcrops, no ravines, no scrub</b> — several frames show parkland-like ground you could build on without earthworks.",
  "<b>De-risked:</b> soil + water studies already done and handed over, fully fenced, 15 potreros, aljibe + pozo, 5 km access of which 3 km paved. The listing's \"2 m²\" area is a portal data error (it is ~8 ha). Listing states <i>libre de hipotecas</i> and <i>negociable</i>. Re-checked 8 Aug 2026: live at COP 720 M.",
  "<b>That geotechnical study is the single most valuable document in this set</b> — it is exactly what every other parcel would have to pay for, and it is what decides whether a parcel is buildable at all."],
 "read the existing geotechnical and water studies before anything else — they are the reason to pay the premium over G. Then confirm area/boundaries, the last 2 km unpaved, title/UAF.")
+
card("warm", "⚠ wrong vereda on the portal", "", "E · Moniquirá — <s>Neval y Cruces</s> <b>San Cristóbal</b>",
 "8.5 ha · <b>COP 750 M</b> · no house · ~1,700 m",
 "https://www.fincaraiz.com.co/finca-en-venta-en-neval-y-cruces-moniquira/192899845", [I["E"]],
 ["<b>⚠ Mis-tagged.</b> The URL — and every earlier version of this dossier — places E in vereda <b>Neval y Cruces</b>. The listing text says <b>\"vereda San Cristóbal\"</b>. Those are different veredas. This is exactly the portal mis-tagging caught repeatedly in this search: <b>verify on the matrícula, never the slug</b>.",
  "<b>Photos:</b> a genuinely spectacular 20–30 m waterfall dropping through mossy cloud forest. But the listing text claims only <i>\"quebrada lindante\"</i>, pozos, nacederos and an acueducto point — <b>no waterfall is claimed in words</b>, so whether that fall is on-title or a neighbouring landmark is an open question. The ground around it is steep and forested.",
  "<b>Demoted</b> — wrong vereda on record, a headline photo the text does not substantiate, and steep ground. Ask ATOS for the matrícula before spending more time. If Neval y Cruces itself is the attraction, <b>K</b> below offers individually-titled lots there."],
 "which vereda it is actually in; whether the waterfall is on-title; net buildable area vs steep forest; and any ronda hídrica.")
)

COOL = (
card("top", "best turnkey balance", "", "A · Arcabuco — Peñas Blancas (with house)",
 "2.97 ha · <b>COP 400 M</b> · house 128 m² · ~2,570 m",
 "https://www.fincaraiz.com.co/finca-en-venta-en-arcabuco/193601271", [I["A"]],
 ["<b>Photos:</b> rolling green pasture with real 360° valley-and-forest panoramas and a modest older teal farmhouse.",
  "<b>Terrain:</b> undulating, not flat — site the house on a chosen bench with some earthworks. <b>Water/access:</b> quebrada + potable tank; 1.3 km off the paved highway with power, septic and gas in — the best-serviced of the cheap tier. Re-checked 8 Aug 2026: live at COP 400 M."],
 "slope for a real pad; water flow + Corpoboyacá concession; that the upper edge is clear of the SFF Iguaque / páramo boundary; the last stretch of road; Peñas Blancas soils are flagged clay/poor.")
+
card("top", "best value & wettest", "green", "C · Gachantivá — La Hoya (blank land)",
 "5.45 ha · <b>COP 230 M</b> (<b>cheapest/m²</b>) · no house · ~2,100 m",
 "https://www.fincaraiz.com.co/finca-en-venta-en-la-hoya-gachantiva/192743485", [I["Clead"], I["Cspring"]],
 ["<b>Photos:</b> the lushest, wettest parcel — bright green pasture, mature trees, dense native fern/cloud-forest scrub and a visible spring in the ferns.",
  "<b>Terrain:</b> rolling-to-steep in a basin (\"La Hoya\"); much of the 5.45 ha is dense scrub and forest, so the genuinely flat clear area looks limited. This is the parcel the DEM cannot settle for you — Arcabuco's band holds 2.6× more steep ground than Moniquirá's, and a basin is where it concentrates."],
 "<b>how much is actually buildable</b> (clear/gentle vs steep/forest); drainage at the basin low point; access-road grade; water rights; any strip inside a ronda hídrica. <b>Also confirm the municipality</b> — \"La Hoya\" is a vereda name in Moniquirá too, and portal mis-tagging has already been caught in this search.")
+
card("top", "cheapest highland, strong water", "", "B · Arcabuco — Peñas Blancas (blank land)",
 "2.43 ha · <b>COP 270 M</b> · no house · ~2,570 m · <i>neighbours A</i>",
 "https://www.fincaraiz.com.co/finca-en-venta-en-arcabuco/192742902", [I["B"]],
 ["<b>Photos:</b> a signed Peñas Blancas parcel actively cultivated with maize on a sloped hillside, a fern-filled spring, dry-season pasture, rough access track.",
  "<b>Terrain:</b> visibly steeper and rougher than neighbour A — a blank canvas, but you are buying slope plus a farm track. <b>Water:</b> the best-claimed of the cheap tier (nacimiento + quebrada + reservorios). Re-checked 8 Aug 2026: live at COP 270 M."],
 "slope for a pad; access-road condition and legal access; water rights and flow; distance to EBSA power; title/UAF.")
+
card("", "comfortable house · premium", "", "D · Arcabuco — Monte Suárez (finished home)",
 "8.93 ha · <b>COP 1,600 M</b> · house 240 m² + caretaker · ~2,650 m",
 "https://www.fincaraiz.com.co/finca-en-venta-en-monte-suarez-arcabuco/192742895", [I["D"]],
 ["<b>Photos:</b> the most finished, comfortable house of the set — two-storey stone-and-white home, terracotta roof, wood-beamed ceilings, wood stove, furnished throughout. Waterfall and spring claimed.",
  "<b>The catch is unchanged:</b> Monte Suárez's head touches SFF Iguaque. The forest-and-waterfall charm sits near the protected edge, and the price is a large premium over everything else here."],
 "<b>first</b>, that the parcel <i>and its water</i> are entirely OUTSIDE SFF Iguaque and the delimited páramo; only then the structural survey, water rights and access. This is the one parcel where a boundary answer can kill the deal outright.")
)

NEW_ROWS = [
 ("K", "Neval y Cruces — <b>individually titled lots</b>", "170 M<br><span class=sm>(5,000 m²)</span>",
  "5,000 / 5,357 / 6,000 / 7,400 / 8,821 m²", "~34,000",
  "Each lot carries <b>its own matrícula inmobiliaria</b>; power, acueducto, gas and quebrada; 4 km from town, 2.8 paved; the 8,821 m² has its own nacedero. A different answer to the UAF problem — <i>if</i> the subdivision is lawful.",
  "https://www.fincaraiz.com.co/lote-en-venta-en-neval-y-cruces-moniquira/193893121"),
 ("N", "(unnamed)", "1,700 M", "<b>40.96 ha</b>", "<b>4,150</b>",
  "The same COP/m² as G at 4.5× the size, and the only parcel found <b>above the 9.38 ha UAF</b> — so the only one that could lawfully be subdivided rather than held whole in an SAS.",
  "https://www.fincaraiz.com.co/finca-en-venta-en-moniquira/192463144"),
 ("L", "Alto Cantando", "1,070 M", "7.76 ha", "13,798",
  "2,500 guava trees and a 3BR house, but the real point is an <b>existing concesión de agua</b> on the quebrada — the single hardest permission to obtain, already granted.",
  "https://www.fincaraiz.com.co/finca-en-venta-en-moniquira/193445858"),
 ("M", "near vía Togüi", "1,860 M", "18 ha", "10,333",
  "350 m² cabaña, 3 nacimientos propios, 2 acueducto points, own transformer, 15 potreros; 5 km from Moniquirá, 15 min from Barbosa.",
  "https://www.fincaraiz.com.co/finca-en-venta-en-moniquira/193434440"),
 ("O", "Colorado", "320 M", "1.63 ha", "19,671",
  "Small for a group — and Colorado is named in the PDM as a <b>wildfire-recurrent vereda</b>.",
  "https://www.fincaraiz.com.co/finca-en-venta-en-colorado-moniquira/192743320"),
]
NEW_TBL = "".join(
    f"<tr><td><b>{k}</b></td><td>{v}</td><td>{p}</td><td>{a}</td><td>{c}</td><td>{w} "
    f"<a href='{u}' target='_blank'>↗</a></td></tr>" for k, v, p, a, c, w, u in NEW_ROWS)

CSS = """
:root{--cream:#faf7f2;--ink:#2b2620;--mut:#6b6157;--line:#e6ded2;--terra:#b5613a;--sage:#5b7a5b;--gold:#b8860b;--card:#fff}
*{box-sizing:border-box}body{margin:0;background:var(--cream);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;line-height:1.6}
.wrap{max-width:960px;margin:0 auto;padding:40px 22px 80px;background:var(--card)}
h1{font-family:Georgia,serif;font-size:30px;margin:.1em 0}.sub{color:var(--mut);font-size:15.5px;margin-bottom:6px}
h2{font-family:Georgia,serif;font-size:22px;margin:34px 0 8px;border-bottom:2px solid var(--line);padding-bottom:5px}
h3{font-size:18px;margin:0}h4{font-size:16px;margin:20px 0 4px;font-family:Georgia,serif}p{font-size:15px}
.callout{background:var(--cream);border:1px solid var(--line);border-left:4px solid var(--sage);border-radius:8px;padding:14px 16px;margin:14px 0;font-size:14.5px}
.callout.warn{border-left-color:var(--terra)}.callout.fork{border-left-color:var(--gold);background:#fbf7ee}
.callout.key{border-left-color:#2c5f4f;background:#f2f7f3}
.cand{border:1px solid var(--line);border-radius:12px;padding:18px;margin:16px 0}
.cand.top{border:2px solid var(--sage)}.cand.top.warm,.cand.warm.top{border:2px solid var(--gold)}
.ch{display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:6px}
.badge{font-size:11.5px;background:#efe7db;color:#7a5a3a;border-radius:14px;padding:3px 10px;white-space:nowrap}
.badge.green{background:#e4efe2;color:#3f6b43}.badge.gold{background:#f3e9cf;color:#8a6d15}
.meta{color:var(--mut);font-size:13.5px;margin:5px 0 12px}
.cand img{width:100%;border:1px solid var(--line);border-radius:8px;margin:6px 0}
.imgrow{display:grid;grid-template-columns:1fr 1fr;gap:8px}@media(max-width:640px){.imgrow{grid-template-columns:1fr}}
.cand p{margin:8px 0}.flag{background:#fbf3ec;border:1px solid #f0dcc9;border-radius:8px;padding:9px 12px;font-size:14px}
.terr img,.fig img{width:100%;border:1px solid var(--line);border-radius:8px;margin:8px 0}
.tw{overflow-x:auto;margin:12px 0}
table{border-collapse:collapse;width:100%;font-size:13.5px;min-width:560px}
th,td{border:1px solid var(--line);padding:7px 9px;text-align:left;vertical-align:top}
th{background:var(--cream);font-weight:700}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
tr.win td{background:#f2f7f3}
.sm{font-size:12px;color:var(--mut)}
ol,ul{padding-left:1.25em}li{margin:.35em 0;font-size:14.5px}a{color:var(--sage)}
.foot{margin-top:34px;padding-top:16px;border-top:1px solid var(--line);color:var(--mut);font-size:13px}
"""

HTML = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Arcabuco + Moniquirá — property dossier (v3, Moniquirá deep dive)</title><style>{CSS}</style></head><body><div class="wrap">
<h1>Arcabuco + Moniquirá — property dossier</h1>
<div class="sub">v3 · 8 August 2026. Rescoped to the two tracks still live, with the <b>Moniquirá deep dive</b> the group asked for. Villa de Leyva (F) and Santa Sofía (I) are dropped — F sits on the water-constrained side, I is 0.72 ha and too small for a group.</div>

<div class="callout warn"><b>New in this pass (8 Aug 2026): every candidate's full gallery reviewed — 207 photos across 12 listings.</b> What it changed:
<br>• <b>E is in the wrong vereda</b> on the portal — the text says San Cristóbal, the URL says Neval y Cruces.
<br>• <b>G sits on karst</b> — visible limestone outcrops, a cave recess and a rock ravine. Foundations, septic siting and groundwater all need specialist input.
<br>• <b>H is clearly the best building land</b>, not just the lowest-risk: clean, open, gently-sloping ground with nothing to clear.
<br>• <b>N is a going concern</b>, not a bare parcel — a working trapiche, two houses, own aljibes, good soils, and the only candidate above the UAF.
<br>• <b>M's springs are <i>veranera</i></b> (dry-season reliable) — the direct antidote to the flank's one measured weakness. <b>L comes with a water concession already granted.</b>
<br>• <b>Six candidates have sat unsold with one agency (ATOS) for twelve months</b>, and two listings volunteer that they are negotiable or open to a swap. Nobody should pay asking.
<br>Full per-parcel notes: <code>docs/candidate_scrutiny.md</code>. Build costs and the community masterplan: see the <a href="index.html">overview</a>.</div>

<div class="callout key"><b>Why this revision exists.</b> Moniquirá had <i>never been analysed</i>. It was missing from the climate inputs (so it had no water balance), missing from the municipal-code list (so no fault, accessibility or map data), and missing from the scorecard — the very tool the brief called "the tool for that conversation" about the climate fork. The group was leaning toward the one option the analysis had never covered. It is now fully in the pipeline, and the numbers below are its first.</div>

<div class="callout fork"><b>The fork, restated with real numbers.</b> The old framing was "cool-but-steep vs warm-and-flat". Measured, that is only half right:
<br>• <b>Terrain — nearly a tie.</b> In the elevation band where parcels actually trade, median slope is <b>10.2° in Moniquirá vs 10.5° in Arcabuco</b>. What differs is the tail: Arcabuco has <b>2.6× more genuinely steep land</b> (12.5% vs 4.8% above 25°). So it is not flat-vs-steep — it is that <b>on the highland, picking the right parcel matters far more</b>.
<br>• <b>Water — the real difference, and it favours Arcabuco.</b> They get <i>the same rain</i> (1,860 vs 1,826 mm). But Moniquirá is 4.8 °C warmer, so its evaporative demand is 15% higher, and in an El Niño drought it goes to <b>10 deficit months against Arcabuco's 3</b>.
<br>• <b>Services — the real difference, and it favours Moniquirá.</b> A <b>Nivel I+II regional hospital in town</b>, which also happens to be the nearest second-level care for the highland veredas.</div>

<h2>What the regional analysis concluded</h2>
<div class="callout key">This dossier is about <b>which parcel</b>. The question of <b>which flank</b> — the
climate, the water balance, the terrain, the services, the hazards and the legal overlays — is
worked through in full in the <a href="report.html">report, §5</a>. The short version, because it
frames every parcel below:
<br>• <b>Same rain, different thirst.</b> Both flanks get essentially the same rainfall (Moniquirá
1,860 mm, Arcabuco 1,826 mm). Moniquirá is 4.8 °C warmer, so in a normal year it is comfortably
humid with <i>zero</i> deficit months — but in an El Niño drought it goes to <b>10 deficit months
against Arcabuco's 3</b>. Drought resilience is the one axis that separates them.
<br>• <b>Terrain is nearly a tie.</b> Median slope where parcels actually trade is 10.2° on the warm
flank against 10.5° in the highland. What differs is the tail: <b>Arcabuco holds 2.6× more land
above 25°</b>. So it is not flat-versus-steep — it is that <b>on the highland, picking the right
parcel matters much more</b>. That is the single most important thing to carry into the cards below.
<br>• <b>Moniquirá has the hospital</b> (Nivel I+II, 118 services) — and it is the nearest
second-level care for the Arcabuco veredas too.
<br>• <b>Water is abundant but not potable</b> anywhere on the warm flank: of 23 rural supplies only
three have working treatment. Budget a plant (COP 11–15.5 M) on any Moniquirá parcel.
<br>• <b>Both municipalities have a ~9.4 ha subdivision floor (UAF)</b>, so unless you buy above it
you are buying one titled parcel held jointly in an SAS.
<br>What it would cost to build on the shortlist, and the community layout, are on the
<a href="index.html">overview</a>.</div>

<h2>Track 1 — Moniquirá, the warm flank (~1,700 m, ~19 °C)</h2>
{WARM}

<h4>New since the July sweep — not yet photo-scrutinised</h4>
<p>The portals blocked in the original sandbox (Metrocuadrado, Properati, Mercado Libre, Ciencuadras) are all reachable now; a FincaRaíz sweep returns 22 lotes/fincas in Moniquirá. The entries relevant to a group hacienda:</p>
<div class="tw"><table>
<tr><th>#</th><th>Vereda / note</th><th>Price</th><th>Area</th><th class="num">COP/m²</th><th>Why it matters</th></tr>
{NEW_TBL}
</table></div>
<p><b>N and K deserve a look before you commit to G.</b> N is the only parcel found above the UAF, so the only one that could lawfully be divided; K is the only route into Neval y Cruces with individual titles already issued.</p>

<h2>Track 2 — Arcabuco &amp; Gachantivá, the cool highland (~2,100–2,650 m, ~14 °C)</h2>
{COOL}

<h2>The terrain, from the topographic maps</h2>
<div class="terr">
<img src="{I['topo_regio']}" alt="Topographic map of the highland cluster">
<p class="sub">The steep green block in the centre is the protected <b>Iguaque massif (3,825 m)</b>. Gachantivá (NW) and Arcabuco (N) sit clear of it — and this is the terrain that produces Arcabuco's steep tail, even though the parcels themselves sit lower and gentler.</p>
<img src="{I['topo_moni']}" alt="Topographic map of the warm Moniquirá flank">
<p class="sub"><b>The warm flank:</b> north down Ruta 62, Arcabuco descends to <b>Moniquirá</b> — lower, warmer, greener, more dissected subtropical hill country. E, G and H sit here; steeper along the river cuts (the waterfalls at Neval y Cruces), gentler on the ridges and at Papayal.</p>
</div>

<h2>Recommended shortlist for ground experts</h2>
<p><b>If the group confirms the warm flank (current lean):</b></p>
<ol>
<li><b>G — Papayal (COP 390 M, 9.11 ha)</b> — still the best value per buildable hectare anywhere in the search. Go in knowing the vereda aqueduct is IRCA "Riesgo Alto" and price your own treatment.</li>
<li><b>H — geotech lote (COP 720 M, 8 ha)</b> — the lowest-diligence-risk parcel found: soil and water studies done and handed over, fenced, mostly paved access, seller says negotiable.</li>
<li><b>N — 40.96 ha (COP 1,700 M)</b> — <i>new.</i> Same price per m² as G, 4.5× the land, and the only parcel above the 9.38 ha UAF, so the only one you could lawfully divide among the group rather than hold whole in an SAS.</li>
<li><i>Also worth a call:</i> <b>K</b> (Neval y Cruces, individually titled lots) and <b>L</b> (Alto Cantando, with a water concession already granted).</li>
</ol>
<p><b>If the group wants maximum drought security instead:</b></p>
<ol>
<li><b>A — Peñas Blancas with house (COP 400 M)</b> — best all-round highland balance, and the wet flank's 3-deficit-month drought profile is the most resilient measured.</li>
<li><b>C — Gachantivá / La Hoya (COP 230 M)</b> — best value and most beautiful, but it is exactly the basin setting where Arcabuco's steep tail concentrates. Resolve buildable area on site.</li>
<li><b>B — Peñas Blancas blank (COP 270 M)</b> — cheapest way into A's vereda, with a visible spring.</li>
</ol>

<h2>What every site visit must confirm</h2>
<ul>
<li><b>Water, legally and chemically.</b> A Corpoboyacá <i>concesión de aguas</i> plus an IRCA test — and in Moniquirá assume the rural supply is untreated until proven otherwise. Abundant rain is not a legal, potable, on-parcel source.</li>
<li><b>Which subcatchment the parcel drains to.</b> It sets both the water outlook and how contested the concession will be.</li>
<li><b>Build-ability.</b> Topographic and geotechnical survey for gentle clear hectares, a stable pad and earthworks volume. Decisive on the highland; still worth doing on the flank.</li>
<li><b>Protected-area overlay.</b> Arcabuco: SFF Iguaque, the delimited páramo, Serranía El Peligro, ~30 m rondas hídricas. Moniquirá: the 13 municipal <i>Conservación Hídrica</i> reserves and the El Peligro edge.</li>
<li><b>Title and tenure.</b> Certificado de Tradición y Libertad (SNR/VUR), ANT baldío check, UAF status — and confirm the <b>municipality</b> on the matrícula, given the repeated vereda-name collisions.</li>
<li><b>Access and services.</b> Legal access/easement and the final unpaved stretch; EBSA grid distance; internet (Starlink fallback); and confirm at Planeación that current zoning permits residencial-campestre — both EOTs are ~20 years old.</li>
</ul>

<div class="foot">Method &amp; caveats: parcel inventory from FincaRaíz, re-verified 8 Aug 2026 (all nine July parcels live, prices unchanged). Water balance from Corpoboyacá POMCA Medio y Bajo Suárez (Consorcio POMCA 2015) subcatchment values with monthly shape from climate-data.org 1991–2021; Moniquirá temperature reconciled across climate-data.org, NASA POWER and an IDEAM-anchored lapse rate (range 18.2–19.6 °C, central 18.8). Slope from ESA Copernicus GLO-30 at 30 m. Services, hazards, UAF and water-quality data from the Moniquirá PDM 2020-2023 and POMCA. Terrain photographs are listing galleries plus OpenTopoMap relief. Slope is area-level, not per-parcel; parcel locations remain vereda-level. Nothing here is verified on the ground — treat every "own water / good access / X hectares" as the seller's claim until a surveyor confirms it. Decision-support only: title work needs a Colombian abogado/notario, and any parcel needs on-site geotechnical, hydrogeological and structural survey before purchase or construction.</div>
</div></body></html>"""

open("outputs/arcabuco_dossier.html", "w", encoding="utf-8").write(HTML)
print("Saved outputs/arcabuco_dossier.html", round(len(HTML) / 1e6, 2), "MB · imgs:",
      HTML.count("data:image/"))
