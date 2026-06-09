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
- statistical-learning
id: pkis:technique:backfitting-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- generalized-additive-model
related_concepts: []
sources:
- hastie-esl-ch09
tags:
- smoothing
- iterative-fitting
- coordinate-descent
title: Backfitting Algorithm
understanding: 0
---

## Definition
An iterative, modular procedure for fitting additive models Y = alpha + sum_j f_j(X_j) + epsilon. After initializing alpha-hat = ave(y_i) (which never changes) and f_j = 0, it cycles through the predictors, repeatedly updating each function f_j by applying its smoothing operator S_j to the partial residuals r_j = {y_i - alpha-hat - sum_{k != j} f_k(x_ik)} as a function of x_ij. One sweep updates every f_j in turn using the current estimates of the others; sweeps continue until the estimates stabilize (typically <20, often <10 cycles). For a large class of linear smoothers, backfitting is exactly a blockwise Gauss-Seidel iteration for solving the linear system whose block structure has identity diagonal and S_j off-diagonal blocks (estimating equations equivalent to the least-squares normal equations when the smoothers are orthogonal projections); for symmetric smoothers with eigenvalues in [0,1) it converges from any starting values. Any per-term fitting method can be plugged in by choosing an appropriate smoothing operator S_j (smoothing splines, local polynomial / kernel regression, parametric or Fourier fits, surface smoothers for interactions). For generalized additive models the same backfitting is performed inside a weighted IRLS / Newton-Raphson loop, with the weighted linear regression replaced by a weighted backfit.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[generalized-additive-model]] — prerequisite-of
[To be populated during integration]