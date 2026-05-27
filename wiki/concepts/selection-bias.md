---
id: "pkis:concept:selection-bias"
aliases: []
title: "Selection Bias"
knowledge_type: concept
also_type: []
domain: [causal-analysis]
tags: [causal-inference, selection-on-observables, selection-on-unobservables, confounding, observational-studies]
related_concepts: [[[potential-outcomes-framework]], [[average-treatment-effect]], [[confounding]], [[omitted-variable-bias]], [[identification-strategy]]]
sources: [[[cunningham-causal-inference-mixtape]], malkiel-emh-critics-2003]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

Selection bias is the component of a naive treatment-control comparison (E[Y|D=1] − E[Y|D=0]) that is not the ATE: it equals E[Y(0)|D=1] − E[Y(0)|D=0], the difference in *baseline* potential outcomes between treated and untreated units — present whenever treatment assignment is correlated with potential outcomes.

## Reading Path
- [[cunningham-causal-inference-mixtape-ch05]] (unread) — formal decomposition of naive comparison into ATE plus selection bias; why randomization solves the problem
