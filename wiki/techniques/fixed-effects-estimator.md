---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- causal-analysis
id: pkis:technique:fixed-effects-estimator
knowledge_type: technique
maturity: settled
related_concepts:
- '[[difference-in-differences]]'
- '[[identification-strategy]]'
- '[[selection-bias]]'
- '[[omitted-variable-bias]]'
sources:
- '[[cunningham-causal-inference-mixtape]]'
- cunningham-causal-inference-mixtape-ch09
- cunningham-causal-inference-mixtape-ch10
tags:
- panel-data
- within-estimator
- demeaning
- unobserved-heterogeneity
- two-way-fixed-effects
- first-differences
title: Fixed Effects Estimator
understanding: 0
---

The fixed effects estimator (within estimator) controls for time-invariant unobserved unit-level heterogeneity by demeaning each unit's observations, removing all variation between units and exploiting only within-unit variation over time; two-way fixed effects adds time dummies to also absorb period-specific shocks common to all units.

## Reading Path
- [[cunningham-causal-inference-mixtape-ch09]] (unread) — primary treatment: within transformation, first differences, two-way FE, Hausman test
- [[cunningham-causal-inference-mixtape-ch10]] (unread) — DiD as special case of two-way fixed effects