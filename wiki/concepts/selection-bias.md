---
aliases: []
also_type: []
coverage: 2
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- causal-analysis
id: pkis:concept:selection-bias
knowledge_type: concept
maturity: settled
related_concepts:
- '[[potential-outcomes-framework]]'
- '[[average-treatment-effect]]'
- '[[confounding]]'
- '[[omitted-variable-bias]]'
- '[[identification-strategy]]'
sources:
- '[[cunningham-causal-inference-mixtape]]'
- '[[malkiel-emh-critics-2003]]'
tags:
- causal-inference
- selection-on-observables
- selection-on-unobservables
- confounding
- observational-studies
title: Selection Bias
understanding: 0
---

Selection bias is the component of a naive treatment-control comparison (E[Y|D=1] − E[Y|D=0]) that is not the ATE: it equals E[Y(0)|D=1] − E[Y(0)|D=0], the difference in *baseline* potential outcomes between treated and untreated units — present whenever treatment assignment is correlated with potential outcomes.

## Reading Path
- [[cunningham-causal-inference-mixtape-ch05]] (unread) — formal decomposition of naive comparison into ATE plus selection bias; why randomization solves the problem
