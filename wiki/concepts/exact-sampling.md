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
- mcmc
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
- statistical-learning
id: pkis:concept:exact-sampling
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch32
tags:
- mcmc
- perfect-simulation
- equilibrium-distribution
- burn-in
- convergence-diagnostics
title: Exact (Perfect) Sampling
understanding: 0
---

## Definition
**Exact sampling** (also *perfect sampling* or *perfect simulation*) refers to algorithms that return samples drawn *precisely* from a Markov chain's stationary distribution $P(x)$, rather than from the time-$T$ approximation $P^{(T)}(x)$ produced by running an ordinary MCMC chain for a finite time.

Standard MCMC (Metropolis, Gibbs, slice sampling) is guaranteed to sample from $P$ only asymptotically, *after the chain has converged*. For finite run length $T$ the samples come from some other distribution $P^{(T)}$, and determining how long is 'long enough' is generally intractable. Exact sampling sidesteps this: it certifies, internally, that the equilibrium distribution has been reached.

### Why it matters
It removes the two chronic headaches of MCMC: choosing a burn-in period and diagnosing convergence. There is no bias from a too-short run.

### How it is achieved
The central realization (Propp-Wilson) is coalescence of coupled chains plus coupling from the past. The flagship demonstration was an exact draw from a 16-million-spin Ising model at its critical temperature.

### Limitations
Exact-sampling schemes can be slow when the underlying chain mixes slowly (e.g. the Ising model below its critical temperature), and the detection machinery may report coalescence later than the true mixing time.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mcmc]] — contrasts-with: Exact sampling removes the asymptotic-convergence / burn-in bias inherent to ordinary finite-time MCMC.
[To be populated during integration]