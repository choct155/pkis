---
title: "Matching Estimators"
knowledge_type: technique
also_type: []
domain: [causal-analysis]
tags: [matching, propensity-score, covariate-balance, selection-on-observables, nearest-neighbor, subclassification, overlap]
related_concepts: [[[propensity-score]], [[identification-strategy]], [[selection-bias]], [[average-treatment-effect]], [[potential-outcomes-framework]]]
sources: [[[cunningham-causal-inference-mixtape]]]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Matching estimators identify causal effects under selection on observables (CIA: conditional independence assumption) by pairing treated and control units with similar observed covariates X, removing baseline differences; propensity score matching (Rosenbaum and Rubin 1983) reduces the dimensionality of matching to a single scalar, requiring overlap of propensity score support.

## Reading Path
- [[cunningham-causal-inference-mixtape-ch06]] (unread) — primary treatment: subclassification, exact matching, nearest-neighbor, propensity score methods, Lalonde-Dehejia-Wahba application
