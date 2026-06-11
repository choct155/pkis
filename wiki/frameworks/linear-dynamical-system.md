---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- signal-processing
- control-theory
- time-series
id: pkis:framework:linear-dynamical-system
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch13
tags:
- Kalman
- state-space
- Gaussian
- sequential
- LDS
- EM
title: Linear Dynamical System (Kalman Filter Model)
understanding: 0
---

## Definition
A state-space model with linear-Gaussian transition and emission distributions:
$$p(\mathbf{z}_n|\mathbf{z}_{n-1}) = \mathcal{N}(\mathbf{z}_n|A\mathbf{z}_{n-1},\Gamma), \quad p(\mathbf{x}_n|\mathbf{z}_n) = \mathcal{N}(\mathbf{x}_n|C\mathbf{z}_n,\Sigma), \quad p(\mathbf{z}_1) = \mathcal{N}(\mathbf{z}_1|\mu_0,V_0)$$

or equivalently via noisy linear equations $\mathbf{z}_n = A\mathbf{z}_{n-1}+\mathbf{w}_n$, $\mathbf{x}_n=C\mathbf{z}_n+\mathbf{v}_n$. Parameters $\theta=\{A,\Gamma,C,\Sigma,\mu_0,V_0\}$ are learned by EM.

Because all distributions are Gaussian, the sum-product algorithm yields closed-form forward (Kalman filter) and backward (RTS smoother) passes, both $O(L^2 N)$. The joint distribution over all variables is a single multivariate Gaussian.

### Why it matters
Generalizes probabilistic PCA and factor analysis to sequential data; the continuous analogue of the HMM. Exact inference is tractable because Gaussians are closed under the products and marginalizations performed at each recursion step. Widely used in tracking, control, econometrics, and neuroscience. Non-linear/non-Gaussian extensions include the extended Kalman filter, unscented Kalman filter, and particle filter.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]