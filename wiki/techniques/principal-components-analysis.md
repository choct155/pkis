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
- linear-algebra
id: pkis:technique:principal-components-analysis
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch20
tags:
- dimensionality-reduction
- unsupervised-learning
- linear-projection
- eigendecomposition
- reconstruction-error
title: Principal Components Analysis (PCA)
understanding: 0
---

## Definition
$$\hat{W} = U_L, \quad \mathcal{L}(W) = \frac{1}{N}\|X - ZW^T\|_F^2, \quad \hat{\Sigma}w_k = \lambda_k w_k$$

PCA finds the orthonormal projection matrix $W \in \mathbb{R}^{D \times L}$ ($L < D$) that minimises average squared reconstruction error; equivalently, the columns of $W$ are the $L$ eigenvectors of the empirical covariance matrix $\hat{\Sigma}$ with the largest eigenvalues, and the projected coordinates $z_n = W^T x_n$ maximise the variance of the projected data.

### Why it matters
PCA is the canonical baseline for linear dimensionality reduction: it is analytically solvable, admits a probabilistic interpretation (PPCA), connects directly to truncated SVD, and serves as a preprocessing step for downstream classifiers, visualisation (eigenfaces), and as the limiting case of factor analysis. Choosing $L$ can be done via scree plots, fraction-of-variance explained, or profile likelihood.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]