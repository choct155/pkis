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
- optimisation
id: pkis:concept:matrix-norms
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch07
tags:
- Frobenius
- nuclear-norm
- spectral-norm
- Schatten
- regularisation
- low-rank
title: Frobenius Norm and Matrix Norms
understanding: 0
---

## Definition
For $\mathbf{A} \in \mathbb{R}^{m \times n}$ with singular values $\sigma_i$, the key matrix norms are:

$$\|\mathbf{A}\|_F = \sqrt{\sum_{i,j} a_{ij}^2} = \sqrt{\operatorname{tr}(\mathbf{A}^T\mathbf{A})} \quad \text{(Frobenius norm)}$$
$$\|\mathbf{A}\|_2 = \sigma_{\max} \quad \text{(spectral / induced 2-norm)}$$
$$\|\mathbf{A}\|_* = \sum_i \sigma_i \quad \text{(nuclear / trace norm)}$$
$$\|\mathbf{A}\|_p^{\text{Schatten}} = \left(\sum_i \sigma_i^p\right)^{1/p} \quad \text{(Schatten } p\text{-norm)}$$

The Frobenius norm treats the matrix as a vector; the nuclear norm is the $\ell_1$ norm on singular values and encourages low-rank structure when used as a regulariser.

### Why it matters
Matrix norms quantify approximation error in low-rank methods (SVD, PCA), condition number bounds, and regularisation. The nuclear norm is the convex surrogate for rank minimisation, widely used in matrix completion and compressed sensing. The Frobenius norm admits a stochastic estimator via the Hutchinson trace estimator.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]