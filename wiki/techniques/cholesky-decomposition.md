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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:technique:cholesky-decomposition
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch04
tags: []
title: Cholesky Decomposition
understanding: 0
---

## Definition
$$A = LL^{\top}$$

The Cholesky decomposition factorizes a symmetric, positive definite matrix $A$ into the product of a lower-triangular matrix $L$ (with strictly positive diagonal) and its transpose; it is the matrix analogue of a square root and the factor $L$ is unique.

### How it is computed
Matching entries of $A$ against $LL^\top$ yields a recursive backward pass: diagonal terms $l_{ii}=\sqrt{a_{ii}-\sum_{k<i} l_{ik}^2}$ and below-diagonal terms $l_{ij}=\frac{1}{l_{jj}}\big(a_{ij}-\sum_{k<j} l_{ik}l_{jk}\big)$ for $i>j$. Each entry depends only on previously computed values, so the full factor is obtained in a single sweep. Positive definiteness guarantees the square roots are of positive quantities, which is also a practical test for SPD-ness.

### Uses in machine learning
The covariance matrix of a multivariate Gaussian is symmetric positive definite, so its Cholesky factor enables drawing samples (transform standard normal noise by $L$) and underlies the **reparameterization trick** in variational autoencoders, allowing gradients to flow through stochastic nodes. It also computes determinants cheaply: $\det(A)=\det(L)^2=\prod_i l_{ii}^2$, and solves SPD linear systems via two triangular back-substitutions.

### Why it matters
SPD matrices appear constantly in ML — kernels, covariances, Hessians, Gram matrices — and the Cholesky factor is the workhorse that makes sampling, inversion, determinants, and linear solves numerically stable and efficient. It is one of the most heavily used decompositions in probabilistic modeling and Gaussian-process computation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]