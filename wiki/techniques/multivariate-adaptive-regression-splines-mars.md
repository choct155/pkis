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
id: pkis:technique:multivariate-adaptive-regression-splines-mars
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch09
tags:
- nonparametric-regression
- basis-functions
- feature-selection
- high-dimensional
title: Multivariate Adaptive Regression Splines (MARS)
understanding: 0
---

## Definition
An adaptive regression procedure well suited to high-dimensional problems, viewable as a generalization of forward stepwise linear regression or a continuous-response modification of CART. MARS builds a model f(X) = beta_0 + sum_m beta_m h_m(X) from a dictionary C of piecewise-linear basis functions: for each input X_j and each observed value t it forms a reflected pair (X_j - t)_+ and (t - X_j)_+ (linear splines with a knot at t, zero over part of their range). The forward pass starts with the constant function and, at each stage, adds the product of a basis function already in the model with a reflected pair from C that most reduces training residual sum of squares (coefficients fit by least squares); products of hinge functions are nonzero only on local regions, so the surface is built up parsimoniously. The build is hierarchical (a high-order product enters only if a lower-order footprint is present) and each input appears at most once per product (no powers); an interaction-order cap (e.g. 2) aids interpretability, and a cap of 1 yields an additive model. A key computational trick updates each candidate knot fit in O(1) by sliding the knot leftward, making a whole input cost O(N). The overfit forward model is then pruned by backward deletion, choosing the size lambda that minimizes generalized cross-validation GCV(lambda) = sum_i (y_i - f_lambda(x_i))^2 / (1 - M(lambda)/N)^2, where the effective number of parameters M(lambda) = r + cK charges c=3 (c=2 for additive models) parameters per selected knot. Extends to classification via 0/1 coding, indicator-response multi-response regression, or the PolyMARS logistic variant.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]