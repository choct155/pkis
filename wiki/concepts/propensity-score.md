---
title: "Propensity Score"
knowledge_type: concept
also_type: []
domain: [causal-analysis]
tags: [propensity-score, matching, balancing-score, selection-on-observables, rosenbaum-rubin, logit]
related_concepts: [[[matching-estimators]], [[selection-bias]], [[potential-outcomes-framework]], [[average-treatment-effect]]]
sources: [[[cunningham-causal-inference-mixtape]]]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

The propensity score e(X) = P(D=1|X) is the conditional probability of treatment given observed covariates; Rosenbaum and Rubin (1983) showed it is a *balancing score* — conditioning on e(X) removes selection bias due to X, reducing high-dimensional covariate matching to one-dimensional score matching.

## Reading Path
- [[cunningham-causal-inference-mixtape-ch06]] (unread) — balancing score theorem, propensity score estimation via logit, overlap/common support requirement
