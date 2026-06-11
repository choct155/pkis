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
- statistics
- machine-learning
- probabilistic-graphical-models
id: pkis:technique:collapsed-gibbs-sampler
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch12
tags:
- mcmc
- rao-blackwellisation
- mixture-models
- dirichlet-process
- marginalisation
title: Collapsed Gibbs Sampler
understanding: 0
---

## Definition
A Gibbs sampling variant in which a subset of latent variables (typically continuous parameters) is analytically marginalized out before constructing the Markov chain, so that only the remaining variables (typically discrete indicators) are explicitly sampled:
$$p(z_i = k \mid z_{-i}, x, \alpha, \beta) \propto p(z_i = k \mid z_{-i}, \alpha)\,p(x_i \mid x_{-i}, z_i = k, z_{-i}, \beta)$$
For a GMM with conjugate priors this gives $p(z_i = k \mid z_{-i}, \alpha) = (N_{k,-i} + \alpha/K)/(N+\alpha-1)$ and $p(x_i \mid D_{-i,k}, \beta)$ is a closed-form posterior predictive.

### Why it matters
Sampling in a lower-dimensional space reduces variance (Rao–Blackwellisation) and often dramatically improves mixing. Collapsed Gibbs is the canonical algorithm for Dirichlet process mixture models and topic models (e.g., LDA), where it naturally extends to the infinite-$K$ limit. Efficient implementation caches sufficient statistics per cluster and updates them incrementally in $O(NKD)$ per sweep.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]