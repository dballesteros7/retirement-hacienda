"""Generate a self-contained interactive scorecard HTML from scorecard_data.json."""
import json
D=json.load(open("outputs/scorecard_data.json"))
payload=json.dumps(D,ensure_ascii=False)

HTML=r"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Hacienda Site Scorecard — interactive</title>
<style>
:root{--ink:#1a1d21;--mut:#5b6570;--line:#e3e7ec;--bg:#fff;--soft:#f6f8fa;--accent:#2c5f4f;--bar:#3a7bd5;--bar2:#6aa0e0}
*{box-sizing:border-box}body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;color:var(--ink);background:var(--soft);margin:0;line-height:1.5}
.wrap{max-width:1080px;margin:0 auto;padding:26px 20px 80px;background:var(--bg)}
h1{font-size:24px;margin:.1em 0 .1em}.sub{color:var(--mut);font-size:14px;margin-bottom:18px}
h2{font-size:16px;margin:26px 0 10px;border-bottom:2px solid var(--line);padding-bottom:5px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:26px}@media(max-width:820px){.grid{grid-template-columns:1fr}}
.presets{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px}
.presets button{font-size:12px;padding:6px 10px;border:1px solid var(--line);background:var(--soft);border-radius:16px;cursor:pointer}
.presets button.active{background:var(--accent);color:#fff;border-color:var(--accent)}
.wt{display:flex;align-items:center;gap:8px;margin:5px 0;font-size:13px}
.wt label{flex:0 0 168px;color:#2a2f34}.wt input{flex:1}.wt .val{flex:0 0 34px;text-align:right;color:var(--mut);font-variant-numeric:tabular-nums}
.bar-row{margin:9px 0}.bar-row .top{display:flex;justify-content:space-between;font-size:13px;margin-bottom:3px}
.bar-row .name{font-weight:600}.bar-row .score{font-variant-numeric:tabular-nums;color:var(--accent);font-weight:700}
.track{height:22px;background:var(--soft);border-radius:5px;overflow:hidden;border:1px solid var(--line)}
.fill{height:100%;background:linear-gradient(90deg,var(--bar),var(--bar2));transition:width .35s ease}
.rank1 .fill{background:linear-gradient(90deg,#2c7a4b,#43a86b)}
table{border-collapse:collapse;width:100%;font-size:12px;margin-top:8px}
th,td{border:1px solid var(--line);padding:5px 6px;text-align:center}
th{background:var(--accent);color:#fff;font-weight:600}th.c0,td.c0{text-align:left}
td.sc{cursor:help;font-variant-numeric:tabular-nums}
.note{font-size:12px;color:var(--mut);margin-top:14px;border-left:3px solid var(--line);padding-left:10px}
.hbar{display:inline-block;height:10px;border-radius:2px;vertical-align:middle}
</style></head><body><div class="wrap">
<h1>Retirement Hacienda — Interactive Site Scorecard</h1>
<div class="sub">Four options × ten criteria. Scores are evidence-anchored analyst judgments (Phase 0/1, all cited); water, seismic & accessibility criteria use the computed models. <b>Drag the weights</b> or pick a preset to re-rank live. Higher = better.</div>
<div class="grid">
 <div>
  <h2>Weighting</h2>
  <div class="presets" id="presets"></div>
  <div id="weights"></div>
  <div class="note">Weights auto-normalize to 100%. "Default" follows the brief's stated priority order (climate & water highest). The ranking is robust: the top option holds across every preset.</div>
 </div>
 <div>
  <h2>Ranking <span id="curpreset" style="font-weight:400;color:var(--mut);font-size:13px"></span></h2>
  <div id="bars"></div>
 </div>
</div>
<h2>Score detail (hover a cell for the rationale)</h2>
<div id="table"></div>
<div class="note">Method: weighted-sum MCDA. Terrain/landslide and some tenure scores rest on published SGC/EOT hazard data and documented events (no parcel-level DEM was available in this environment — flagged for a field/GIS survey). Water = radiation-aware Hargreaves aridity index + El Niño stress test; seismic = NSR-10 zone + computed distance to the GEM active-fault database; accessibility = computed distances + documented drive-times. This is decision-support, not an engineering or legal determination.</div>
<script>
const D=%%PAYLOAD%%;
let W=Object.assign({},D.presets["Default (brief priority)"]);
let curPreset="Default (brief priority)";
const el=id=>document.getElementById(id);
function totals(){const s=Object.values(W).reduce((a,b)=>a+b,0)||1;const out=D.units.map(u=>{let t=0;D.criteria.forEach(c=>t+=D.scores[u][c.key].v*W[c.key]);return{u,v:t/s}});out.sort((a,b)=>b.v-a.v);return out}
function renderPresets(){el("presets").innerHTML="";Object.keys(D.presets).forEach(name=>{const b=document.createElement("button");b.textContent=name;b.className=(name===curPreset?"active":"");b.onclick=()=>{W=Object.assign({},D.presets[name]);curPreset=name;renderAll()};el("presets").appendChild(b)})}
function renderWeights(){const w=el("weights");w.innerHTML="";D.criteria.forEach(c=>{const row=document.createElement("div");row.className="wt";row.innerHTML=`<label>${c.label}</label><input type=range min=0 max=30 value=${W[c.key]} data-k="${c.key}"><span class="val">${W[c.key]}</span>`;w.appendChild(row)});w.querySelectorAll("input").forEach(inp=>inp.oninput=e=>{W[e.target.dataset.k]=+e.target.value;curPreset="Custom";renderAll()})}
function renderBars(){const t=totals();const mx=Math.max(...t.map(x=>x.v));let h="";t.forEach((x,i)=>{h+=`<div class="bar-row ${i===0?'rank1':''}"><div class="top"><span class="name">${i+1}. ${x.u}</span><span class="score">${x.v.toFixed(1)}</span></div><div class="track"><div class="fill" style="width:${(x.v/100*100).toFixed(1)}%"></div></div></div>`});el("bars").innerHTML=h;el("curpreset").textContent="· "+curPreset}
function color(v){const g=Math.round(120+ (v/100)*(200-120)); if(v>=75)return"#2c7a4b"; if(v>=60)return"#5b9e5f"; if(v>=45)return"#e0a52e"; return"#c0603a"}
function renderTable(){let h="<table><tr><th class='c0'>Criterion</th><th>wt</th>";D.units.forEach(u=>h+=`<th>${u.replace(' (town belt)','')}</th>`);h+="</tr>";D.criteria.forEach(c=>{h+=`<tr><td class='c0'>${c.label}</td><td>${W[c.key]}</td>`;D.units.forEach(u=>{const s=D.scores[u][c.key];h+=`<td class='sc' style='background:${color(s.v)}22' title="${s.r.replace(/"/g,'&quot;')}">${s.v}</td>`});h+="</tr>"});const t=totals();h+="<tr><td class='c0'><b>Weighted total</b></td><td></td>";D.units.forEach(u=>{const v=t.find(x=>x.u===u).v;h+=`<td><b>${v.toFixed(1)}</b></td>`});h+="</tr></table>";el("table").innerHTML=h}
function renderAll(){renderPresets();renderWeights();renderBars();renderTable()}
renderAll();
</script></div></body></html>"""
open("outputs/scorecard_interactive.html","w",encoding="utf-8").write(HTML.replace("%%PAYLOAD%%",payload))
print("Saved outputs/scorecard_interactive.html")
