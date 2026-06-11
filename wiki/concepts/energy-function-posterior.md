---
aliases: []
also_type: []
analogous-to:
- ising-model
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
- bayesian-inference
- statistical-physics
- probabilistic-modeling
id: pkis:concept:energy-function-posterior
instantiates:
- partition-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- laplace-approximation
related_concepts: []
sources:
- murphy-pml2-advanced-ch07
tags:
- energy
- unnormalized-density
- partition-function
- MAP
- posterior
title: Energy Function (Unnormalized Posterior)
understanding: 0
uses:
- bayesian-inference
- maximum-a-posteriori-estimation-map
---

## Definition
$$\mathcal{E}(\theta) = -\log p(\theta, D) = -\log p(D|\theta) - \log p(\theta)$$

The energy function recasts the joint log-density as a scalar cost surface; the posterior normalising constant $Z = p(D) = \int e^{-\mathcal{E}(\theta)}\,d\theta$ is the partition function, and the MAP estimate is the global energy minimum.

### Why it matters
Expressing the posterior as $p(\theta|D) = e^{-\mathcal{E}(\theta)}/Z$ enables a unified language shared by statistical physics, optimisation, and Bayesian inference. It motivates Laplace approximation (Taylor-expand $\mathcal{E}$ around its minimum), MCMC (random walk on the energy landscape), and variational inference (minimise a functional over $\mathcal{E}$). Working in log-space avoids numerical underflow when evaluating ratios of unnormalised densities.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[ising-model]] — analogous-to
- [[maximum-a-posteriori-estimation-map]] — uses
- [[laplace-approximation]] — prerequisite-of
- [[partition-function]] — instantiates
- [[bayesian-inference]] — uses
[To be populated during integration]