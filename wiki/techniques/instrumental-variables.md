---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- causal-analysis
id: pkis:technique:instrumental-variables
knowledge_type: technique
maturity: settled
related_concepts:
- '[[identification-strategy]]'
- '[[local-average-treatment-effect]]'
- '[[selection-bias]]'
- '[[potential-outcomes-framework]]'
- '[[regression-discontinuity]]'
sources:
- '[[cunningham-causal-inference-mixtape]]'
tags:
- iv
- two-stage-least-squares
- 2sls
- exclusion-restriction
- relevance
- exogeneity
- late
- compliers
- natural-experiment
title: Instrumental Variables
understanding: 0
---

Instrumental variables (IV) identifies causal effects by using an instrument Z that is correlated with treatment D (relevance), independent of unobserved confounders (exogeneity/independence), and affects outcome Y only through D (exclusion restriction); two-stage least squares (2SLS) is the standard estimator, and under heterogeneous treatment effects the estimand is LATE for compliers.

## Reading Path
- [[cunningham-causal-inference-mixtape-ch08]] (unread) — primary treatment: three IV conditions, 2SLS mechanics, complier typology, quarter-of-birth and sibling-sex instruments
