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
- optimization
- linear-algebra
- regularization
id: pkis:result:l2-regularization-eigenspectrum-shrinkage
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch07
tags:
- weight-decay
- L2-regularization
- eigenvalue
- Hessian
- shrinkage
- ridge-regression
title: L2 Regularization Eigenspectrum Shrinkage
understanding: 0
uses:
- ridge-regression
- hessian-matrix
- eigendecomposition
- weight-decay-as-prior
---

## Definition
For a quadratic objective with Hessian $\mathbf{H} = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top$, the $L^2$-regularized optimum satisfies:
$$\tilde{\mathbf{w}} = \mathbf{Q}(\boldsymbol{\Lambda}+\alpha\mathbf{I})^{-1}\boldsymbol{\Lambda}\mathbf{Q}^\top \mathbf{w}^*$$

The component of $\mathbf{w}^*$ along eigenvector $i$ is rescaled by $\frac{\lambda_i}{\lambda_i + \alpha}$. Directions with $\lambda_i \gg \alpha$ are nearly unchanged; directions with $\lambda_i \ll \alpha$ are shrunk toward zero.

$L^2$ regularization selectively suppresses parameters in directions of low curvature (low information) while preserving those that strongly reduce training loss.

### Why it matters
This result gives a precise spectral interpretation of weight decay: it acts like a PCA filter on parameter space, retaining directions that genuinely reduce loss and discarding those that do not. It also explains why $L^2$ regularization never produces exact zeros (unlike $L^1$), since the shrinkage factor $\lambda_i/(\lambda_i+\alpha)$ is always positive.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[weight-decay-as-prior]] — uses
- [[eigendecomposition]] — uses
- [[hessian-matrix]] — uses
- [[ridge-regression]] — uses
[To be populated during integration]