---
id: "pkis:technique:synthetic-control"
aliases: []
title: "Synthetic Control"
knowledge_type: technique
also_type: []
domain: [causal-analysis]
tags: [synthetic-control, comparative-case-studies, donor-pool, placebo-tests, abadie, single-treated-unit, pre-treatment-fit]
related_concepts: [[[identification-strategy]], [[difference-in-differences]], [[matching-estimators]], [[potential-outcomes-framework]], [[counterfactuals]]]
sources:
- "[[cunningham-causal-inference-mixtape]]"
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

The synthetic control method (Abadie and Gardeazabal 2003) constructs a weighted combination of control units (the "donor pool") whose pre-treatment outcome trajectory matches the treated unit's; post-treatment divergence estimates the treatment effect; validity is assessed via in-space and in-time placebo tests across all donor units.

## Reading Path
- [[cunningham-causal-inference-mixtape-ch11]] (unread) — primary treatment: donor pool weighting, pre-treatment fit, placebo tests, California Prop 99 application
