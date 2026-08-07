"""Terrain / buildability from a real DEM — Arcabuco (cool highland) vs Moniquira (warm flank).

Answers the dossier's biggest open question: is the Moniquira flank actually the "gentlest, most
genuinely buildable land", or was that just a flattering set of listing photos?

Source: Copernicus GLO-30 DSM (ESA, 30 m), public AWS Open Data, tile cached under data/dem/.
Method: clip each AOI -> reproject to UTM 18N at 30 m -> slope from a 3x3 gradient ->
classify with the project's existing thresholds (config.SLOPE_BUILDABLE / SLOPE_MARGINAL).

IMPORTANT LIMIT: the listings are located at VEREDA level, not by coordinate or cadastral
boundary. So this is an AREA-level characterisation of the two tracks, NOT a per-parcel slope.
It tells you which flank is gentler on average; it cannot tell you how many flat hectares
parcel G or C actually has. That still needs the coordinates and a topographic survey.
To keep the comparison fair we also restrict to each track's PARCEL ELEVATION BAND, so we are
not scoring Arcabuco against its own paramo tops or Moniquira against its river gorges.
"""
import os, sys, math
import numpy as np, pandas as pd, requests, rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling
from rasterio.windows import from_bounds
sys.path.insert(0, 'code')
from config import AOIS, AOI_TILE, DEM_TILES, UTM18N, SLOPE_BUILDABLE, SLOPE_MARGINAL

TRACKS = {
    'arcabuco':  dict(label='Arcabuco / Gachantivá (cool highland)', band=(2000, 2750),
                      parcels='A, B, C, D  ~2,100-2,650 m'),
    'moniquira': dict(label='Moniquirá (warm flank)',                band=(1500, 2000),
                      parcels='E, G, H  ~1,700 m'),
}
DEM_DIR = 'data/dem'


def tile_path(key):
    os.makedirs(DEM_DIR, exist_ok=True)
    p = os.path.join(DEM_DIR, f'{key}.tif')
    if not os.path.exists(p):
        url = DEM_TILES[key]
        print(f'   downloading Copernicus GLO-30 tile {key} …', flush=True)
        with requests.get(url, stream=True, timeout=600) as r:
            r.raise_for_status()
            with open(p, 'wb') as f:
                for chunk in r.iter_content(1 << 20):
                    f.write(chunk)
        print(f'   cached {p} ({os.path.getsize(p)/1e6:.1f} MB)')
    return p


def aoi_slope(name):
    """Return (slope_deg, elev_m) arrays for one AOI, on a 30 m UTM grid, nodata removed."""
    lat0, lat1, lon0, lon1 = AOIS[name]
    with rasterio.open(tile_path(AOI_TILE[name])) as src:
        win = from_bounds(lon0, lat0, lon1, lat1, src.transform)
        dem = src.read(1, window=win, masked=True)
        tr = src.window_transform(win)
        dst_tr, w, h = calculate_default_transform(
            src.crs, UTM18N, dem.shape[1], dem.shape[0],
            *rasterio.windows.bounds(win, src.transform), resolution=30.0)
        out = np.empty((h, w), dtype='float32')
        reproject(source=dem.filled(np.nan), destination=out,
                  src_transform=tr, src_crs=src.crs,
                  dst_transform=dst_tr, dst_crs=UTM18N,
                  src_nodata=np.nan, dst_nodata=np.nan,
                  resampling=Resampling.bilinear)
    dzdy, dzdx = np.gradient(out, 30.0, 30.0)       # metres per metre, 30 m posting
    slope = np.degrees(np.arctan(np.hypot(dzdx, dzdy)))
    ok = np.isfinite(slope) & np.isfinite(out)
    return slope[ok], out[ok]


def stats(slope, elev, label, scope):
    n = slope.size
    return dict(track=label, scope=scope, cells=n, area_km2=round(n * 900 / 1e6, 1),
                elev_p50=round(float(np.median(elev))),
                slope_mean=round(float(slope.mean()), 1),
                slope_p50=round(float(np.median(slope)), 1),
                pct_buildable=round(100 * float((slope <= SLOPE_BUILDABLE).mean()), 1),
                pct_marginal=round(100 * float(((slope > SLOPE_BUILDABLE) &
                                                (slope <= SLOPE_MARGINAL)).mean()), 1),
                pct_steep=round(100 * float((slope > SLOPE_MARGINAL).mean()), 1))


rows, keep = [], {}
for name, meta in TRACKS.items():
    print(f'==> {meta["label"]}')
    slope, elev = aoi_slope(name)
    rows.append(stats(slope, elev, meta['label'], 'whole AOI'))
    lo, hi = meta['band']
    m = (elev >= lo) & (elev <= hi)
    rows.append(stats(slope[m], elev[m], meta['label'], f'parcel band {lo}-{hi} m'))
    keep[name] = (slope[m], meta)

df = pd.DataFrame(rows)
df.to_csv('outputs/slope_summary.csv', index=False)
pd.set_option('display.width', 200, 'display.max_columns', 20)
print('\n' + df.to_string(index=False))

band = df[df.scope.str.startswith('parcel band')].reset_index(drop=True)
a, m = band.iloc[0], band.iloc[1]
print(f'\nIn the band where the parcels actually sit, gentle ground (<={SLOPE_BUILDABLE:.0f}°) is '
      f'{m.pct_buildable:.1f}% of Moniquirá vs {a.pct_buildable:.1f}% of Arcabuco '
      f'({m.pct_buildable/max(a.pct_buildable,1e-9):.1f}x); '
      f'median slope {m.slope_p50:.1f}° vs {a.slope_p50:.1f}°.')

# --- figure -------------------------------------------------------------------------------
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.0))
bins = np.arange(0, 61, 2)
for ax, (name, (slope, meta)) in zip(axes, keep.items()):
    ax.hist(slope, bins=bins, color='#3a7bd5', alpha=.8, density=True)
    ax.axvline(SLOPE_BUILDABLE, color='#2c7a4b', lw=2, label=f'{SLOPE_BUILDABLE:.0f}° buildable')
    ax.axvline(SLOPE_MARGINAL, color='#c0392b', lw=2, ls='--', label=f'{SLOPE_MARGINAL:.0f}° hard')
    pb = 100 * float((slope <= SLOPE_BUILDABLE).mean())
    ax.set_title(f'{meta["label"]}\n{meta["parcels"]} · {pb:.0f}% of land ≤{SLOPE_BUILDABLE:.0f}°',
                 fontsize=10)
    ax.set_xlabel('slope (degrees)'); ax.grid(alpha=.25); ax.legend(fontsize=8)
axes[0].set_ylabel('share of cells')
plt.suptitle('Terrain in the parcel elevation band — Copernicus GLO-30, 30 m '
             '(area-level, not per-parcel)', fontsize=11, y=1.02)
plt.tight_layout(); plt.savefig('outputs/fig_slope.png', dpi=130, bbox_inches='tight')
print('\nSaved outputs/slope_summary.csv + fig_slope.png')
