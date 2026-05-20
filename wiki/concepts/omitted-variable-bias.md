---
title: "Omitted Variable Bias"
knowledge_type: concept
also_type: []
domain: [causal-analysis]
tags: [regression, bias, confounding, endogeneity, ols, econometrics]
related_concepts: [[[selection-bias]], [[confounding]], [[identification-strategy]], [[collider-bias]], [[directed-graphical-models]]]
sources: [[[cunningham-causal-inference-mixtape]]]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Omitted variable bias (OVB) occurs when a regression excludes a variable that is correlated with both the included regressor of interest and the outcome; the bias equals the product of the true coefficient on the omitted variable and the regression coefficient of the omitted variable on the included regressor — in DAG terms, OVB is the consequence of leaving a back-door path open through a confounder.

## Reading Path
- [[cunningham-causal-inference-mixtape-ch03]] (unread) — algebraic derivation of OVB formula; Frisch-Waugh decomposition
- [[cunningham-causal-inference-mixtape-ch04]] (unread) — DAG interpretation of OVB as open backdoor path
