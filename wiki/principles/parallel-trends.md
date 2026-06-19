---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- causal-analysis
id: pkis:principle:parallel-trends
knowledge_type: principle
maturity: settled
related_concepts:
- '[[difference-in-differences]]'
- '[[potential-outcomes-framework]]'
- '[[selection-bias]]'
- '[[identification-strategy]]'
sources:
- '[[cunningham-causal-inference-mixtape]]'
tags:
- difference-in-differences
- did
- identifying-assumption
- counterfactual
- panel-data
- pre-trends-test
title: Parallel Trends
understanding: 0
---

The parallel trends assumption states that, absent treatment, the treated group's outcome would have followed the same trend as the control group's outcome — it is the key identifying assumption for difference-in-differences, is fundamentally untestable for the post-treatment period, and is typically supported by pre-treatment trend tests.

## Reading Path
- [[cunningham-causal-inference-mixtape-ch10]] (unread) — formal statement, pre-trends testing as partial validation, violations from anticipation effects and heterogeneous timing
