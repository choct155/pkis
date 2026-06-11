---
aliases: []
also_type: []
applies:
- gaussian-process-gp
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
- statistics
- Bayesian-inference
id: pkis:technique:gp-posterior-inference
instantiates:
- bayesian-inference
- gaussian-process-regression
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch18
tags:
- GP
- posterior
- Cholesky
- Gaussian-likelihood
- interpolation
title: GP Posterior Inference (Gaussian Likelihood)
understanding: 0
uses:
- gaussian-distribution
- cholesky-decomposition
---

## Definition
Given training data $\mathcal{D} = \{(x_n, y_n)\}$ with $y_n = f(x_n) + \epsilon_n$, $\epsilon_n \sim \mathcal{N}(0,\sigma_y^2)$, and a GP prior $f \sim \mathcal{GP}(m, K)$, the posterior predictive distribution at test inputs $X_*$ is Gaussian:
$$p(f_*|\mathcal{D}, X_*) = \mathcal{N}(f_* | \boldsymbol{\mu}_{*|X}, \boldsymbol{\Sigma}_{*|X})$$
$$\boldsymbol{\mu}_{*|X} = \boldsymbol{\mu}_* + K_{X,*}^T K_\sigma^{-1}(y - \boldsymbol{\mu}_X)$$
$$\boldsymbol{\Sigma}_{*|X} = K_{*,*} - K_{X,*}^T K_\sigma^{-1} K_{X,*}$$
where $K_\sigma = K_{X,X} + \sigma_y^2 I$. Numerically, compute the Cholesky $K_\sigma = LL^T$ in $O(N^3)$; then $\boldsymbol{\alpha} = L^{-T}(L^{-1}y)$ and $\boldsymbol{\mu}_{*|X} = K_{X,*}^T \boldsymbol{\alpha}$.

With noise-free observations, set $\sigma_y^2 = 0$ to obtain exact interpolation.

### Why it matters
This is the core inference algorithm for GP regression: exact, closed-form, and analytically tractable. The posterior mean is a weighted sum of kernel evaluations at training points (matching the representer theorem), and the posterior variance quantifies epistemic uncertainty that grows away from observed data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gaussian-process-regression]] — instantiates
- [[bayesian-inference]] — instantiates
- [[cholesky-decomposition]] — uses
- [[gaussian-distribution]] — uses
- [[gaussian-process-gp]] — applies
[To be populated during integration]