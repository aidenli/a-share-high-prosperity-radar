# A-share High Prosperity Radar

A public-internet signal radar for A-share high-prosperity research.

It collects public signals, scores high-prosperity clues, tracks source health, merges story lines, and outputs static JSON/Markdown.

Important boundaries:

- No Tushare token.
- No secrets.
- No trading advice.
- Outputs are research leads only and must be validated locally with financial, valuation, market, and risk checks.

## Run locally

```bash
python scripts/collect_high_prosperity_signals.py \
  --config config/high_prosperity_sources.json \
  --output-dir data/processed/high_prosperity_radar \
  --report-dir reports/high_prosperity_radar
```

## GitHub Actions

`.github/workflows/update-high-prosperity-signals.yml` runs hourly via cron and can also be triggered manually.
