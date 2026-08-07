"""Build a single self-contained, friend-facing overview page with the interactive
scorecard embedded. Warm brochure styling. -> outputs/hacienda_overview.html"""
import json, base64
D = json.load(open("outputs/scorecard_data.json"))
payload = json.dumps(D, ensure_ascii=False)
wb = base64.b64encode(open("outputs/fig_water_balance.png","rb").read()).decode()

CARDS = [
 ("pick","Our pick","The Wet Flank","Arcabuco · Gachantivá · Santa Sofía",
  "~14–16 °C, green hills","≈ 4–18k COP/m² (cheapest)",
  "Water all year round, the cheapest land, no heritage building limits, ~40–60 min to Tunja's hospital.",
  "Cooler and cloudier than the valley; fewer shops nearby; ~3 h to Bogotá's airport."),
 ("warm","Easy-airport option","Mesitas / Tequendama","El Colegio, Cundinamarca",
  "~23 °C, warm year-round","≈ 49–130k COP/m²",
  "Closest to Bogotá's airport (~1 h 47) and its big hospitals (~1.5 h); pleasant warm climate.",
  "Rainy-season landslides close the access roads; some rural property crime."),
 ("pretty","The postcard","Villa de Leyva (town)","Boyacá",
  "~17–18 °C, sunny","≈ 110k COP/m² (priciest)",
  "The best climate and the prettiest town of them all; great amenities and tourism.",
  "Water is tight (the town rationed in 2016); most expensive; heritage rules limit building."),
 ("city","The city base","Tunja","Boyacá capital",
  "~13 °C, cool","≈ 15–108k COP/m²",
  "Safest option, best hospital and everyday services, strongest new roads.",
  "Cold for a warm retirement; no nearby airport (~2.5–3 h to Bogotá)."),
]
cards_html = ""
for cls,tag,name,where,clim,price,pro,con in CARDS:
    star = "★ " if cls=="pick" else ""
    cards_html += f"""
    <div class="card {cls}">
      <div class="tag">{tag}</div>
      <h3>{star}{name}</h3>
      <div class="where">{where}</div>
      <div class="facts"><span>{clim}</span><span>{price}</span></div>
      <p class="pro"><b>Draw:</b> {pro}</p>
      <p class="con"><b>Catch:</b> {con}</p>
    </div>"""

PARCELS = [
 ("Arcabuco / Peñas Blancas","COP 400 M · 3 ha","Stream + potable tank, 1.3 km paved road. The best all-round wet-flank pick.","https://fincaraiz.com.co/finca-en-venta-en-arcabuco/193601271"),
 ("Gachantivá / La Hoya","COP 230 M · 5.5 ha","Forest + springs on the Gachantivá–Villa de Leyva road. Cheapest larger parcel.","https://fincaraiz.com.co/finca-en-venta-en-la-hoya-gachantiva/192743485"),
 ("Tena / Catalamonte (Tequendama)","COP 1,750 M · 24 ha","2 springs + 2 streams, ~25 min to the airport. If we weight airport access highest.","https://fincaraiz.com.co/finca-en-venta-en-catalamonte-tena/193286551"),
]
parcels_html = ""
for name,price,note,url in PARCELS:
    parcels_html += f"""<div class="parcel"><div class="pn">{name}</div><div class="pp">{price}</div><div class="pnote">{note}</div><a href="{url}" target="_blank" rel="noopener">see the listing ↗</a></div>"""

HTML = r"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Our Retirement Hacienda — Where Should We Build?</title>
<style>
:root{--cream:#faf7f2;--ink:#2b2620;--mut:#6b6157;--line:#e6ded2;--terra:#b5613a;--sage:#5b7a5b;--gold:#c99a3f;--card:#fff}
*{box-sizing:border-box}body{margin:0;background:var(--cream);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;line-height:1.6}
.wrap{max-width:940px;margin:0 auto;padding:0 20px 70px}
.hero{padding:54px 0 30px;border-bottom:1px solid var(--line);text-align:center}
h1{font-family:Georgia,'Times New Roman',serif;font-size:34px;line-height:1.15;margin:0 0 10px;letter-spacing:-.3px}
.lede{font-size:18px;color:var(--mut);max-width:640px;margin:0 auto 20px}
.verdict{display:inline-block;background:var(--sage);color:#fff;padding:12px 20px;border-radius:30px;font-size:15.5px}
.verdict b{font-weight:700}
h2{font-family:Georgia,serif;font-size:24px;margin:44px 0 6px}
.sec-sub{color:var(--mut);margin:0 0 18px;font-size:15px}
.cards{display:grid;grid-template-columns:1fr 1fr;gap:16px}@media(max-width:720px){.cards{grid-template-columns:1fr}}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px 18px 16px;position:relative}
.card.pick{border:2px solid var(--sage);box-shadow:0 4px 18px rgba(91,122,91,.12)}
.tag{font-size:11px;text-transform:uppercase;letter-spacing:.09em;color:var(--terra);font-weight:700;margin-bottom:4px}
.card.pick .tag{color:var(--sage)}
.card h3{font-family:Georgia,serif;font-size:19px;margin:0 0 2px}
.where{color:var(--mut);font-size:13px;margin-bottom:10px}
.facts{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:10px}
.facts span{background:var(--cream);border:1px solid var(--line);border-radius:14px;padding:3px 10px;font-size:12.5px}
.card p{margin:6px 0;font-size:14px}.pro b{color:var(--sage)}.con b{color:var(--terra)}
.water{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:20px;margin-top:14px}
.water img{width:100%;border:1px solid var(--line);border-radius:8px;margin-top:12px}
/* scorecard */
#sc{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:20px;margin-top:14px}
.presets{display:flex;flex-wrap:wrap;gap:7px;margin-bottom:14px}
.presets button{font-size:12.5px;padding:7px 12px;border:1px solid var(--line);background:var(--cream);border-radius:18px;cursor:pointer}
.presets button.active{background:var(--terra);color:#fff;border-color:var(--terra)}
.sc-grid{display:grid;grid-template-columns:1fr 1fr;gap:26px}@media(max-width:720px){.sc-grid{grid-template-columns:1fr}}
.wt{display:flex;align-items:center;gap:8px;margin:6px 0;font-size:13px}
.wt label{flex:0 0 150px;color:#3a342c}.wt input{flex:1;accent-color:var(--terra)}.wt .val{flex:0 0 26px;text-align:right;color:var(--mut)}
.bar-row{margin:11px 0}.bar-row .top{display:flex;justify-content:space-between;font-size:14px;margin-bottom:4px}
.bar-row .name{font-weight:600}.bar-row .score{font-weight:700;color:var(--sage)}
.track{height:24px;background:var(--cream);border:1px solid var(--line);border-radius:6px;overflow:hidden}
.fill{height:100%;background:linear-gradient(90deg,#8aa88a,#a9c0a0);transition:width .35s}
.rank1 .fill{background:linear-gradient(90deg,#5b7a5b,#76986f)}
.parcels{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-top:14px}@media(max-width:720px){.parcels{grid-template-columns:1fr}}
.parcel{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px}
.pn{font-weight:700;font-size:15px}.pp{color:var(--terra);font-weight:700;margin:3px 0 6px}.pnote{font-size:13.5px;color:#4a443c;margin-bottom:8px}
.parcel a{color:var(--sage);text-decoration:none;font-size:13px;font-weight:600}
.foot{margin-top:40px;padding-top:18px;border-top:1px solid var(--line);color:var(--mut);font-size:13.5px}
</style></head><body><div class="wrap">
<div class="hero">
  <h1>Our Retirement Hacienda</h1>
  <div class="lede">Four beautiful places in the Colombian highlands, weighed on the things that matter for the next 30 years. Here's where the evidence points — and a scorecard you can play with yourself.</div>
  <div class="verdict">The pick: <b>the wet north-east flank of the Ricaurte valley</b> — mild, green, water-secure, and the most affordable land.</div>
</div>

<h2>The shortlist</h2>
<p class="sec-sub">Same region, very different trade-offs. Our top choice is marked.</p>
<div class="cards">%%CARDS%%</div>

<h2>Why not just buy in pretty Villa de Leyva? Water.</h2>
<p class="sec-sub">The single biggest factor over 30 years — and the one that quietly separates these places.</p>
<div class="water">
  <p style="margin-top:0">Villa de Leyva is gorgeous, but it sits on a semi-arid valley floor: it <b>rationed drinking water in 2016</b>, and it dries out every year. Our model of rainfall vs. evaporation (below) shows the valley towns — Villa de Leyva, Tunja, Sáchica — running a moisture <b>deficit</b> (the red) through much of the year, while <b>Arcabuco and the wet flank sit in surplus</b> (rain towering over the red line). A short drive uphill onto the wet side gets us the same landscape and climate <em>with</em> water security — the thing you can't easily fix once you've built.</p>
  <img src="data:image/png;base64,%%WBFIG%%" alt="Monthly rainfall vs. water demand for each area — red shows deficit months">
</div>

<h2>Weigh in — what matters most to you?</h2>
<p class="sec-sub">Drag the sliders or pick a lens. Watch the ranking reshuffle. (However you weight it, the wet flank stays on top — but the runners-up trade places.)</p>
<div id="sc">
  <div class="presets" id="presets"></div>
  <div class="sc-grid">
    <div><div id="weights"></div></div>
    <div><div id="bars"></div></div>
  </div>
</div>

<h2>Three real parcels to daydream about</h2>
<p class="sec-sub">Actual current listings. Prices and "own water" claims still need local checking before anyone gets too excited.</p>
<div class="parcels">%%PARCELS%%</div>

<div class="foot">This is a starting point for our conversation, not a done deal. Every parcel still needs local checks — water, slope, and clean title — before an offer. The full report (with all the evidence and sources) and the interactive map are in our shared Claude artifacts. Analysis: July 2026.</div>

<script>
const D=%%PAYLOAD%%;
let W=Object.assign({},D.presets["Default (brief priority)"]);let curPreset="Default (brief priority)";
const el=id=>document.getElementById(id);
const LENS={"Default (brief priority)":"Balanced","Climate-first":"Climate first","Water-first":"Water first","Services & airport-first":"Airport & services","Cost-first":"Budget first"};
function totals(){const s=Object.values(W).reduce((a,b)=>a+b,0)||1;const o=D.units.map(u=>{let t=0;D.criteria.forEach(c=>t+=D.scores[u][c.key].v*W[c.key]);return{u,v:t/s}});o.sort((a,b)=>b.v-a.v);return o}
function renderPresets(){el("presets").innerHTML="";Object.keys(D.presets).forEach(n=>{const b=document.createElement("button");b.textContent=LENS[n]||n;b.className=(n===curPreset?"active":"");b.onclick=()=>{W=Object.assign({},D.presets[n]);curPreset=n;renderAll()};el("presets").appendChild(b)})}
function renderWeights(){const w=el("weights");w.innerHTML="";D.criteria.forEach(c=>{const r=document.createElement("div");r.className="wt";r.innerHTML=`<label>${c.label.replace(/ \(.*\)/,'')}</label><input type=range min=0 max=30 value=${W[c.key]} data-k="${c.key}"><span class="val">${W[c.key]}</span>`;w.appendChild(r)});w.querySelectorAll("input").forEach(i=>i.oninput=e=>{W[e.target.dataset.k]=+e.target.value;curPreset="Custom";renderAll()})}
function renderBars(){const t=totals();let h="";t.forEach((x,i)=>{h+=`<div class="bar-row ${i===0?'rank1':''}"><div class="top"><span class="name">${i+1}. ${x.u}</span><span class="score">${x.v.toFixed(1)}</span></div><div class="track"><div class="fill" style="width:${x.v.toFixed(1)}%"></div></div></div>`});el("bars").innerHTML=h}
function renderAll(){renderPresets();renderWeights();renderBars()}
renderAll();
</script>
</div></body></html>"""
out = (HTML.replace("%%CARDS%%",cards_html).replace("%%PARCELS%%",parcels_html)
           .replace("%%PAYLOAD%%",payload).replace("%%WBFIG%%",wb))
open("outputs/hacienda_overview.html","w",encoding="utf-8").write(out)
print("Saved outputs/hacienda_overview.html", round(len(out)/1000,1),"KB")
