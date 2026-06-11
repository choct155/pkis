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
- probability
- machine-learning
id: pkis:concept:stochastic-process-as-prior
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch31
tags:
- stochastic-process
- kolmogorov-extension
- prior
- infinite-dimensional
- bayesian-nonparametric
title: Stochastic Process as Prior
understanding: 0
---

## Definition
A stochastic process $\{X_t\}_{t\in\mathcal{T}}$ over an index set $\mathcal{T}$ defines a prior distribution on an infinite collection of random variables simultaneously. The key consistency requirement (Kolmogorov's extension theorem) guarantees that any finite-dimensional marginal is well-defined: for any finite $\{t_1,\ldots,t_n\}\subset\mathcal{T}$ the joint $p(X_{t_1},\ldots,X_{t_n})$ is coherent with the full process.

In Bayesian nonparametrics this construction is the standard device for placing priors on functions (Gaussian processes), distributions (Dirichlet processes), and other infinite-dimensional objects.

### Why it matters
Using a stochastic process as a prior allows the model complexity to be formally infinite while every computational operation touches only finitely many marginals, enabling tractable posterior inference despite the infinite-parameter nature of the prior.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]