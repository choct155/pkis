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
- linear-algebra
id: pkis:technique:pca-linear-algebra-derivation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch02
tags:
- PCA
- dimensionality reduction
- eigendecomposition
- reconstruction
- projection
title: Principal Component Analysis (Linear Algebra Derivation)
understanding: 0
---

## Definition
Given data matrix $\mathbf{X}\in\mathbb{R}^{m\times n}$, PCA finds an orthonormal decoding matrix $\mathbf{D}\in\mathbb{R}^{n\times l}$ ($l<n$, columns orthonormal) that minimises reconstruction error:
$$\mathbf{D}^* = \arg\min_{\mathbf{D}^T\mathbf{D}=\mathbf{I}_l} \|\mathbf{X} - \mathbf{X}\mathbf{D}\mathbf{D}^T\|_F^2.$$
The optimal code for input $\mathbf{x}$ is $\mathbf{c} = \mathbf{D}^T\mathbf{x}$ and the reconstruction is $\hat{\mathbf{x}} = \mathbf{D}\mathbf{D}^T\mathbf{x}$. Using trace identities and eigendecomposition, the objective reduces to $\arg\max_{\mathbf{d}^T\mathbf{d}=1}\mathbf{d}^T\mathbf{X}^T\mathbf{X}\mathbf{d}$, so the optimal columns of $\mathbf{D}$ are the top-$l$ eigenvectors of $\mathbf{X}^T\mathbf{X}$.

PCA is lossy linear dimensionality reduction via orthogonal projection onto the subspace of maximum variance.

### Why it matters
This derivation reveals PCA as purely an eigendecomposition problem and shows how the Frobenius norm, trace identities, and orthogonality constraints interact. It is the canonical bridge from linear algebra to unsupervised representation learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]