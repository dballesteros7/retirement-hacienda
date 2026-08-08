"""Friend-facing overview page — the one a non-analyst actually reads.

v3 (2026-08-08): rebuilt around the decision the group is actually making. Four shortlisted
parcels with real depth (including what it costs to make each one liveable), the water and
terrain evidence in plain language, the interactive scorecard, and a "daydreaming" section
carrying the community masterplan — one casa comunal, three satellite houses — with a phased
budget from code/masterplan.py. -> outputs/hacienda_overview.html
"""
import json, base64
import pandas as pd

D = json.load(open("outputs/scorecard_data.json"))
payload = json.dumps(D, ensure_ascii=False)


def b64(p):
    return base64.b64encode(open(p, "rb").read()).decode()


wb = b64("outputs/fig_water_balance.png")
sl = b64("outputs/fig_slope.png")
mp = b64("outputs/fig_masterplan.png")

phases = pd.read_csv("outputs/masterplan_phases.csv")
summary = pd.read_csv("outputs/masterplan_summary.csv")
H = summary[summary.parcel == "H"].iloc[0]

# ---------------------------------------------------------------- the four real options ------
OPTIONS = [
 dict(cls="pick", tag="Best land to build on", name="H · the geotech lote", where="Moniquirá · 8 ha · COP 720 M",
      facts=["~19 °C, warm", "9,000 COP/m²", "15 min to town"],
      story="Open, gently-sloping ridgetop pasture with mature shade trees and a long view over the "
            "valley. Already fully fenced, 15 paddocks, an aljibe and a well. The photographs show clean, "
            "clear ground — no rock outcrops, no scrub, nothing to clear before you start.",
      why="<b>It comes with a geotechnical study of the soil and of the water, already done and handed "
          "over.</b> That is the single most valuable document in the whole search — every other parcel "
          "would have to pay for it, and it is the study that tells you whether you can actually build. "
          "The listing also says outright that the price is negotiable.",
      cost="Land 720 M + roughly 2,070 M to build the community (below) ≈ <b>2,790 M all-in</b>.",
      check="Read the existing soil and water studies first — they are why you would pay the premium "
            "over Papayal. Then the last 2 km of unpaved access, and the title.",
      url="https://www.fincaraiz.com.co/lote-en-venta-en-moniquira/193363278"),
 dict(cls="value", tag="Cheapest usable land", name="G · Papayal", where="Moniquirá · 9.1 ha · COP 390 M",
      facts=["~19 °C, warm", "4,281 COP/m²", "cheapest per m²"],
      story="A broad flat valley-bottom pasture with big shade trees and grazing cattle, and a real "
            "stream running over cobbles in deep shade — the water in the photos is genuinely there.",
      why="Best price per usable hectare anywhere in the search, and it has been sitting unsold with "
          "the same agency for <b>twelve months</b>.",
      cost="Land 390 M + about 2,100 M to build ≈ <b>2,490 M all-in</b> — including a "
           "<b>45 M karst contingency</b> the other parcels do not need.",
      check="<b>The photos show limestone karst</b> — a deep rock ravine, an exposed outcrop with a cave "
            "recess. That means possible voids under foundations, groundwater that moves fast and "
            "unpredictably, and septic fields that can reach the aquifer quickly. Get a geotechnical and "
            "hydrogeological survey <i>before</i> offering, not after. And treat “90% usable” as a "
            "seller's number: a real share of it is gorge and steep forest.",
      url="https://www.fincaraiz.com.co/finca-en-venta-en-papayal-moniquira/192742687"),
 dict(cls="big", tag="The one we could actually divide", name="N · the panela farm", where="Moniquirá · 41 ha · COP 1,700 M",
      facts=["~19 °C, warm", "4,150 COP/m²", "41 hectares"],
      story="A working sugar-cane farm on semi-flat ground with good soils, its own wells, a vereda "
            "aqueduct, a maintained gravel road — and a complete trapiche: mill, moulding room, furnace. "
            "Two simple houses already stand on it.",
      why="At the same price per m² as Papayal it is <b>four and a half times the land</b>, and it is the "
          "<b>only parcel we found above the 9.38 ha legal subdivision floor</b>. That matters enormously: "
          "everywhere else, the group has to buy one parcel and hold it jointly through a company. Here "
          "each family could own its own titled plot. It has also been on the market fourteen months.",
      cost="Land 1,700 M + about 2,250 M ≈ <b>3,950 M all-in</b> — but you are buying an income and "
           "existing buildings alongside the land.",
      check="Whether the cane operation is genuinely running or just standing. Soil quality claims. And "
            "get a surveyor to confirm the 41 ha before assuming the subdivision maths works.",
      url="https://www.fincaraiz.com.co/finca-en-venta-en-moniquira/192463144"),
 dict(cls="cool", tag="Move in on day one", name="A · Peñas Blancas", where="Arcabuco · 3 ha · COP 400 M",
      facts=["~14 °C, cool green", "13,472 COP/m²", "house included"],
      story="A 4-bedroom farmhouse with a fireplace, a full kitchen and wraparound eaves, on rolling "
            "green pasture with a 360° view. Mains electricity, septic, bottled gas, a stream and a "
            "potable reserve tank. Just 1.3 km off the paved road — three minutes' drive.",
      why="The only shortlisted parcel where <b>you could sleep on site from week one</b> while the rest "
          "is built. And it sits on the flank with the best drought resilience we measured.",
      cost="Land 400 M. The house is already there, so the build programme shrinks — but at 3 ha it is "
           "tight for four houses with any privacy.",
      check="At 2.97 ha this is small for a community of four buildings. It also browns off visibly in "
            "the dry season and the Peñas Blancas soils are flagged as poor clay.",
      url="https://www.fincaraiz.com.co/finca-en-venta-en-arcabuco/193601271"),
]

cards = ""
for o in OPTIONS:
    facts = "".join(f"<span>{f}</span>" for f in o["facts"])
    cards += f"""
    <div class="opt {o['cls']}">
      <div class="tag">{o['tag']}</div>
      <h3>{o['name']}</h3>
      <div class="where">{o['where']}</div>
      <div class="facts">{facts}</div>
      <p>{o['story']}</p>
      <p class="why"><b>Why it's here:</b> {o['why']}</p>
      <p class="cost"><b>What it costs:</b> {o['cost']}</p>
      <p class="check"><b>Before you fall in love:</b> {o['check']}</p>
      <a href="{o['url']}" target="_blank" rel="noopener">see the listing ↗</a>
    </div>"""

phase_rows = "".join(
    f"<tr><td>{r.phase}</td><td class='num'>{r.cop_M:,.0f}</td>"
    f"<td class='num'>{r.cum_M:,.0f}</td><td class='num'>{r.per_household_M:,.0f}</td>"
    f"<td class='wht'>{r.what}</td></tr>" for r in phases.itertuples())

HTML = r"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Our Retirement Hacienda — Where Should We Build?</title>
<style>
:root{--cream:#faf7f2;--ink:#2b2620;--mut:#6b6157;--line:#e6ded2;--terra:#b5613a;--sage:#5b7a5b;--gold:#c99a3f;--card:#fff}
*{box-sizing:border-box}
body{margin:0;background:var(--cream);color:var(--ink);line-height:1.65;
 font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif}
.wrap{max-width:1000px;margin:0 auto;padding:44px 22px 90px}
h1{font-family:Georgia,serif;font-size:40px;line-height:1.15;margin:.1em 0 .2em}
h2{font-family:Georgia,serif;font-size:26px;margin:52px 0 6px}
h3{font-size:19px;margin:0 0 2px;font-family:Georgia,serif}
.lede{font-size:18.5px;color:#4a443c;max-width:44em}
.sec-sub{color:var(--mut);margin:0 0 16px;max-width:52em}
.hero{text-align:center;padding:8px 0 4px}.hero .lede{margin:0 auto}
.verdict{display:inline-block;margin-top:18px;background:var(--sage);color:#fff;border-radius:30px;
 padding:12px 24px;font-size:16px;max-width:46em}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:18px}
@media(max-width:800px){.opts{grid-template-columns:1fr}}
.opt{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px}
.opt.pick{border:2px solid var(--sage)}.opt.value{border:2px solid var(--gold)}
.tag{font-size:11.5px;text-transform:uppercase;letter-spacing:.09em;color:var(--terra);font-weight:700}
.where{color:var(--mut);font-size:13.5px;margin-bottom:9px}
.facts{display:flex;flex-wrap:wrap;gap:7px;margin-bottom:11px}
.facts span{background:var(--cream);border:1px solid var(--line);border-radius:14px;padding:3px 11px;font-size:12.5px}
.opt p{font-size:14.5px;margin:9px 0}
.why{background:#f2f7f3;border-left:3px solid var(--sage);border-radius:6px;padding:9px 12px}
.cost{background:#fbf7ee;border-left:3px solid var(--gold);border-radius:6px;padding:9px 12px}
.check{background:#fbf3ec;border-left:3px solid var(--terra);border-radius:6px;padding:9px 12px}
.opt a{color:var(--sage);text-decoration:none;font-size:13px;font-weight:700}
.panel{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px;margin-top:14px}
.panel img{width:100%;border-radius:9px;border:1px solid var(--line);margin-top:10px}
.panel p{font-size:15px}
.dream{background:linear-gradient(180deg,#f6f2ea,#faf7f2);border:1px solid var(--line);
 border-radius:16px;padding:26px;margin-top:14px}
.prog{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:16px 0 6px}
@media(max-width:800px){.prog{grid-template-columns:1fr 1fr}}
.pill{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:13px;text-align:center}
.pill .n{font-family:Georgia,serif;font-size:23px;color:var(--terra)}
.pill .l{font-size:12.5px;color:var(--mut)}
.tw{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:13.5px;margin-top:12px;min-width:620px}
th,td{border-bottom:1px solid var(--line);padding:9px 10px;text-align:left;vertical-align:top}
th{font-size:12px;text-transform:uppercase;letter-spacing:.05em;color:var(--mut)}
td.num{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
td.wht{color:var(--mut);font-size:13px}
tr:last-child td{border-bottom:none;font-weight:700}
.presets{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:14px}
.presets button{border:1px solid var(--line);background:var(--card);border-radius:20px;padding:7px 15px;
 font-size:13px;cursor:pointer;color:#4a443c}
.presets button.active{background:var(--sage);color:#fff;border-color:var(--sage)}
.sc-grid{display:grid;grid-template-columns:1fr 1fr;gap:26px}@media(max-width:720px){.sc-grid{grid-template-columns:1fr}}
.wt{display:flex;align-items:center;gap:10px;margin:7px 0;font-size:13.5px}
.wt label{flex:0 0 150px;color:#3a342c}.wt input{flex:1;accent-color:var(--terra)}.wt .val{flex:0 0 26px;text-align:right;color:var(--mut)}
.bar-row{margin:11px 0}.bar-row .top{display:flex;justify-content:space-between;font-size:14px}
.track{height:11px;background:#eee7dc;border-radius:7px;overflow:hidden;margin-top:4px}
.fill{height:100%;background:linear-gradient(90deg,#8aa88a,#a9c0a0);transition:width .35s}
.rank1 .fill{background:linear-gradient(90deg,#5b7a5b,#76986f)}
.note{font-size:13.5px;color:var(--mut);margin-top:10px}
.foot{margin-top:46px;padding-top:18px;border-top:1px solid var(--line);color:var(--mut);font-size:13.5px}
a{color:var(--sage)}
</style></head><body><div class="wrap">

<div class="hero">
  <h1>Our Retirement Hacienda</h1>
  <div class="lede">Two flanks of the same Colombian valley, twelve real parcels, and one honest
  trade-off to settle between us. Here's where the evidence actually points — and what it would
  cost to build the thing we keep talking about.</div>
  <div class="verdict">We're leaning <b>warm — Moniquirá</b>. The numbers say that's defensible.
  It wins on health care and costs the same. It loses on one thing: drought.</div>
</div>

<h2>The choice, in one paragraph</h2>
<p class="sec-sub">Both flanks get <b>the same rainfall</b> — 1,860 mm on the warm side, 1,826 mm up
in Arcabuco. So this was never really about which place is wetter. Moniquirá sits 900 m lower and
is <b>4.8 °C warmer</b>, so more of its rain evaporates. In a normal year that costs nothing at all —
Moniquirá has <b>zero</b> dry months and ends the year in surplus. In an El Niño drought year it
goes to <b>ten</b> difficult months where Arcabuco has three. Against that, Moniquirá has a proper
<b>hospital in town</b> — first <i>and</i> second level, 118 services — and Arcabuco has a village
clinic and a 45-minute drive. That's the whole decision: <b>better health care now, versus better
water in the bad years.</b></p>

<h2>Four parcels worth arguing about</h2>
<p class="sec-sub">Out of twelve we looked at properly — every photo, every listing, every agency.
Six have sat unsold with one agency for a year, so nobody should be paying asking price.
<b>All twelve, with the photo-by-photo reads, are in the <a href="dossier.html">dossier</a>.</b></p>
<div class="opts">%%CARDS%%</div>

<h2>The two things the evidence actually turns on</h2>
<p class="sec-sub">Short version here. The full workings — sources, methods, every number — are in
the <a href="report.html">report</a>.</p>
<div class="panel">
  <p style="margin-top:0"><b>Water, and specifically drought.</b> Rain versus evaporation, month by
  month; red means the ground is drawing down more than it receives. Villa de Leyva — the pretty
  one — is in deficit most of the year and <b>rationed drinking water in 2016</b>. Both our flanks
  sit in surplus, which is why they're the shortlist. The gap only opens in a bad year, and that's
  the whole argument between them.</p>
  <img src="data:image/png;base64,%%WBFIG%%" alt="Monthly rainfall vs water demand for all six areas">
  <p style="margin-top:18px"><b>Terrain — and this one surprised us.</b> We pulled real 30 m
  satellite elevation and measured the slope where parcels are actually sold, rather than across
  the whole mountain. <b>The two flanks are nearly identical</b> — typical ground is about 10° on
  both. What differs is the bad end: <b>Arcabuco has two and a half times more genuinely steep
  land</b>. So it isn't "flat versus steep". It's that in the highland, <b>picking the right parcel
  matters much more</b>, because you're likelier to be shown something difficult.</p>
  <img src="data:image/png;base64,%%SLFIG%%" alt="Slope distribution in the parcel elevation band, Arcabuco vs Moniquirá">
  <p class="note"><b>One warning that applies to every warm-flank parcel:</b> the water is abundant
  but <b>not drinkable as it arrives</b>. Of 23 rural supplies in Moniquirá only three have a
  working treatment plant, and all four the health authority monitors are rated <b>high risk</b>
  with no treatment at all — including the one behind parcel G's "vereda water point". Solvable,
  and costed below: about <b>COP 11–15.5 M</b> for a plant, plus <b>600,000 a year</b>. Budget it,
  don't assume it.</p>
</div>

<h2>Weigh it yourself</h2>
<p class="sec-sub">Drag the sliders, or pick a lens. The wet flank leads four of the five —
but <b>Moniquirá wins on services</b>, and on climate the two are 0.3 points apart. It's close.</p>
<div id="sc">
  <div class="presets" id="presets"></div>
  <div class="sc-grid">
    <div><div id="weights"></div></div>
    <div><div id="bars"></div></div>
  </div>
</div>

<h2>Now the fun part — what would we actually build?</h2>
<div class="dream">
  <p style="margin-top:0;font-size:16px">One <b>casa comunal</b> in the middle — the big kitchen,
  the long table, the fire, a couple of guest rooms for whoever's visiting, the laundry and the
  workshop. Then <b>three private houses</b> scattered around it at 90–140 m, far enough that you
  can't hear each other, close enough to walk over for dinner without thinking about it. Everything
  fed by gravity from one tank uphill, so the water works when the power doesn't.</p>

  <div class="prog">
    <div class="pill"><div class="n">160 m²</div><div class="l">casa comunal</div></div>
    <div class="pill"><div class="n">3 × 80 m²</div><div class="l">private houses</div></div>
    <div class="pill"><div class="n">400 m²</div><div class="l">built in total</div></div>
    <div class="pill"><div class="n">~4 ha</div><div class="l">of the 8 used</div></div>
  </div>

  <img src="data:image/png;base64,%%MPFIG%%" style="width:100%;border-radius:9px;border:1px solid var(--line);margin-top:12px" alt="Indicative site layout and budget comparison">

  <p style="margin-top:16px">The layout isn't decoration — it's built around the constraints we
  actually found. The tank sits uphill of everything so the whole system is gravity-fed. The septic
  fields are pushed well away from the stream. Nothing is inside the <b>30 m ronda hídrica</b>, the
  legal no-build strip along any watercourse. The forest edge stays where it is, for shade and for
  the birds.</p>

  <h3 style="margin-top:22px;font-size:20px">And you don't have to do it all at once</h3>
  <p>This is the part that makes it feel possible. Each phase is a place you can stop.</p>
  <div class="tw"><table>
    <tr><th>Phase</th><th class="num">COP M</th><th class="num">running total</th><th class="num">each</th><th>what it buys</th></tr>
    %%PHASES%%
  </table></div>
  <p class="note">Three households sharing. <b>After phase 2 you are living on the land</b> — the
  communal house and the first private house are finished — for roughly <b>COP 680 M each</b>
  (≈ EUR 158,000 at the 2026 average rate). The last two houses can wait for whenever. All-in,
  finished, on parcel H: about <b>COP 2,790 M</b> — near enough <b>COP 930 M (≈ EUR 216,000) per
  household</b>. Running costs land around <b>COP 26 M a year</b> for everything including a
  part-time caretaker, which is under <b>9 M each</b>.</p>
  <p class="note">These are 2026 published Colombian rates, not quotes — rural building swings
  hugely with access and ground conditions. Treat them as a budget envelope for the conversation,
  ±30%, and get real quotes before anyone transfers anything.</p>
</div>

<h2>What happens next</h2>
<div class="panel">
  <ol>
    <li><b>Settle the climate question between us</b> — warm Moniquirá or cool Arcabuco. Everything
    else follows from that, and the scorecard above is the tool for that argument.</li>
    <li><b>Ask the agencies for coordinates and the matrícula inmobiliaria</b> on the two or three
    we like. We can't check boundaries, protected areas or real slope without them — and one listing
    already has the wrong vereda on it.</li>
    <li><b>Read H's soil and water studies.</b> They already exist. That is a free look at the
    single question that decides whether a parcel is buildable.</li>
    <li><b>Get a water test and a Corpoboyacá concession check</b> on whichever parcel leads.</li>
    <li><b>Then, and only then, make an offer</b> — well under asking, on anything that's been
    sitting for a year.</li>
  </ol>
</div>

<h2>Want to go deeper?</h2>
<div class="panel">
  <p style="margin-top:0">This page is the short version. Each of the others answers one question:</p>
  <ul>
    <li><a href="report.html"><b>The report</b></a> — <i>why here?</i> The regional case: climate,
    water, terrain, services, hazards and law, how the five options rank, and every source.
    Section 5 is the full Moniquirá analysis.</li>
    <li><a href="dossier.html"><b>The dossier</b></a> — <i>which parcel?</i> All twelve candidates,
    every photograph reviewed, with what to verify on each before an offer.</li>
    <li><a href="scorecard.html"><b>The scorecard</b></a> — <i>what if we weight it differently?</i>
    Move the sliders yourself and watch the ranking change.</li>
    <li><a href="map.html"><b>The map</b></a> — <i>where is all this?</i> Municipalities, faults,
    candidate sectors and the parcels, on real terrain.</li>
  </ul>
</div>

<div class="foot">This is decision-support, not advice, and nothing here has been verified on the
ground. Every "own water", "good access" and hectare count is still the seller's claim until a
surveyor says otherwise. Title work needs a Colombian abogado; any parcel needs geotechnical,
hydrogeological and structural survey before purchase or building. Sources, workings and the full
per-parcel notes are in the <a href="report.html">report</a>, the <a href="dossier.html">dossier</a>
and the <a href="map.html">map</a>. Analysis updated 8 August 2026.</div>

<script>
const D=%%PAYLOAD%%;
let W=Object.assign({},D.presets["Default (brief priority)"]);let curPreset="Default (brief priority)";
const el=id=>document.getElementById(id);
const LENS={"Default (brief priority)":"Balanced","Climate-first":"Climate first","Water-first":"Water first","Services & airport-first":"Health & airport","Cost-first":"Budget first"};
function totals(){const s=Object.values(W).reduce((a,b)=>a+b,0)||1;const o=D.units.map(u=>{let t=0;D.criteria.forEach(c=>t+=D.scores[u][c.key].v*W[c.key]);return{u,v:t/s}});o.sort((a,b)=>b.v-a.v);return o}
function renderPresets(){el("presets").innerHTML="";Object.keys(D.presets).forEach(n=>{const b=document.createElement("button");b.textContent=LENS[n]||n;b.className=(n===curPreset?"active":"");b.onclick=()=>{W=Object.assign({},D.presets[n]);curPreset=n;renderAll()};el("presets").appendChild(b)})}
function renderWeights(){const w=el("weights");w.innerHTML="";D.criteria.forEach(c=>{const r=document.createElement("div");r.className="wt";r.innerHTML=`<label>${c.label.replace(/ \(.*\)/,'')}</label><input type=range min=0 max=30 value=${W[c.key]} data-k="${c.key}"><span class="val">${W[c.key]}</span>`;w.appendChild(r)});w.querySelectorAll("input").forEach(i=>i.oninput=e=>{W[e.target.dataset.k]=+e.target.value;curPreset="Custom";renderAll()})}
function renderBars(){const t=totals();let h="";t.forEach((x,i)=>{h+=`<div class="bar-row ${i===0?'rank1':''}"><div class="top"><span class="name">${i+1}. ${x.u}</span><span class="score">${x.v.toFixed(1)}</span></div><div class="track"><div class="fill" style="width:${x.v.toFixed(1)}%"></div></div></div>`});el("bars").innerHTML=h}
function renderAll(){renderPresets();renderWeights();renderBars()}
renderAll();
</script>
</div></body></html>"""

out = (HTML.replace("%%CARDS%%", cards).replace("%%PHASES%%", phase_rows)
           .replace("%%PAYLOAD%%", payload).replace("%%WBFIG%%", wb)
           .replace("%%SLFIG%%", sl).replace("%%MPFIG%%", mp))
open("outputs/hacienda_overview.html", "w", encoding="utf-8").write(out)
print("Saved outputs/hacienda_overview.html", round(len(out) / 1000, 1), "KB")
