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
- spatial-statistics
generalizes:
- poisson-process
- poisson-regression
id: pkis:concept:cox-process
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch18
specializes:
- point-process
tags:
- point-process
- Poisson
- GP
- spatial-statistics
- latent-variable
title: Cox Process (Poisson GP)
understanding: 0
uses:
- gaussian-process-gp
---

## Definition
A **Cox process** (doubly stochastic Poisson process) is a Poisson process whose log-intensity function is modelled by a GP:
$$y_n \sim \text{Poi}(\exp(f(x_n))), \quad f \sim \mathcal{GP}(0, K)$$

The latent rate $\lambda(x) = \exp(f(x))$ is itself random, making the intensity spatially correlated according to the kernel $K$. Posterior inference over $f$ requires approximate methods (Laplace, MCMC, or variational inference) since the Poisson likelihood is non-conjugate.

### Why it matters
Cox processes are the standard Bayesian nonparametric model for spatially or temporally varying count data (disease mapping, seismology, neuronal spike trains). The GP prior allows smooth spatial borrowing of information, and posterior uncertainty quantifies both data sparsity and model uncertainty.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[poisson-regression]] — generalizes
- [[point-process]] — specializes
- [[gaussian-process-gp]] — uses
- [[poisson-process]] — generalizes
[To be populated during integration]