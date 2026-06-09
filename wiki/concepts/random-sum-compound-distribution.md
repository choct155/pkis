---
aliases: []
also_type: []
applies:
- poisson-process
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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:concept:random-sum-compound-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch01
tags:
- probability-theory
- stochastic-processes
- generating-functions
- compound-poisson
- random-sums
title: Random Sum and Compound Distribution
understanding: 0
uses:
- probability-generating-function
- convolution-of-distributions
---

## Definition
$$S_N = \sum_{i=1}^{N} X_i, \qquad P_{S_N}(s) = P_N\big(P_{X_1}(s)\big)$$

A random sum adds a *random* number $N$ of i.i.d. terms $X_1, X_2, \ldots$ (with $N$ independent of the terms); its distribution is the *compound distribution*. Its generating function is the composition of the two generating functions, with the gf of the random index on the outside.

### Compound Poisson and moments
When $N \sim \text{Poisson}(\lambda)$ the composition gives the **compound-Poisson** gf $P_{S_N}(s) = \exp\{\lambda(P_{X_1}(s)-1)\}$. Differentiating the composition at $s=1$ yields the clean moment relation
$$E(S_N) = E(N)\,E(X_1),$$
the first instance of the pattern later generalized by Wald's identity.

### Thinning as a special case
If the $X_i$ are Bernoulli($p$) indicators (success/failure), compounding a Poisson($\lambda$) count thins it to a Poisson($\lambda p$): each arrival survives with probability $p$ and the survivors are again Poisson. This is the analytic basis of Poisson-process thinning and coloring.

### Why it matters
Random sums model insurance claims (a random number of claims of random size), customer flows, and offspring counts. Compounding via gf composition is exactly the operation that drives the simple branching process, where the generation-to-generation map is functional composition of the offspring generating function with itself.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[poisson-process]] — applies: Compounding Bernoulli indicators by a Poisson count yields Poisson thinning, basic to Poisson-process theory.
- [[convolution-of-distributions]] — uses: A random sum mixes convolution powers of the term distribution weighted by the index distribution.
- [[probability-generating-function]] — uses: The compound-distribution gf is the composition P_N(P_X(s)) of the two PGFs.
[To be populated during integration]