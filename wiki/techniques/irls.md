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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
- optimisation
id: pkis:technique:irls
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch04
- murphy-pml1-intro-ch10
tags:
- Newton-Raphson
- logistic-regression
- GLM
- weighted-least-squares
- canonical-link
- second-order-optimisation
title: Iterative Reweighted Least Squares (IRLS)
understanding: 0
---

## Definition
IRLS solves the maximum-likelihood problem for generalised linear models by applying the Newton–Raphson update

$$\mathbf{w}^{\text{new}} = (\mathbf{\Phi}^T\mathbf{R}\mathbf{\Phi})^{-1}\mathbf{\Phi}^T\mathbf{R}\mathbf{z}$$

where $\mathbf{z} = \mathbf{\Phi}\mathbf{w}^{\text{old}} - \mathbf{R}^{-1}(\mathbf{y}-\mathbf{t})$ is a vector of working responses and $\mathbf{R}$ is a diagonal weight matrix with elements $R_{nn} = y_n(1-y_n)$ (for logistic regression). At each iteration a weighted least-squares problem is solved, with weights depending on the current parameter estimates.

### Why it matters
IRLS is the standard batch optimiser for logistic regression and all GLMs with a canonical link. The error surface for logistic regression is strictly concave (positive-definite Hessian $\mathbf{H}=\mathbf{\Phi}^T\mathbf{R}\mathbf{\Phi}$), guaranteeing a unique global minimum and fast quadratic convergence. The same algorithm extends to multiclass softmax regression with a block-structured Hessian.

### Connection to GLM theory
IRLS is equivalent to Fisher scoring when the canonical link is used. The working response $z_n$ has the interpretation of a linearised target value in the space of the linear predictor $a = \mathbf{w}^T\boldsymbol{\phi}$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]