---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:result:rubins-rules
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch18
tags:
- missing-data
- imputation
- variance-estimation
- survey-sampling
- uncertainty-quantification
title: Rubin's Rules for Combining Multiple Imputations
understanding: 0
---

## Definition
The standard moment-matching formulas for combining K complete-data analyses of multiply imputed datasets into a single inference for a scalar estimand omega. Let omega_hat_k and W_bar_{;k} be the complete-data point estimate and variance estimate from the kth imputed dataset, k = 1,...,K. The combined point estimate is the average omega_bar_K = (1/K) sum_k omega_hat_k. Its total variance decomposes into two components: the within-imputation variance W_bar_K = (1/K) sum_k W_bar_{;k} (the average of the complete-data variances) and the between-imputation variance B_K = (1/(K-1)) sum_k (omega_hat_k - omega_bar_K)^2 (the sample variance of the K point estimates, capturing extra uncertainty from not knowing the missing values). The total variance is T_K = W_bar_K + ((K+1)/K) B_K, where the (K+1)/K factor corrects for using a finite number of imputations. Interval estimates use a t reference distribution with degrees of freedom d.f. = (K-1)(1 + (K/(K+1)) (W_bar_K / B_K))^2, an approximation obtained by matching the first two moments of the variance estimate (a Satterthwaite-type approximation). The ratio of between- to total variance is an estimate of the fraction of missing information; when it is small, inference is insensitive to the missing-data model. These rules let analysts pool point-estimate-plus-standard-error output without access to the original imputation model; with full Bayesian simulation, combining is even simpler — one just mixes the posterior draws across imputations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]