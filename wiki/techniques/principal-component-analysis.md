---
aliases:
- PCA
also_type: []
coverage: 2
date_created: 2026-05-20
date_updated: '2026-06-08'
domain:
- statistical-learning
id: pkis:technique:principal-component-analysis
instantiates:
- latent-variable-models
knowledge_type: technique
maturity: settled
related_concepts:
- '[[curse-of-dimensionality]]'
- '[[singular-value-decomposition]]'
- '[[matrix-decompositions]]'
- '[[analytic-geometry]]'
sources:
- '[[hastie-esl]]'
- '[[deisenroth-mml]]'
tags:
- linear-algebra
- dimensionality-reduction
title: Principal Component Analysis (PCA)
understanding: 0
---

Linear dimensionality reduction that projects data onto the directions of maximum variance, found as the eigenvectors of the covariance matrix (equivalently, the right singular vectors of the centered data matrix).

## Connections
- [[latent-variable-models]] — instantiates: PCA is the Gaussian-latent member of the latent variable family.

## Contrast with Independent Component Analysis
PCA and ICA are siblings in the latent variable family but differ in the assumed source prior, and this single choice determines what they can recover. PCA uses only second-order statistics (the covariance matrix) and is equivalent to assuming Gaussian latents. Because the Gaussian distribution is invariant under rotation of the latent space, PCA fixes only an orthogonal subspace and an ordering by variance — it cannot identify the true mixing directions, and any rotation of its components is equally valid.

ICA instead assumes the latents are *independent and non-Gaussian* (e.g. heavy-tailed $p(s)\propto 1/\cosh(s)$ via the $\tanh$ nonlinearity). Non-Gaussianity breaks the rotational symmetry, so ICA can recover the actual mixing matrix $G$ (up to scale and permutation) where PCA cannot. Put crudely: PCA decorrelates, ICA makes independent. When the sources really are Gaussian, ICA degenerates and recovers no preferred alignment — exactly the regime where PCA is the right tool.