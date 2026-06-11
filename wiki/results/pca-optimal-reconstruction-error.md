---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:result:pca-optimal-reconstruction-error
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch13
tags:
- PCA
- dimensionality-reduction
- reconstruction-error
- eigenvalues
title: PCA Optimal Reconstruction Error
understanding: 0
---

## Definition
For data $\mathbf{x} \in \mathbb{R}^D$ with covariance $\mathbf{C} = \mathbb{E}[(\mathbf{x}-\boldsymbol{\mu})(\mathbf{x}-\boldsymbol{\mu})^\top]$ having eigenvalues $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_D \ge 0$, the minimum mean squared reconstruction error achievable by any rank-$d$ linear autoencoder is

$$\min \; \mathbb{E}\!\left[\|\mathbf{x} - \hat{\mathbf{x}}\|^2\right] = \sum_{i=d+1}^{D} \lambda_i.$$

This minimum is attained when the encoder projects onto the top-$d$ eigenvectors of $\mathbf{C}$ (principal components).

### Why it matters
The result gives a precise, data-driven criterion for choosing the number of principal components $d$: retain enough components so that $\sum_{i=d+1}^D \lambda_i$ (the discarded variance) is acceptably small. It also establishes the equivalence between minimising reconstruction error and maximising explained variance under an orthogonality constraint, connecting the autoencoder view of PCA to the classical eigendecomposition view.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]