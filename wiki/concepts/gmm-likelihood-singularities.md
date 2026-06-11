---
aliases: []
also_type: []
applies:
- gaussian-mixture-models
- maximum-likelihood-estimation
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- variational-inference
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
id: pkis:concept:gmm-likelihood-singularities
instantiates:
- overfitting-and-underfitting
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch09
tags:
- Gaussian-mixtures
- MLE
- overfitting
- identifiability
- singularities
title: Singularities in Gaussian Mixture Maximum Likelihood
understanding: 0
uses:
- mixture-model-identifiability
---

## Definition
The log-likelihood of a Gaussian mixture
$$\ln p(\mathbf{X}\mid\boldsymbol{\pi},\boldsymbol{\mu},\boldsymbol{\Sigma})=\sum_{n=1}^N\ln\sum_{k=1}^K\pi_k\mathcal{N}(\mathbf{x}_n\mid\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k)$$
is *unbounded above*. If component $j$ collapses onto a data point ($\boldsymbol{\mu}_j=\mathbf{x}_n$, $\sigma_j\to 0$), its contribution $\mathcal{N}(\mathbf{x}_n\mid\mathbf{x}_n,\sigma_j^2\mathbf{I})=(2\pi)^{-D/2}\sigma_j^{-D}\to\infty$. Unlike a single Gaussian, the remaining components can simultaneously assign finite probability to all other points, so the overall log-likelihood diverges.

This makes MLE for Gaussian mixtures an *ill-posed* optimisation problem.

### Why it matters
Singularities are a fundamental limitation of MLE for Gaussian mixtures; they are a pathological form of over-fitting. Practical remedies include: (1) detecting component collapse and re-initialising, (2) constraining covariances to have bounded determinants, or (3) adopting a Bayesian treatment (variational or MCMC) with proper priors, which automatically regularises against collapse. Bayesian approaches resolve the singularity by making the posterior probability of such degenerate solutions exactly zero.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mixture-model-identifiability]] — uses
- [[variational-inference]] — contrasts-with: Bayesian treatment resolves singularities via priors
- [[overfitting-and-underfitting]] — instantiates
- [[maximum-likelihood-estimation]] — applies
- [[gaussian-mixture-models]] — applies
[To be populated during integration]