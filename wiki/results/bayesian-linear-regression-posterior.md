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
- bayesian-statistics
id: pkis:result:bayesian-linear-regression-posterior
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch03
tags:
- conjugate-prior
- posterior
- ridge-regression
- sequential-learning
title: Bayesian Linear Regression Posterior
understanding: 0
---

## Definition
For a linear basis function model with Gaussian likelihood $p(\mathbf{t}|\mathbf{w},\beta) = \prod_n \mathcal{N}(t_n|\mathbf{w}^T\boldsymbol{\phi}(x_n),\beta^{-1})$ and Gaussian prior $p(\mathbf{w}) = \mathcal{N}(\mathbf{w}|\mathbf{m}_0,\mathbf{S}_0)$, the posterior is exactly Gaussian:

$$p(\mathbf{w}|\mathbf{t}) = \mathcal{N}(\mathbf{w}|\mathbf{m}_N, \mathbf{S}_N)$$

$$\mathbf{m}_N = \mathbf{S}_N(\mathbf{S}_0^{-1}\mathbf{m}_0 + \beta\boldsymbol{\Phi}^T\mathbf{t}), \quad \mathbf{S}_N^{-1} = \mathbf{S}_0^{-1} + \beta\boldsymbol{\Phi}^T\boldsymbol{\Phi}$$

For the isotropic prior $p(\mathbf{w}|\alpha)=\mathcal{N}(\mathbf{w}|\mathbf{0},\alpha^{-1}\mathbf{I})$, maximizing the posterior is equivalent to minimizing the $L_2$-regularized sum-of-squares error with $\lambda = \alpha/\beta$.

### Why it matters
Conjugate Gaussian analysis gives an *exact* closed-form posterior in a single pass, enabling sequential Bayesian updating: the posterior after $n$ observations becomes the prior for observation $n+1$. The MAP solution recovers ridge regression; the full posterior enables predictive uncertainty quantification.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]