---
aliases:
- PCA
also_type: []
coverage: 2
date_created: 2026-05-20
date_updated: 2026-05-20
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