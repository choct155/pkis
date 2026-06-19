---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- causal-analysis
id: pkis:concept:average-treatment-effect
knowledge_type: concept
maturity: settled
related_concepts:
- - - potential-outcomes-framework
- - - selection-bias
- - - local-average-treatment-effect
- - - counterfactuals
sources:
- "[[cunningham-causal-inference-mixtape]]"
tags:
- causal-inference
- ate
- att
- atu
- late
- estimand
- potential-outcomes
title: Average Treatment Effect
understanding: 0
uses:
- linear-regression
---

The average treatment effect (ATE = E[Y(1)−Y(0)]) is the mean causal effect over the full population; ATT (average treatment effect on the treated) averages only over units that received treatment; ATU (on the untreated) averages only over controls — these three estimands differ when effects are heterogeneous and when treatment assignment is non-random.

## Reading Path
- [[cunningham-causal-inference-mixtape-ch05]] (unread) — defines ATE, ATT, ATU and explains when each is the relevant estimand; selection bias decomposition

## Connections
- [[linear-regression]] — uses