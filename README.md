# Retirement Hacienda

Site-selection research and decision-support for a shared retirement hacienda in the
Colombian central highlands (Cundiboyacense).

**Live site:** https://dballesteros7.github.io/retirement-hacienda/

| Page | What it is |
|---|---|
| [Overview](index.html) | Friendly summary + interactive scorecard |
| [Report](report.html) | Full site-selection analysis with sources |
| [Scorecard](scorecard.html) | Weighted multi-criteria model (adjustable weights) |
| [Map](map.html) | Candidate sectors, parcels, active faults, terrain |
| [Dossier](dossier.html) | Arcabuco-area property deep dive (9 parcels) |

## Working on this

Read **[CLAUDE.md](CLAUDE.md)** first — it has the current state, decisions, open items,
and the rebuild/publish workflow.

```bash
pip install -r requirements.txt
./build.sh          # regenerate all artifacts + refresh the site at repo root
git add -A && git commit -m "Update" && git push
```

Source lives in `code/` (pipeline), `data/` (geodata), `docs/` (research prose, the source
of truth), `logs/` (methods log). GitHub Pages serves only the root `*.html`.

> Decision-support, not legal, engineering, or financial advice.
