---
id: "pkis:technique:difference-in-differences"
aliases: []
title: "Difference-in-Differences"
knowledge_type: technique
also_type: []
domain: [causal-analysis]
tags: [did, parallel-trends, two-way-fixed-effects, panel-data, pre-trends, natural-experiment, policy-evaluation]
related_concepts: [[[identification-strategy]], [[parallel-trends]], [[fixed-effects-estimator]], [[selection-bias]], [[potential-outcomes-framework]]]
sources:
- "[[cunningham-causal-inference-mixtape]]"
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Difference-in-differences (DiD) identifies causal effects by comparing the pre-post change in outcomes for a treated group to the pre-post change for an untreated group; identification relies on the parallel trends assumption (treated and control groups would have had the same outcome trend absent treatment); typically implemented via two-way fixed effects regression.

## Reading Path
- [[cunningham-causal-inference-mixtape-ch10]] (unread) — primary treatment: 2×2 DiD, parallel trends, two-way FE, pre-trends test, Card-Krueger minimum wage application
- [[cunningham-causal-inference-mixtape-ch09]] (unread) — panel data prerequisites: fixed effects estimator, within transformation
