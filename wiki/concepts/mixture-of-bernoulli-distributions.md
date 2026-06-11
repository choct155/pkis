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
- machine-learning
- probabilistic-modeling
id: pkis:concept:mixture-of-bernoulli-distributions
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch09
tags:
- mixture-models
- binary-data
- latent-class-analysis
- EM
- Bernoulli
title: Mixture of Bernoulli Distributions (Latent Class Analysis)
understanding: 0
---

## Definition
A mixture of $K$ multivariate Bernoulli distributions over a $D$-dimensional binary vector $\mathbf{x}=(x_1,\ldots,x_D)^T$:
$$p(\mathbf{x}\mid\boldsymbol{\mu},\boldsymbol{\pi})=\sum_{k=1}^{K}\pi_k\prod_{i=1}^{D}\mu_{ki}^{x_i}(1-\mu_{ki})^{1-x_i}$$
where $\boldsymbol{\mu}_k$ is the vector of Bernoulli parameters for component $k$. Also known as *latent class analysis*.

The mixture mean and covariance are
$$\mathbb{E}[\mathbf{x}]=\sum_k\pi_k\boldsymbol{\mu}_k, \qquad \mathrm{cov}[\mathbf{x}]=\sum_k\pi_k\{\boldsymbol{\Sigma}_k+\boldsymbol{\mu}_k\boldsymbol{\mu}_k^T\}-\mathbb{E}[\mathbf{x}]\mathbb{E}[\mathbf{x}]^T$$
with $\boldsymbol{\Sigma}_k=\mathrm{diag}\{\mu_{ki}(1-\mu_{ki})\}$. The covariance is non-diagonal, so the mixture captures correlations absent in any single component.

### Why it matters
Unlike the Gaussian mixture, the Bernoulli mixture likelihood is bounded above (since $0\leq p(\mathbf{x}_n\mid\boldsymbol{\mu}_k)\leq 1$), so there are no singularities in maximum likelihood estimation. EM updates in closed form: $\boldsymbol{\mu}_k^{\text{new}}=\bar{\mathbf{x}}_k$ (responsibility-weighted mean) and $\pi_k^{\text{new}}=N_k/N$. The model is the foundation for discrete hidden Markov models and is conjugate to Beta/Dirichlet priors.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]