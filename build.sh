#!/usr/bin/env bash
# Rebuild every artifact, then refresh the published site at the repo root.
# Usage: ./build.sh          (from the repo root)
set -euo pipefail
cd "$(dirname "$0")"

echo "==> 1/10 water balance (Thornthwaite + Hargreaves, El Nino stress test)"
python3 code/water_balance.py

echo "==> 2/10 seismic fault distances + accessibility metrics"
python3 code/geo_metrics.py

echo "==> 3/10 DEM slope / buildability (Copernicus GLO-30)"
python3 code/slope_analysis.py

echo "==> 4/10 weighted scorecard + sensitivity"
python3 code/scorecard.py

echo "==> 5/10 interactive scorecard HTML"
python3 code/build_scorecard_html.py

echo "==> 6/10 interactive Leaflet map"
python3 code/build_map.py

echo "==> 7/10 final report HTML (from docs/final_report.md)"
python3 code/build_report_html.py

echo "==> 8/10 friend-facing overview"
python3 code/build_overview.py

echo "==> 9/10 Arcabuco + Moniquirá property dossier"
python3 code/build_dossier2.py

echo "==> 10/10 assemble site bundle"
python3 code/build_site2.py

echo "==> publishing site files to repo root"
cp outputs/site/index.html outputs/site/report.html outputs/site/scorecard.html \
   outputs/site/map.html outputs/site/dossier.html .

echo
echo "Done. Site refreshed at repo root:"
ls -lh index.html report.html scorecard.html map.html dossier.html | awk '{print "   "$5"\t"$9}'
echo
echo "Publish with:  git add -A && git commit -m 'Update site' && git push"
echo "Live at:       https://dballesteros7.github.io/retirement-hacienda/"
