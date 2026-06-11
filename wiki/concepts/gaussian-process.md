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
contrasts-with:
- bayesian-neural-networks
- curse-of-dimensionality
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- statistical-learning
- bayesian-stats
generalizes:
- gaussian-distribution
id: pkis:concept:gaussian-process
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- gaussian-process-regression
related_concepts: []
sources:
- mackay-itila-ch45
tags:
- gaussian-process
- prior-over-functions
- nonparametric
- bayesian-inference
- stochastic-process
title: Gaussian Process
understanding: 0
uses:
- generalized-linear-models
- mercer-kernel
---

## Definition
A **Gaussian process (GP)** is a probability distribution placed *directly* over a space of functions $y(\mathbf{x})$, without any explicit parameterization. It is the generalization of a multivariate Gaussian from a finite vector to an infinite-dimensional function space: a stochastic process $y(\mathbf{x})$ is a GP if, for *any* finite collection of input points $\mathbf{x}^{(1)},\dots,\mathbf{x}^{(N)}$, the joint density of the function values $P\big(y(\mathbf{x}^{(1)}),\dots,y(\mathbf{x}^{(N)})\big)$ is multivariate Gaussian. It is fully specified by a **mean function** $\mu(\mathbf{x})$ (usually taken to be zero) and a **covariance function** $C(\mathbf{x},\mathbf{x}')$ giving the expected covariance between $y(\mathbf{x})$ and $y(\mathbf{x}')$. The function underlying any one modelling problem is treated as a single sample from this distribution.

### Why it matters
The GP is the simplest nontrivial prior over functions, yet it captures the essential structure (smoothness, lengthscale, periodicity) that parametric models like multilayer perceptrons encode only implicitly. Crucially, for prediction only the prior $P(y(\mathbf{x}))$ and the noise model matter, so the *representation* of $y$ is irrelevant — the GP makes this explicit.

### Tractability despite infinite dimension
Though the function space is infinite-dimensional, inference concentrates on the joint distribution of observed and queried values, which is finite. Predictions therefore cost only polynomial — in practice $O(N^3)$ — work in the number of data points $N$, independent of any notional number of basis functions.

### Ubiquity
Brownian motion, Wiener and Langevin processes, Kalman-filter models, and geostatistical 'kriging' are all GPs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mercer-kernel]] — uses
- [[generalized-linear-models]] — uses: For non-Gaussian data a latent GP feeds a GLM-style link/likelihood (location and optionally shape).
- [[curse-of-dimensionality]] — contrasts-with: Centering a GP on a parametric mean function lets the posterior concentrate near it, mitigating the curse of dimensionality.
- [[bayesian-neural-networks]] — contrasts-with: GPs place a prior directly on functions (a smoothing device); BNNs parameterize functions and can in principle do feature discovery.
- [[gaussian-process-regression]] — prerequisite-of: GPR is inference under a GP prior with a Gaussian noise model.
- [[gaussian-distribution]] — generalizes: A GP is the generalization of a finite-dimensional Gaussian to an infinite-dimensional function space; any finite marginal is Gaussian.
[To be populated during integration]