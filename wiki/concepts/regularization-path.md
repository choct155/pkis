---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine learning
id: pkis:concept:regularization-path
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch11
tags:
- lasso
- ridge
- model selection
- sparsity
- lambda
title: Regularisation Path
understanding: 0
uses:
- lasso-regression
- ridge-regression
- least-angle-regression-lars
- cross-validation
---

## Definition
The regularisation path is the curve $\{\hat{\mathbf{w}}(\lambda) : \lambda \in [0, \lambda_\max]\}$ traced by the MAP estimator as the penalty strength $\lambda$ varies from 0 (OLS) to $\lambda_\max$ (all-zeros solution).

It provides a continuous view of how sparsity or shrinkage evolves with regularisation and is used to select $\lambda$ via cross-validation or empirical Bayes.

### Why it matters
For lasso, the regularisation path is piecewise linear in $\lambda$, meaning the active set of non-zero coefficients changes at finitely many breakpoints that can be computed exactly (LARS algorithm). For ridge the path is smooth. Plotting coefficient values against $\lambda$ (or the $\ell_1$ norm bound $B$) reveals which features enter the model first and which are most robust, making the path a diagnostic tool for feature selection.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[cross-validation]] — uses
- [[least-angle-regression-lars]] — uses
- [[ridge-regression]] — uses
- [[lasso-regression]] — uses
[To be populated during integration]