---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:technique:loo-cv
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch07
tags:
- cross-validation
- predictive-accuracy
- psis
- importance-sampling
- out-of-sample
- model-comparison
title: Bayesian Leave-One-Out Cross-Validation (LOO-CV)
understanding: 0
---

## Definition
The Bayesian special case of cross-validation in which the data are partitioned into n holdout sets of a single point each, yielding n leave-one-out posteriors p_post^(-i). The estimate of out-of-sample fit is lppd_loo-cv = Σ_i log p_post^(-i)(y_i), computed as Σ_i log( (1/S) Σ_s p(y_i|ω_i^s) ). Because each prediction conditions on only n−1 points, it slightly underestimates fit; a first-order bias correction b is available but usually negligible. An effective number of parameters follows as p_loo = lppd − lppd_loo-cv.

Naive LOO-CV requires refitting the model n times, which is prohibitive; in practice the n leave-one-out posteriors are approximated from a single full-posterior fit via Pareto-smoothed importance sampling (PSIS-LOO), making it about as cheap as WAIC but more robust under weak priors or influential observations. When even that fails, k-fold CV (e.g. k=10) is the fallback. LOO-CV differs from WAIC in the prediction task it targets: LOO-CV predicts p(ỹ_i | x̃_i, y_{-i}, x_{-i}) using only other data, whereas WAIC predicts at already-observed x-locations using all data — a difference that matters for flexible regression and hierarchical models. Gelman's stated preference among predictive-fit measures is PSIS-LOO-CV.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]