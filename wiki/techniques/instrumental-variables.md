---
id: "pkis:technique:instrumental-variables"
aliases: []
title: "Instrumental Variables"
knowledge_type: technique
also_type: []
domain: [causal-analysis]
tags: [iv, two-stage-least-squares, 2sls, exclusion-restriction, relevance, exogeneity, late, compliers, natural-experiment]
related_concepts: [[[identification-strategy]], [[local-average-treatment-effect]], [[selection-bias]], [[potential-outcomes-framework]], [[regression-discontinuity]]]
sources:
- "[[cunningham-causal-inference-mixtape]]"
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Instrumental variables (IV) identifies causal effects by using an instrument Z that is correlated with treatment D (relevance), independent of unobserved confounders (exogeneity/independence), and affects outcome Y only through D (exclusion restriction); two-stage least squares (2SLS) is the standard estimator, and under heterogeneous treatment effects the estimand is LATE for compliers.

## Reading Path
- [[cunningham-causal-inference-mixtape-ch08]] (unread) — primary treatment: three IV conditions, 2SLS mechanics, complier typology, quarter-of-birth and sibling-sex instruments
