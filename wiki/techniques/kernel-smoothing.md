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
id: pkis:technique:kernel-smoothing
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch06
tags:
- nonparametric-regression
- local-averaging
- nadaraya-watson
- memory-based
- smoothing
title: Kernel Smoothing (Local Averaging)
understanding: 0
---

## Definition
A memory-based nonparametric regression technique that estimates f(x_0) = E(Y|X=x_0) by a locally weighted average of the responses, where weights are supplied by a kernel K_lambda(x_0, x_i) that decays smoothly with distance from the query point x_0. The canonical estimator is the Nadaraya-Watson kernel-weighted average f-hat(x_0) = [sum_i K_lambda(x_0,x_i) y_i] / [sum_i K_lambda(x_0,x_i)] (ESL 6.2). The kernel is parameterized by a bandwidth/window lambda that sets neighborhood width: K_lambda(x_0,x) = D(|x - x_0|/h_lambda(x_0)). Common shapes are the Epanechnikov quadratic D(t)=(3/4)(1-t^2) for |t|<=1 (compact support), the tri-cube (1-|t|^3)^3 (flat-topped, differentiable at support boundary), and the noncompact Gaussian density. Smoothing replaces the discontinuous k-NN moving average with a smoothly varying fit; bandwidth governs a bias-variance tradeoff (narrow = low bias/high variance; wide = high bias/low variance). CRITICAL: this 'kernel' is purely a localization/weighting device and is conceptually DISTINCT from the 'kernel trick' kernels that compute inner products in an implicit RKHS feature space (ESL is explicit on this distinction). Drawbacks: locally-weighted constant fits are badly biased at domain boundaries (kernel asymmetry) and in regions of uneven design density; this motivates local regression. Generalizes to R^p via radial kernels on a standardized/Mahalanobis metric but degrades quickly with dimension (curse of dimensionality).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]