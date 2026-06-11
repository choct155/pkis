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
contrasts-with:
- ridge-regression
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine learning
extends:
- maximum-likelihood-estimation
id: pkis:technique:lasso-regression
instantiates:
- lasso
- map-regression-as-regularized-least-squares
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch11
tags:
- sparsity
- variable selection
- L1
- regularization
- MAP estimation
title: Lasso Regression ($\ell_1$-Regularised Linear Regression)
understanding: 0
uses:
- soft-thresholding
- regularization-path
- shooting-algorithm
---

## Definition
$$\hat{\mathbf{w}}_\text{lasso} = \operatorname*{argmin}_{\mathbf{w}} \|\mathbf{X}\mathbf{w}-\mathbf{y}\|_2^2 + \lambda\|\mathbf{w}\|_1$$

Lasso (Least Absolute Shrinkage and Selection Operator) is MAP estimation of a linear regression model under an independent Laplace prior on the weights; the $\ell_1$ penalty causes many coefficients to be exactly zero, yielding sparse solutions.

### Why it matters
Unlike ridge, which shrinks all coefficients proportionally, lasso performs simultaneous estimation and variable selection. The $\ell_1$ ball has corners on the coordinate axes, so the constrained optimum is geometrically likely to fall there. The solution in orthonormal design is soft-thresholding: $\hat{w}_d = \operatorname{sign}(\hat{w}_d^\text{mle})(|\hat{w}_d^\text{mle}|-\lambda)_+$. The regularisation path is piecewise linear in $\lambda$, and the maximum number of non-zero variables is $\min(N,D)$.

### Limitations
Lasso shrinks selected coefficients (bias), is not model-selection consistent at the prediction-optimal $\lambda$, and cannot select more than $N$ variables when $D>N$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[maximum-likelihood-estimation]] — extends
- [[map-regression-as-regularized-least-squares]] — instantiates
- [[shooting-algorithm]] — uses
- [[lasso]] — instantiates
- [[regularization-path]] — uses
- [[soft-thresholding]] — uses
- [[ridge-regression]] — contrasts-with
[To be populated during integration]