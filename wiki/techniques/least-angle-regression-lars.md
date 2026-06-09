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
- optimization
extends:
- subset-selection
id: pkis:technique:least-angle-regression-lars
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch03
tags:
- regression
- regularization
- variable-selection
- path-algorithm
- sparsity
- lasso
title: Least Angle Regression (LARS)
understanding: 0
uses:
- linear-regression
- effective-degrees-of-freedom
---

## Definition
A regression procedure (Efron et al., 2004) that can be seen as a 'democratic' version of forward-stepwise regression and that, with a small modification, computes the entire lasso solution path at the cost of a single least-squares fit. After standardizing predictors, LAR starts with residual r = y - ybar and all coefficients zero. It finds the predictor most correlated with the residual and moves its coefficient continuously toward its least-squares value; as soon as a second predictor 'catches up' in absolute correlation with the evolving residual, that variable joins the active set, and the active coefficients move together along their joint least-squares direction in a way that keeps their correlations tied and monotonically decreasing. The step direction at step k is delta_k = (X_A^T X_A)^{-1} X_A^T r_k, and the new fit direction u_k = X_A delta_k makes the smallest (and equal) angle with each active predictor (whence 'least angle'). Coefficient profiles are piecewise-linear, so exact step lengths are computed analytically without small increments. The Lasso modification (3.2a): if a non-zero coefficient hits zero, drop that variable from the active set and recompute the joint direction; this yields the exact lasso path. A second modification (FS_0 / non-negative least-squares constraint b_j s_j >= 0) reproduces infinitesimal forward-stagewise regression. After the kth LAR step the effective degrees of freedom of the fit is exactly k. Coordinate descent (Friedman et al.) is an alternative to LARS for computing lasso solutions on a grid of lambda.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[effective-degrees-of-freedom]] — uses: after k LAR steps the effective df is exactly k
- [[subset-selection]] — extends: a 'democratic' continuous relaxation of forward-stepwise/stagewise selection
- [[linear-regression]] — uses: moves coefficients along joint least-squares directions of the active set
[To be populated during integration]