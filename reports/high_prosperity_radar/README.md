# A股高景气公开信号雷达 MVP

这个 MVP 借鉴 LearnPrompt/ai-news-radar 的思路，用公开互联网源生成“高景气线索层”。

定位：

- 只做公开信号收集、去重、评分、故事线合并、源健康统计。
- 不使用 Tushare token。
- 不输出真实买卖建议。
- 后续必须由本地 Tushare 财务/估值/行情系统验证。

运行：

```bash
cd /Users/xmr/.hermes/profiles/stock/home/stock_workspace
python scripts/collect_high_prosperity_signals.py
```

主要输出：

- `data/processed/high_prosperity_radar/latest-signals-all.json`
- `data/processed/high_prosperity_radar/latest-signals-24h.json`
- `data/processed/high_prosperity_radar/source-status.json`
- `data/processed/high_prosperity_radar/stories-merged.json`
- `data/processed/high_prosperity_radar/high_prosperity_signals.jsonl`
- `reports/high_prosperity_radar/latest.md`

GitHub Actions 模板：

- `.github/workflows/update-high-prosperity-signals.yml`

注意：当前模板只跑公开源，不配置 Tushare，不配置任何敏感密钥。
