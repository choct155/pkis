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
- probability-theory
- time-series
- machine-learning
id: pkis:concept:observed-markov-chain
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch13
tags:
- Markov
- sequential
- autoregressive
- time-series
- first-order
title: Markov Chain (Observed, Higher-Order)
understanding: 0
---

## Definition
A probabilistic model for sequential data in which the joint distribution factorizes as
$$p(x_1,\ldots,x_N) = p(x_1)\prod_{n=2}^{N}p(x_n|x_{n-1}) \quad \text{(first order)}$$
or more generally as $p(x_n|x_{n-M},\ldots,x_{n-1})$ for an $M$th-order chain. For discrete observations with $K$ states the first-order model has $K(K-1)$ parameters; the $M$th-order model has $K^{M-1}(K-1)$ parameters (exponential in $M$). For continuous observations the $M$th-order linear-Gaussian version is the autoregressive (AR) model.

### Why it matters
Simplest non-i.i.d. sequential model; motivates the introduction of latent variables (state-space models) to capture longer-range dependence without exponential parameter growth. The homogeneous (stationary) first-order chain is the building block of HMMs and LDS.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]