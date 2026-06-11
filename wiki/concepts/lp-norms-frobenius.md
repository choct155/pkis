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
- linear-algebra
- machine-learning
id: pkis:concept:lp-norms-frobenius
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch02
tags:
- norm
- L1
- L2
- Frobenius
- sparsity
- regularization
title: Lp Norms and Frobenius Norm
understanding: 0
---

## Definition
$$\|\mathbf{x}\|_p = \left(\sum_i |x_i|^p\right)^{1/p}, \quad p \geq 1; \qquad \|\mathbf{A}\|_F = \sqrt{\sum_{i,j} A_{i,j}^2} = \sqrt{\operatorname{Tr}(\mathbf{A}\mathbf{A}^T)}$$

A **norm** is any function $f$ satisfying non-negativity with equality at zero, the triangle inequality, and absolute homogeneity. Special cases: $L^2$ (Euclidean), $L^1$ (sum of absolutes, sparsity-inducing), $L^\infty$ (max norm), and the Frobenius norm (matrix analogue of $L^2$).

### Why it matters
The choice of norm encodes geometric and statistical assumptions. $L^2$ regularization corresponds to a Gaussian prior; $L^1$ promotes sparsity and corresponds to a Laplace prior. The Frobenius norm is the natural loss for matrix reconstruction problems such as PCA and low-rank approximation. The identity $\|\mathbf{A}\|_F = \sqrt{\operatorname{Tr}(\mathbf{A}\mathbf{A}^T)}$ enables algebraic manipulation via trace properties.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]