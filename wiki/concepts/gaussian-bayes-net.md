---
aliases: []
also_type: []
analogous-to:
- structural-equation-models
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
- gaussian-graphical-model
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probabilistic-graphical-models
- statistics
id: pkis:concept:gaussian-bayes-net
instantiates:
- multivariate-normal-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch04
specializes:
- bayesian-networks
tags:
- linear-Gaussian
- structural-equation-model
- covariance
- DAG
title: Gaussian Bayes Net (Directed Gaussian Graphical Model)
understanding: 0
uses:
- gaussian-distribution
- path-coefficient
---

## Definition
A DAG-structured model where every CPD is a linear Gaussian:
$$p(x_i \mid x_{\text{pa}(i)}) = \mathcal{N}\!\left(x_i \,\middle|\, \mu_i + w_i^T x_{\text{pa}(i)},\, \sigma_i^2\right)$$
The joint is multivariate Gaussian $p(x) = \mathcal{N}(x\mid\mu, \Sigma)$ with $\Sigma = \mathbf{U}\mathbf{S}^2\mathbf{U}^T$, where $\mathbf{U} = (\mathbf{I}-\mathbf{W})^{-1}$ and $\mathbf{W}$ is the lower-triangular matrix of regression weights.

The Cholesky-like factorization of the precision matrix corresponds directly to the DAG edge weights.

### Why it matters
Gaussian Bayes nets unify linear structural equation models (SEMs) with probabilistic graphical models. The mapping $\Sigma = \mathbf{U}\mathbf{S}^2\mathbf{U}^T$ gives a closed-form path from local parameters $(\mu_i, w_i, \sigma_i)$ to the global covariance, enabling efficient inference and connecting to path-coefficient analysis and causal modeling.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gaussian-graphical-model]] — contrasts-with: Gaussian Bayes net is directed; Gaussian graphical model is undirected
- [[multivariate-normal-model]] — instantiates
- [[path-coefficient]] — uses
- [[structural-equation-models]] — analogous-to
- [[gaussian-distribution]] — uses
- [[bayesian-networks]] — specializes
[To be populated during integration]