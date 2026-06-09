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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:concept:stationary-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- limiting-distributions
related_concepts: []
sources:
- resnick-stochastic-processes-ch02
tags:
- stochastic-processes
- markov-property
- ergodicity
- invariant-measure
- long-run-behavior
title: Stationary Distribution and Invariant Measure
understanding: 0
uses:
- markov-chains
- recurrence-and-transience
---

## Definition
A probability distribution \pi = {\pi_j} over the state space of a Markov chain is stationary if \pi' = \pi' P, i.e. \pi_j = \sum_k \pi_k p_{kj}. If the chain is started from \pi, it becomes a strictly stationary stochastic process: P_\pi[X_n=j] = \pi_j for all n. More generally a non-negative sequence \nu with \nu' = \nu' P is an invariant measure; an invariant measure that is also a probability (summable to 1) is a stationary distribution, but some invariant measures have infinite total mass and cannot be normalized.

For a recurrent state i, the cycle construction \nu_j = E_i \sum_{0<=n<\tau_i(1)} 1_{[X_n=j]} (expected visits to j between successive visits to i) yields an invariant measure with \nu_i=1. If i is positive recurrent (E_i\tau_i(1)<\infty), normalizing gives the stationary distribution \pi_j = \nu_j / E_i\tau_i(1). For an irreducible recurrent chain the invariant measure exists, is strictly positive and finite at every state, and is unique up to a multiplicative constant; for an irreducible positive-recurrent chain there is a unique stationary distribution given by \pi_j = 1/m_j = 1/E_j[\tau_j(1)] (the reciprocal mean return time). Without irreducibility uniqueness fails (e.g. gambler's ruin has uncountably many stationary distributions concentrated on the two absorbing states). The practical recipe for the mean return times is to solve the linear system \pi'=\pi'P. A generating-function technique handles infinite state spaces (e.g. the Moran storage model gives \Pi(s) = (1-EA_1)(1-s)/(A(s)-s), requiring EA_1<1).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[recurrence-and-transience]] — uses: invariant measure / stationary distribution constructed from positive-recurrent cycle structure
- [[limiting-distributions]] — prerequisite-of: a limit distribution is necessarily a stationary distribution
- [[markov-chains]] — uses: the equilibrium distribution of a Markov chain
[To be populated during integration]