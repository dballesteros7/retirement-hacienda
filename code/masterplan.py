"""Community masterplan + build budget — one casa comunal and three satellite houses.

The group's shape: three households, each with a private house, around one shared central
building (kitchen, dining, living, guest rooms, laundry, workshop). This costs that programme on
the three shortlisted parcels using 2026 Colombian unit rates, and draws an indicative site plan
that respects the constraints the analysis actually found: gentle-slope siting, a 30 m ronda
hidrica setback, gravity-fed water from an uphill tank, and septic fields placed away from the
watercourse (which matters more than usual on G, where the photos show limestone karst).

EVERYTHING HERE IS PLANNING-LEVEL. Unit rates are national/regional 2026 published figures, not
quotes. Rural work varies enormously with access and ground conditions. Treat the totals as a
budget envelope for a conversation, not an estimate to commit to. Sources in logs/methods_log.md.
"""
import sys, json
import numpy as np, pandas as pd
sys.path.insert(0, 'code')

M = 1_000_000  # COP millions
# EUR conversion is for the group's intuition only. Published 2026 EUR/COP quotes disagree
# (aggregators show a 2026 average ~4,300 against a stated low of ~4,157 and high of ~4,442,
# and one "live" figure well outside that band). We use the 2026 AVERAGE and label it as such.
# COP is the currency the transaction actually happens in — treat EUR as a sense-check only.
EURCOP = 4300

# --- programme -------------------------------------------------------------------------------
CASA_COMUNAL_M2 = 160     # shared kitchen/dining/living + 2 guest rooms + laundry + workshop
SATELLITE_M2    = 120     # private house per household (raised from 80 on 2026-08-08 — 80 was
                          # too small for a home you actually retire into, not a guest cabin)
N_SATELLITES    = 3
HOUSEHOLDS      = 3
BUILT_M2 = CASA_COMUNAL_M2 + N_SATELLITES * SATELLITE_M2

# --- 2026 unit rates (COP). See methods log for sources + access dates -----------------------
RATES = {
    'build_finished_m2':   3_500_000,   # mid-high campestre, finished. Published range 3.1-3.8 M/m2
    'build_shell_m2':      2_050_000,   # obra gris only. Published range 1.85-2.25 M/m2
    'rural_access_uplift': 0.05,        # material transport / access. Published range 2-8%
    'design_licence_pct':  0.05,        # architect + licencia de construccion, share of build
    'potabiliser':        13_000_000,   # 400-500 L/h plant for a small complex. Range 11-15.5 M
    'potab_maintenance':     600_000,   # per year
    'water_storage_dist':  8_000_000,   # tanks, pump, gravity distribution to 4 buildings
    'well_per_m':            200_000,   # drilling. Published range 150-250k per metre
    'well_depth_m':               60,
    'septic_each':         7_000_000,   # pozo septico + field. Published range 5-10 M
    'solar_kwp':           4_200_000,   # per kWp installed. Published range 3.5-5.0 M
    'solar_kwp_size':              5,
    'battery_5kwh':       11_000_000,   # lithium 5 kWh. Published range 8-14 M
    'grid_extension':     15_000_000,   # EBSA MV extension + transformer — ESTIMATE, get a quote
    'starlink_kit':        1_599_000,
    'starlink_month':        250_000,
    'internal_roads':     25_000_000,   # ~400 m of internal track, gentle ground
    'earthworks_pad':      5_000_000,   # per building pad on gentle ground (steep: 10-50 M total)
    'fencing':            20_000_000,   # perimeter, if not already fenced
    'txn_cost_pct':           0.025,    # notarial + registro + beneficencia, buyer side (2.15-2.5%)
}

# --- the three parcels actually worth costing ------------------------------------------------
PARCELS = {
 'H': dict(label='H · Moniquirá, geotech lote', ha=8.0, ask=720*M, fenced=True, karst=False,
           grid='easy', water='aljibe + pozo, geotech study done', slope='gentle ridge',
           note='Best building land found. Study handed over. Listing says negotiable.'),
 'G': dict(label='G · Moniquirá, Papayal', ha=9.11, ask=390*M, fenced=False, karst=True,
           grid='near', water='quebrada + vereda aqueduct (IRCA Riesgo Alto)', slope='flat vega + steep hills',
           note='Cheapest usable land. Karst: foundations, septic siting and groundwater need specialist input.'),
 'N': dict(label='N · Moniquirá, finca panelera', ha=40.96, ask=1700*M, fenced=False, karst=False,
           grid='on site', water='acueducto veredal + own aljibes', slope='semi-flat',
           note='Above the 9.38 ha UAF, so lawfully divisible. Arrives with 2 houses + trapiche.'),
}


def budget(p, finish='finished'):
    r = RATES
    rate = r['build_finished_m2'] if finish == 'finished' else r['build_shell_m2']
    build = BUILT_M2 * rate * (1 + r['rural_access_uplift'])
    rows = [
        ('Land (asking price)',            p['ask']),
        ('Purchase costs (notary/registry/beneficencia, 2.5%)', p['ask'] * r['txn_cost_pct']),
        (f'Construction — {BUILT_M2} m² ({finish})', build),
        ('Design + licencia de construcción', build * r['design_licence_pct']),
        ('Building pads / earthworks',      (1 + N_SATELLITES) * r['earthworks_pad']),
        ('Internal access track',           r['internal_roads']),
        ('Perimeter fencing',               0 if p['fenced'] else r['fencing']),
        ('Water — potabilisation plant',    r['potabiliser']),
        ('Water — storage, pump, distribution', r['water_storage_dist']),
        ('Water — well/aljibe deepening',   0 if 'aljibe' in p['water'] else r['well_per_m'] * r['well_depth_m']),
        ('Septic — 4 systems',              (1 + N_SATELLITES) * r['septic_each']),
        ('Grid connection (EBSA)',          0 if p['grid'] == 'on site' else r['grid_extension']),
        ('Solar PV 5 kWp + 5 kWh battery',  r['solar_kwp'] * r['solar_kwp_size'] + r['battery_5kwh']),
        ('Starlink hardware',               r['starlink_kit']),
    ]
    if p['karst']:
        rows.append(('Karst contingency — geotech, sealed septic, foundations', 45 * M))
    sub = sum(v for _, v in rows)
    rows.append(('Contingency 15%', sub * 0.15))
    return pd.DataFrame(rows, columns=['item', 'cop'])


records = []
for k, p in PARCELS.items():
    df = budget(p)
    total = df.cop.sum()
    records.append(dict(parcel=k, label=p['label'], ha=p['ha'], ask_M=p['ask'] / M,
                        total_M=round(total / M), per_household_M=round(total / HOUSEHOLDS / M),
                        cop_per_m2_land=round(p['ask'] / (p['ha'] * 10_000)),
                        note=p['note']))
    df.assign(parcel=k).to_csv(f'outputs/masterplan_budget_{k}.csv', index=False)

summary = pd.DataFrame(records)
summary.to_csv('outputs/masterplan_summary.csv', index=False)
pd.set_option('display.width', 200, 'display.max_columns', 20)
print(summary[['parcel', 'ha', 'ask_M', 'total_M', 'per_household_M', 'cop_per_m2_land']].to_string(index=False))

hb = budget(PARCELS['H'])
tot = hb.cop.sum()
print(f"\nProgramme: casa comunal {CASA_COMUNAL_M2} m² + {N_SATELLITES} × {SATELLITE_M2} m² "
      f"= {BUILT_M2} m² built, {HOUSEHOLDS} households.")
print(f"On H, all-in ≈ COP {tot/M:,.0f} M (≈ EUR {tot/EURCOP:,.0f}) "
      f"-> ≈ COP {tot/HOUSEHOLDS/M:,.0f} M (≈ EUR {tot/HOUSEHOLDS/EURCOP:,.0f}) per household.")

# --- phasing: what it takes to be ON the land, sleeping there, before the satellites ---------
r = RATES
phase1_build = (CASA_COMUNAL_M2 + SATELLITE_M2) * r['build_finished_m2'] * (1 + r['rural_access_uplift'])
PHASES = [
 ('Phase 0 — buy and secure',
  PARCELS['H']['ask'] + PARCELS['H']['ask'] * r['txn_cost_pct'] + 25 * M,
  'Land, purchase costs, survey + geotech review, title work, SAS set-up.'),
 ('Phase 1 — water, power, access',
  r['potabiliser'] + r['water_storage_dist'] + r['grid_extension'] + r['internal_roads']
  + r['starlink_kit'] + 2 * r['septic_each'] + 2 * r['earthworks_pad'],
  'Potabilisation and storage, grid connection, internal track, Starlink, two pads and septics.'),
 ('Phase 2 — casa comunal + first satellite',
  phase1_build * (1 + r['design_licence_pct']),
  f'{CASA_COMUNAL_M2 + SATELLITE_M2} m² finished. The group can now live on site while the rest is built.'),
 ('Phase 3 — remaining two satellites',
  2 * SATELLITE_M2 * r['build_finished_m2'] * (1 + r['rural_access_uplift']) * (1 + r['design_licence_pct'])
  + 2 * r['septic_each'] + 2 * r['earthworks_pad']
  + r['solar_kwp'] * r['solar_kwp_size'] + r['battery_5kwh'],
  'Two more houses, their septics and pads, plus solar + battery once loads are known.'),
]
_sub = sum(v for _, v, _ in PHASES)
PHASES.append(('Contingency 15% (held across all phases)', _sub * 0.15,
               'Rural build overruns are normal. Hold this, do not spend it early.'))
ph = pd.DataFrame([(n, round(v / M), d) for n, v, d in PHASES],
                  columns=['phase', 'cop_M', 'what'])
ph['cum_M'] = ph.cop_M.cumsum()
ph['per_household_M'] = (ph.cop_M / HOUSEHOLDS).round()
ph.to_csv('outputs/masterplan_phases.csv', index=False)
print("\nPhased on H (each phase is a stopping point, not a commitment to the next):")
print(ph[['phase', 'cop_M', 'cum_M', 'per_household_M']].to_string(index=False))
_live = ph.cum_M.iloc[2] * 1.15   # carry the same contingency against the first three phases
print(f"\nPhase 0+1+2 gets you living on the land for COP {_live:,.0f} M with contingency "
      f"(≈ COP {_live/HOUSEHOLDS:,.0f} M / EUR {_live*M/HOUSEHOLDS/EURCOP:,.0f} each) — "
      f"before the last two houses exist.")

# running costs
run = {'Potabiliser maintenance': RATES['potab_maintenance'],
       'Starlink': RATES['starlink_month'] * 12,
       'Predial (property tax, ~0.5% of avalúo — indicative)': PARCELS['H']['ask'] * 0.005,
       'Caretaker (mayordomo), part-time — indicative': 1_600_000 * 12}
print("\nIndicative annual running cost, parcel H:")
for k, v in run.items():
    print(f"  {k:58s} COP {v/M:6.1f} M")
print(f"  {'TOTAL':58s} COP {sum(run.values())/M:6.1f} M/yr  "
      f"({sum(run.values())/HOUSEHOLDS/M:.1f} M per household)")
json.dump({k: v for k, v in run.items()}, open('outputs/masterplan_running.json', 'w'))

# headline figures consumed by code/build_overview.py — single source of truth for the page
HEAD = dict(
    casa_comunal_m2=CASA_COMUNAL_M2, satellite_m2=SATELLITE_M2, n_satellites=N_SATELLITES,
    built_m2=BUILT_M2, households=HOUSEHOLDS, eurcop=EURCOP,
    total_M=round(tot / M), per_household_M=round(tot / HOUSEHOLDS / M),
    per_household_eur=round(tot / HOUSEHOLDS / EURCOP),
    live_after_phase2_M=round(_live), live_after_phase2_each_M=round(_live / HOUSEHOLDS),
    live_after_phase2_each_eur=round(_live * M / HOUSEHOLDS / EURCOP),
    running_M=round(sum(run.values()) / M, 1),
    running_each_M=round(sum(run.values()) / HOUSEHOLDS / M, 1),
    build_M={k: round(budget(v).cop.sum() / M) for k, v in PARCELS.items()},
    land_M={k: round(v['ask'] / M) for k, v in PARCELS.items()},
)
json.dump(HEAD, open('outputs/masterplan_headline.json', 'w'), indent=1)

# --- figures ---------------------------------------------------------------------------------
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, FancyBboxPatch

fig = plt.figure(figsize=(13.5, 5.6))
ax = fig.add_subplot(1, 2, 1)

# indicative site plan on a gentle ridge, ~4 ha of the parcel shown
ax.set_xlim(0, 400); ax.set_ylim(0, 340); ax.set_aspect('equal')
ax.add_patch(Polygon([(0, 0), (400, 0), (400, 340), (0, 340)], fc='#eef4e8', ec='none'))

# quebrada along the east edge + its 30 m ronda hidrica no-build strip
qx = [345, 352, 340, 356, 344, 358]
qy = [0, 70, 140, 210, 280, 340]
ax.plot(qx, qy, color='#3a7bd5', lw=2.6, zorder=3)
ax.add_patch(Polygon([(315, 0), (400, 0), (400, 340), (315, 340)], fc='#3a7bd5', alpha=.10, ec='none'))
ax.text(358, 20, 'quebrada', color='#2c5f8a', fontsize=8, rotation=90)
ax.text(322, 150, '30 m ronda hídrica — no build', color='#2c5f8a', fontsize=7.5, rotation=90)

# forest edge
ax.add_patch(Polygon([(0, 268), (400, 300), (400, 340), (0, 340)], fc='#5b7a5b', alpha=.28, ec='none'))
ax.text(20, 312, 'existing forest / shade trees — keep', fontsize=7.5, color='#3f5f3f')

# access track
ax.plot([0, 60, 130, 185], [40, 55, 95, 150], color='#a08050', lw=3.4, zorder=2)
ax.text(6, 26, 'access track from vereda road', fontsize=7.5, color='#7a6038')

# water tank uphill, gravity feed
ax.add_patch(Circle((120, 250), 13, fc='#3a7bd5', ec='w', lw=1.6, zorder=5))
ax.text(120, 272, 'tank + potabiliser\n(gravity feed)', ha='center', fontsize=7.2, color='#2c5f8a')
for tx, ty in [(185, 156), (91, 116), (235, 100), (249, 212)]:
    ax.plot([120, tx], [250, ty], color='#3a7bd5', lw=.8, ls=':', zorder=1)

# casa comunal, centre
ax.add_patch(FancyBboxPatch((165, 138), 40, 34, boxstyle='round,pad=3',
                            fc='#b5613a', ec='w', lw=2, zorder=6))
ax.text(185, 130, f'CASA COMUNAL · {CASA_COMUNAL_M2} m²', ha='center', va='top', fontsize=8,
        weight='bold', color='#7a3d22', zorder=7)

# three satellites at privacy distance; footprint drawn proportional to floor area
sats = [((76, 98), f'casa 1 · {SATELLITE_M2} m²'), ((220, 82), f'casa 2 · {SATELLITE_M2} m²'),
        ((234, 194), f'casa 3 · {SATELLITE_M2} m²')]
_w = 26 * (SATELLITE_M2 / 80) ** 0.5
for (sx, sy), lbl in sats:
    ax.add_patch(FancyBboxPatch((sx, sy), _w, _w * 0.85, boxstyle='round,pad=2.5',
                                fc='#5b7a5b', ec='w', lw=1.8, zorder=6))
    ax.text(sx + _w / 2, sy - 7, lbl, ha='center', va='top', fontsize=7.4, color='#3f5f3f', zorder=7)
    ax.plot([sx + _w / 2, 185], [sy + _w * 0.42, 155], color='#c9b79c', lw=1.1, ls='--', zorder=1)

# septic fields, downhill and well clear of the quebrada
for ex, ey in [(60, 150), (255, 40), (270, 245)]:
    ax.add_patch(Circle((ex, ey), 9, fc='#c9a227', alpha=.55, ec='none', zorder=4))
ax.text(60, 165, 'septic fields — sited away\nfrom the watercourse', fontsize=6.8, color='#8a6d15')

# huerta / orchard
ax.add_patch(Polygon([(120, 26), (250, 26), (250, 60), (120, 60)], fc='#8fbf6f', alpha=.4, ec='none'))
ax.text(185, 43, 'huerta / frutales', ha='center', va='center', fontsize=7.4, color='#456b35')

ax.set_title('Indicative layout — casa comunal + 3 satellites\n(~4 ha of a gentle ridge; '
             'spacing ≈ 90–140 m for privacy)', fontsize=10)
ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values():
    s.set_edgecolor('#d8d0c4')

# budget comparison
ax2 = fig.add_subplot(1, 2, 2)
lbls = [f"{r.parcel} · {r.ha:.0f} ha" for r in summary.itertuples()]
land = [r.ask_M for r in summary.itertuples()]
rest = [r.total_M - r.ask_M for r in summary.itertuples()]
x = np.arange(len(lbls))
ax2.bar(x, land, .55, label='land (asking)', color='#b5613a')
ax2.bar(x, rest, .55, bottom=land, label='build + water + power + fees', color='#5b7a5b')
for i, r in enumerate(summary.itertuples()):
    ax2.text(i, r.total_M + 60, f"{r.total_M:,.0f} M\n({r.per_household_M:,.0f} M each)",
             ha='center', fontsize=8.5, weight='bold')
ax2.set_xticks(x); ax2.set_xticklabels(lbls, fontsize=9)
ax2.set_ylabel('COP millions'); ax2.legend(fontsize=8.5, loc='upper left')
ax2.set_title(f'All-in to a finished community of {BUILT_M2} m²\n'
              f'({HOUSEHOLDS} households, 2026 rates, ±30%)', fontsize=10)
ax2.grid(axis='y', alpha=.25); ax2.set_ylim(0, max(summary.total_M) * 1.28)

plt.tight_layout()
plt.savefig('outputs/fig_masterplan.png', dpi=130, bbox_inches='tight')
print('\nSaved outputs/masterplan_summary.csv, masterplan_budget_*.csv, fig_masterplan.png')
