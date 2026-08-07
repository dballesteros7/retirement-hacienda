"""Arcabuco wet-flank dossier v2 — all 9 candidates photo-scrutinized + climate fork."""
import base64
S="outputs/shots"
def img(fn): return "data:image/jpeg;base64,"+base64.b64encode(open(f"{S}/{fn}","rb").read()).decode()
I={
 "A":img("screenshot-1784473887655-0.jpg"),"Clead":img("screenshot-1784473887656-1.jpg"),
 "Cspring":img("screenshot-1784473958903-2.jpg"),"B":img("screenshot-1784474148823-6.jpg"),
 "topo_regio":img("screenshot-1784474065523-4.jpg"),"topo_gach":img("screenshot-1784474065523-5.jpg"),
 "D":img("screenshot-1784475339222-0.jpg"),"E":img("screenshot-1784475378771-3.jpg"),
 "F":img("screenshot-1784475415303-4.jpg"),"G":img("screenshot-1784475444227-5.jpg"),
 "H":img("screenshot-1784475471382-6.jpg"),"Isf":img("screenshot-1784475496175-7.jpg"),
 "topo_moni":img("screenshot-1784475532278-8.jpg"),
}
def card(cls,badge,badgecls,title,meta,url,imgs,paras,flag):
    ims="".join(f'<img src="{s}" alt="">' for s in imgs)
    if len(imgs)>1: ims=f'<div class="imgrow">{ims}</div>'
    ps="".join(f"<p>{p}</p>" for p in paras)
    return f"""<div class="cand {cls}"><div class="ch"><h3>{title}</h3><span class="badge {badgecls}">{badge}</span></div>
    <div class="meta">{meta} · <a href="{url}" target="_blank">listing ↗</a></div>{ims}{ps}
    <p class="flag"><b>Verify on the ground:</b> {flag}</p></div>"""

COOL = (
card("top","best turnkey balance","","A · Arcabuco — Peñas Blancas (with house)",
 "2.97 ha · <b>COP 400 M</b> · house 128 m² · ~2,570 m","https://www.fincaraiz.com.co/finca-en-venta-en-arcabuco/193601271",[I["A"]],
 ["<b>Photos:</b> rolling green pasture with real 360° valley-and-forest panoramas and a modest older teal farmhouse. Green with dry-season tan grass and forest edges.",
  "<b>Terrain:</b> undulating, not flat — you'd site the house on a chosen bench with some earthworks. <b>Water/access:</b> quebrada + potable tank; 1.3 km off the paved highway with power/septic/gas in — best-serviced of the cheap tier."],
 "slope for a real pad; water flow + Corpoboyacá concession; that the upper edge is clear of the SFF/páramo boundary; last-stretch road; Peñas Blancas soils are flagged clay/poor.")
+
card("top","best value & wettest","green","C · Gachantivá — La Hoya (blank land)",
 "5.45 ha · <b>COP 230 M</b> (<b>cheapest/m²</b>) · no house · ~2,100 m","https://www.fincaraiz.com.co/finca-en-venta-en-la-hoya-gachantiva/192743485",[I["Clead"],I["Cspring"]],
 ["<b>Photos:</b> the lushest, wettest parcel — bright green pasture, mature trees, dense native fern/cloud-forest scrub, and a visible spring in the ferns. Forested mountains all around.",
  "<b>Terrain:</b> rolling-to-<b>steep</b> in a basin (\"La Hoya\"); much of the 5.45 ha is dense scrub/forest, so the genuinely flat, clear <b>net-buildable area looks limited</b> — the headline question here. Wonderful for water/privacy/ecology, harder to site."],
 "<b>how much is actually buildable</b> (clear/gentle vs steep/forest); drainage at the basin low point; access-road grade; water rights; any strip in a ronda hídrica.")
+
card("top","cheapest highland, strong water","","B · Arcabuco — Peñas Blancas (blank land)",
 "2.43 ha · <b>COP 270 M</b> · no house · ~2,570 m · <i>neighbours A</i>","https://www.fincaraiz.com.co/finca-en-venta-en-arcabuco/192742902",[I["B"]],
 ["<b>Photos:</b> a signed Peñas Blancas parcel actively cultivated with maize on a <b>sloped hillside</b>, a fern-filled spring, dry-season pasture, rough access track.",
  "<b>Terrain:</b> visibly steeper/rougher than neighbour A; a blank canvas but you're buying slope + a farm track. <b>Water:</b> best-claimed of the cheap tier (nacimiento + quebrada + reservorios)."],
 "slope for a pad; access-road condition + legal access; water rights + flow; distance to EBSA power; title/UAF.")
+
card("","comfortable house · premium","","D · Arcabuco — Monte Suárez (finished home)",
 "8.93 ha · <b>COP 1,600 M</b> · house 240 m² + caretaker · ~2,650 m","https://www.fincaraiz.com.co/finca-en-venta-en-monte-suarez-arcabuco/192742895",[I["D"]],
 ["<b>Photos:</b> the most finished, comfortable house of the set — two-storey stone-and-white home, terracotta roof, wood-beamed ceilings, wood stove, furnished bedrooms/kitchen/bath. Set on a wooded slope; waterfall + spring claimed.",
  "<b>Terrain/location:</b> higher and heavily forested; the land is steep and tree-covered. <b>The catch:</b> Monte Suárez's head touches SFF Iguaque — the forest/waterfall charm sits near the protected edge, and the price is premium."],
 "<b>first</b>, that the parcel + its water are fully OUTSIDE the SFF Iguaque / páramo; then structural survey of the house, water rights, and access.")
+
card("","charming home · Villa de Leyva side","","F · Villa de Leyva — Sabana (adobe farmhouse)",
 "7.54 ha · <b>COP 1,300 M</b> (price reduced) · traditional house · ~2,300 m","https://www.fincaraiz.com.co/finca-en-venta-en-sabana-villa-de-leyva/192743084",[I["F"]],
 ["<b>Photos:</b> a charming traditional adobe/tapia farmhouse — ochre walls, tile roof, blue trim, flower-filled yard, tree-lined lane. The most 'move-in and love it' home; gentler, treed, rolling land.",
  "<b>Location:</b> ~20 min from Villa de Leyva toward Arcabuco — keeps VdL's amenities/tourism, but it's the <b>drier VdL side</b> (the water-constrained municipality), so the spring+creek claim matters most here. Pricey per m²."],
 "the water source is real, year-round, and legally securable (this is the dry side); title; whether any heritage/POT rule reaches the parcel.")
+
card("","compact turnkey · too small for a group","","I · Santa Sofía — Barbilla y Mané",
 "0.72 ha · <b>COP 800 M</b> · house ~147 m² · ~2,300 m","https://www.fincaraiz.com.co/finca-en-venta-en-barbilla-y-mane-santa-sofia/192865610",[I["Isf"]],
 ["<b>Photos:</b> a modest single-storey house on a gentle grassy plot with mountain views; basic but functional; utilities + paved access.",
  "<b>Fit:</b> at 0.72 ha it's a <b>single-home lot — too small</b> for a group hacienda with several casitas, and priciest per m². Listed here for completeness / a solo fallback, not the group goal."],
 "n/a for the group use-case unless combined with an adjacent parcel.")
)

WARM = (
card("top warm","most buildable value","gold","G · Moniquirá — Papayal (best buildable value)",
 "9.11 ha · <b>COP 390 M</b> (~4,300/m²) · no house · ~1,700 m","https://www.fincaraiz.com.co/finca-en-venta-en-papayal-moniquira/192742687",[I["G"]],
 ["<b>Photos:</b> the <b>flattest, most usable land of the whole set</b> — gentle silvopasture with mature spreading shade trees and grazing cattle. The listing's \"~90% usable\" looks credible.",
  "<b>Terrain:</b> gentle/rolling, open, genuinely buildable — the opposite of the steep highland parcels. <b>Trade-off:</b> warm subtropical (~19 °C), ~40 min beyond Arcabuco; a different, warmer lifestyle. Cheapest large parcel found."],
 "confirm the flat impression across the full 9 ha; water source + concession; access; title/UAF; that warm ~19 °C suits the group.")
+
card("top warm","lowest diligence risk","gold","H · Moniquirá — lote (geotech already done)",
 "8.0 ha · <b>COP 720 M</b> · no house · ~1,700 m · <i>Casa 360</i>","https://www.fincaraiz.com.co/lote-en-venta-en-moniquira/193363278",[I["H"]],
 ["<b>Photos:</b> open, gently-rolling ridgetop pasture with a magnificent moss-draped tree and sweeping valley panoramas — buildable and scenic.",
  "<b>De-risked:</b> soil + water studies already done, fully fenced, 3 km paved + 2 km unpaved access. <b>Notes:</b> warm Moniquirá; the listing's \"2 m²\" area is a data error (it's ~8 ha)."],
 "read the existing soil/water studies; confirm area/boundaries; access last 2 km; title/UAF.")
+
card("warm","spectacular water · steep","","E · Moniquirá — Neval y Cruces (the waterfalls)",
 "8.5 ha · <b>COP 750 M</b> · no house · ~1,700 m","https://www.fincaraiz.com.co/finca-en-venta-en-neval-y-cruces-moniquira/192899845",[I["E"]],
 ["<b>Photos:</b> genuine <b>waterfalls</b> cascading through dense subtropical forest — the most water-dramatic parcel by far.",
  "<b>Terrain:</b> waterfalls mean steep relief + heavy forest → <b>limited flat buildable land</b> (like La Hoya, but warm). A 'wow'/eco parcel more than an easy build site."],
 "net buildable area vs steep forest; that the waterfall/creek is on-title and not in a protected ronda; access; warm climate fit.")
)

CSS="""
:root{--cream:#faf7f2;--ink:#2b2620;--mut:#6b6157;--line:#e6ded2;--terra:#b5613a;--sage:#5b7a5b;--gold:#b8860b;--card:#fff}
*{box-sizing:border-box}body{margin:0;background:var(--cream);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;line-height:1.6}
.wrap{max-width:960px;margin:0 auto;padding:40px 22px 80px;background:var(--card)}
h1{font-family:Georgia,serif;font-size:30px;margin:.1em 0}.sub{color:var(--mut);font-size:15.5px;margin-bottom:6px}
h2{font-family:Georgia,serif;font-size:22px;margin:34px 0 8px;border-bottom:2px solid var(--line);padding-bottom:5px}
h3{font-size:18px;margin:0}p{font-size:15px}
.callout{background:var(--cream);border:1px solid var(--line);border-left:4px solid var(--sage);border-radius:8px;padding:14px 16px;margin:14px 0;font-size:14.5px}
.callout.warn{border-left-color:var(--terra)}.callout.fork{border-left-color:var(--gold);background:#fbf7ee}
.cand{border:1px solid var(--line);border-radius:12px;padding:18px;margin:16px 0}
.cand.top{border:2px solid var(--sage)}.cand.top.warm,.cand.warm.top{border:2px solid var(--gold)}
.ch{display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:6px}
.badge{font-size:11.5px;background:#efe7db;color:#7a5a3a;border-radius:14px;padding:3px 10px;white-space:nowrap}
.badge.green{background:#e4efe2;color:#3f6b43}.badge.gold{background:#f3e9cf;color:#8a6d15}
.meta{color:var(--mut);font-size:13.5px;margin:5px 0 12px}
.cand img{width:100%;border:1px solid var(--line);border-radius:8px;margin:6px 0}
.imgrow{display:grid;grid-template-columns:1fr 1fr;gap:8px}@media(max-width:640px){.imgrow{grid-template-columns:1fr}}
.cand p{margin:8px 0}.flag{background:#fbf3ec;border:1px solid #f0dcc9;border-radius:8px;padding:9px 12px;font-size:14px}
.terr img{width:100%;border:1px solid var(--line);border-radius:8px;margin:8px 0}
ol,ul{padding-left:1.25em}li{margin:.35em 0;font-size:14.5px}a{color:var(--sage)}
.foot{margin-top:34px;padding-top:16px;border-top:1px solid var(--line);color:var(--mut);font-size:13px}
"""

HTML=f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Arcabuco wet flank — property dossier (v2, all 9 scrutinized)</title><style>{CSS}</style></head><body><div class="wrap">
<h1>Arcabuco wet flank — property dossier</h1>
<div class="sub">All nine candidate fincas photo-scrutinized and terrain-checked. Buildable ~1–10 ha across Arcabuco · Gachantivá · Santa Sofía · Moniquirá. Updated 19 Jul 2026 — decision-support before sending experts to the ground.</div>

<div class="callout fork"><b>The real fork we found by looking closely.</b> Two very different tracks, and you should pick the <i>climate</i> first, then the parcel:
<br>• <b>Cool green highland (~2,100–2,700 m, ~13–16 °C)</b> — Arcabuco &amp; Gachantivá: the classic "wet flank" — lush, cool, beautiful, but <b>steep</b>, so buildable flat area and protected-boundary proximity are the constraints.
<br>• <b>Warm Moniquirá flank (~1,700 m, ~19 °C)</b> — north down the paved Ruta 62: the <b>gentlest, cheapest, most genuinely buildable land</b> we saw (open pasture, big trees), with abundant water — but it's a warm, subtropical lifestyle and ~40 min farther from Villa de Leyva/Tunja.</div>

<div class="callout warn"><b>Two constraints still gate everything.</b> (1) Arcabuco's high south-west third is the <b>protected SFF Iguaque park + delimited páramo</b> — no-build; the wettest, most forested parcels flirt with this edge, so overlay every candidate on the park before an offer. (2) The subdivision floor (<b>UAF ≈ 9.9 ha</b>) means you buy <b>one titled parcel in a shared SAS</b>, not divided lots.</div>

<h2>The terrain, from the topographic maps</h2>
<div class="terr">
<img src="{I['topo_regio']}" alt="Topographic map of the wet-flank highland cluster">
<p class="sub">The steep green block in the centre is the protected <b>Iguaque massif (3,825 m)</b>. Gachantivá (NW) and Arcabuco (N) sit clear of it; the gentler ground is in the valley basins.</p>
<img src="{I['topo_moni']}" alt="Topographic map of the warm Moniquirá flank">
<p class="sub"><b>The warm flank:</b> north down Ruta 62, Arcabuco (high, by Cerro Iguaque) descends to <b>Moniquirá</b> — lower, warmer, greener, more dissected subtropical hill country. E/G/H sit here; steeper along the river cuts (waterfalls at Neval y Cruces), gentler on the ridges and Papayal.</p>
</div>

<h2>Track 1 — Cool green highland (Arcabuco · Gachantivá · Villa de Leyva side)</h2>
{COOL}

<h2>Track 2 — Warm Moniquirá flank (~1,700 m)</h2>
{WARM}

<h2>Recommended shortlist for ground experts</h2>
<p><b>If the group wants the cool-green highland (the original wet-flank thesis):</b></p>
<ol>
<li><b>A — Peñas Blancas, with house (COP 400 M)</b> — best all-round: house + utilities + paved-road proximity + water + views. Verify slope for a pad, water rights, and the protected boundary.</li>
<li><b>C — Gachantivá / La Hoya (COP 230 M)</b> — best value & most beautiful; the one thing to resolve on site is <i>how much is actually buildable</i> (steep forest vs gentle clear).</li>
<li><b>B — Peñas Blancas, blank (COP 270 M)</b> — cheapest way into A's exact vereda, with a visible spring; verify slope/access.</li>
<li><i>Also:</i> <b>D — Monte Suárez (COP 1,600 M)</b> if you want a ready comfortable home and will clear the SFF-boundary question first; <b>F — Sabana (COP 1,300 M)</b> for a charming turnkey with Villa de Leyva proximity — but confirm its water on the dry side.</li>
</ol>
<p><b>If the group is open to a warmer, gentler, more buildable setting (Moniquirá):</b></p>
<ol>
<li><b>G — Papayal (COP 390 M, 9 ha)</b> — the most usable, buildable land at the best value; confirm the flat impression and water.</li>
<li><b>H — geotech lote (COP 720 M, 8 ha)</b> — buildable, sweeping views, and diligence already started (soil + water studies, fenced).</li>
<li><b>E — Neval y Cruces (COP 750 M)</b> — only if the group wants the waterfalls and accepts steep, forested ground.</li>
</ol>

<h2>What each site visit must confirm (universal checklist)</h2>
<ul>
<li><b>Build-ability:</b> topographic + geotechnical survey — gentle, clear hectares; stable pad; earthworks. (This is decisive on the highland parcels.)</li>
<li><b>Water, legally:</b> hydrogeology of the spring/creek + a Corpoboyacá <b>concesión de aguas</b>; IRCA water-quality test. Abundant rain ≠ a legal, potable, on-parcel source.</li>
<li><b>Protected-area overlay:</b> fully outside SFF Iguaque, the delimited páramo Iguaque-Merchán, the Serranía El Peligro reserve, and every ~30 m ronda-hídrica setback (critical for D and the wettest parcels).</li>
<li><b>Title & tenure:</b> Certificado de Tradición y Libertad (SNR/VUR), ANT baldío check, UAF status — buy one parcel, hold in the SAS.</li>
<li><b>Access & services:</b> legal access/easement + final unpaved-stretch condition; EBSA grid distance; internet (Starlink fallback); current zoning permits residencial-campestre (EOT is dated — confirm at Planeación).</li>
</ul>

<div class="foot">Method & caveats: inventory from FincaRaíz; all nine listings' photo galleries scrutinized in-browser; terrain from listing photos + OpenTopoMap (SRTM/Sonny) relief. A parcel-resolution DEM and live routing were not reachable in this environment, so slope is read visually and locations are vereda-level (exact boundaries + true buildable hectares are for the ground survey). Nothing here is verified — treat every "own water / good access" as the seller's claim until a surveyor confirms it. All URLs accessed 19 Jul 2026.</div>
</div></body></html>"""
open("outputs/arcabuco_dossier.html","w",encoding="utf-8").write(HTML)
print("Saved outputs/arcabuco_dossier.html", round(len(HTML)/1e6,2),"MB · imgs:", HTML.count("data:image/jpeg"))
