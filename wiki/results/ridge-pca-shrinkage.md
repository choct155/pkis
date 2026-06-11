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
- statistics
- machine learning
- linear algebra
id: pkis:result:ridge-pca-shrinkage
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch11
tags:
- ridge regression
- SVD
- PCA
- shrinkage
- degrees of freedom
title: Ridge–PCA Shrinkage Connection
understanding: 0
---

## Definition
Let $\mathbf{X} = \mathbf{U}\mathbf{S}\mathbf{V}^T$ be the SVD of $\mathbf{X}$. The ridge fitted values are

$$\hat{\mathbf{y}}_\text{ridge} = \sum_{j=1}^D \mathbf{u}_j \frac{\sigma_j^2}{\sigma_j^2+\lambda} \mathbf{u}_j^T\mathbf{y}$$

compared with $\hat{\mathbf{y}}_\text{ols} = \sum_j \mathbf{u}_j \mathbf{u}_j^T\mathbf{y}$; ridge multiplies each principal-direction contribution by a shrinkage factor $\sigma_j^2/(\sigma_j^2+\lambda)\in(0,1)$ that approaches 0 for small singular values and 1 for large ones.

### Why it matters
This result explains *why* ridge outperforms OLS: directions in which $\mathbf{X}$ has low variance (small $\sigma_j$) are also directions where the posterior variance of $\mathbf{w}$ is large, so downweighting them reduces estimation error. It also defines the effective degrees of freedom $\text{dof}(\lambda)=\sum_j \sigma_j^2/(\sigma_j^2+\lambda)$, bridging regularisation strength and model complexity, and motivates principal components regression as a hard-thresholded special case.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]