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
- statistics
- optimisation
- signal processing
id: pkis:concept:soft-thresholding
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch11
tags:
- proximal operator
- sparsity
- lasso
- coordinate descent
title: Soft Thresholding Operator
understanding: 0
---

## Definition
$$\operatorname{SoftThreshold}(x, \delta) \triangleq \operatorname{sign}(x)(|x|-\delta)_+$$

The soft-threshold function shrinks a scalar $x$ toward zero by $\delta$, setting it exactly to zero when $|x|\leq\delta$; it is the proximal operator of the $\ell_1$ norm.

### Why it matters
Soft thresholding is the closed-form coordinate update for lasso: with orthonormal features the optimal $\hat{w}_d$ is $\operatorname{SoftThreshold}(\mathbf{x}_{:d}^T\mathbf{r}_{-d}/\|\mathbf{x}_{:d}\|^2,\, \lambda/\|\mathbf{x}_{:d}\|^2)$. It contrasts with hard thresholding (subset selection), which retains the full OLS value when above threshold but does not shrink. Soft thresholding is also the key operation in wavelet denoising and ISTA/FISTA algorithms.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]