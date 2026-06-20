---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- causal-analysis
id: pkis:technique:synthetic-control
knowledge_type: technique
maturity: settled
related_concepts:
- '[[identification-strategy]]'
- '[[difference-in-differences]]'
- '[[matching-estimators]]'
- '[[potential-outcomes-framework]]'
- '[[counterfactuals]]'
sources:
- '[[cunningham-causal-inference-mixtape]]'
- cunningham-causal-inference-mixtape-ch11
tags:
- synthetic-control
- comparative-case-studies
- donor-pool
- placebo-tests
- abadie
- single-treated-unit
- pre-treatment-fit
title: Synthetic Control
understanding: 0
---

The synthetic control method (Abadie and Gardeazabal 2003) constructs a weighted combination of control units (the "donor pool") whose pre-treatment outcome trajectory matches the treated unit's; post-treatment divergence estimates the treatment effect; validity is assessed via in-space and in-time placebo tests across all donor units.

## Reading Path
- [[cunningham-causal-inference-mixtape-ch11]] (unread) — primary treatment: donor pool weighting, pre-treatment fit, placebo tests, California Prop 99 application