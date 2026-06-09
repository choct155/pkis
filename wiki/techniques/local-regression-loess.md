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
id: pkis:technique:local-regression-loess
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch06
tags:
- nonparametric-regression
- local-polynomial
- loess
- weighted-least-squares
- equivalent-kernel
- boundary-correction
title: Local Regression (LOESS)
understanding: 0
---

## Definition
A nonparametric regression technique that, at each target point x_0, solves a separate kernel-weighted least-squares problem fitting a low-degree polynomial locally, then evaluates that fit only at x_0: min over alpha,beta of sum_i K_lambda(x_0,x_i)[y_i - alpha(x_0) - beta(x_0)x_i]^2 (ESL 6.7), with f-hat(x_0) = b(x_0)^T (B^T W B)^{-1} B^T W y = sum_i l_i(x_0) y_i. The estimate is linear in y; the combined weights l_i(x_0) are called the EQUIVALENT KERNEL, and stacking them gives a linear smoother matrix S_lambda with f-hat = S_lambda y. Fitting local lines (rather than the locally-constant Nadaraya-Watson average) automatically corrects boundary and design-density bias exactly to first order, a phenomenon dubbed 'automatic kernel carpentry' (the equivalent kernel self-adjusts so that bias has only degree >= 2 components). Higher-degree local polynomials remove higher-order bias (local quadratics correct 'trimming the hills and filling the valleys' curvature bias) at the cost of increased variance Var(f-hat(x_0)) = sigma^2 ||l(x_0)||^2, which grows with degree -- a bias-variance tradeoff in degree selection; asymptotically odd degrees dominate even ones. Effective degrees of freedom = trace(S_lambda) calibrates smoothing; leave-one-out CV, GCV, and C_p are available cheaply for linear smoothers. Generalizes to R^p (local hyperplanes) and underlies the loess/locfit software, which use triangulation + blending to cut the O(N) per-evaluation cost of these memory-based methods.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]