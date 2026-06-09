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
id: pkis:technique:principal-curves-surfaces
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch14
tags:
- unsupervised-learning
- dimension-reduction
- manifold-learning
- nonlinear-pca
title: Principal Curves and Surfaces
understanding: 0
---

## Definition
A nonlinear generalization of the principal-component line: a smooth one-dimensional curve f(λ) (or higher-dimensional surface) in ℝ^p that passes through the "middle" of a distribution. The defining **self-consistency** property is f(λ) = E(X | λ_f(X) = λ) — each point of the curve is the average of all data that project orthogonally onto it (λ_f(x) being the arc-length location of x's closest point). Estimation alternates two steps until convergence: (a) for fixed projection indices, re-estimate each coordinate function f̂_j(λ) by smoothing X_j against arc-length (a scatterplot smoother, enforcing self-consistency); (b) for the fixed curve, re-project each data point to its nearest point. Initialized at the first principal component, it converges to that component when the smoother is linear least squares (equivalent to the power method for the top eigenvector). Related concepts: **principal points** (the k self-consistent prototypes minimizing expected distance — the distributional analog of K-means centroids), with principal curves being k=∞ principal points constrained to a smooth curve. Principal surfaces nearly coincide with the batch SOM when a kernel smoother is used, but parameterize the whole manifold rather than sharing discrete prototypes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]