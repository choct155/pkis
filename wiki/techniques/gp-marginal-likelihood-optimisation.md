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
- Bayesian-statistics
id: pkis:technique:gp-marginal-likelihood-optimisation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch17
tags:
- empirical Bayes
- type-II ML
- kernel learning
- hyperparameter optimisation
- marginal likelihood
title: GP Marginal Likelihood Maximisation (Empirical Bayes for Kernels)
understanding: 0
---

## Definition
Given a GP with kernel parameters $\theta$, the **log marginal likelihood** is
$$\log p(\mathbf{y}|X,\theta) = -\tfrac{1}{2}\mathbf{y}^T K_\sigma^{-1}\mathbf{y} - \tfrac{1}{2}\log|K_\sigma| - \tfrac{N}{2}\log(2\pi),$$
where $K_\sigma = K_{X,X}+\sigma_y^2 I$. The gradient with respect to any hyperparameter $\theta_j$ is
$$\frac{\partial}{\partial\theta_j}\log p = \tfrac{1}{2}\operatorname{tr}\!\left[(\boldsymbol{\alpha}\boldsymbol{\alpha}^T - K_\sigma^{-1})\frac{\partial K_\sigma}{\partial\theta_j}\right], \quad \boldsymbol{\alpha}=K_\sigma^{-1}\mathbf{y}.$$
This expression balances a **data-fit term** ($\mathbf{y}^T K_\sigma^{-1}\mathbf{y}$) against a **complexity penalty** ($\log|K_\sigma|$), automatically implementing Occam's razor.

### Why it matters
Unlike cross-validation, marginal-likelihood optimisation is gradient-based ($O(N^2)$ per hyperparameter once $K_\sigma^{-1}$ is computed), scales to moderate $N$, and provides a principled Bayesian trade-off between fit and complexity. It is the standard method for learning length scales, output variance, and noise variance in GP models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]