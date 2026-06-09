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
id: pkis:concept:burn-in-and-warmup
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch11
tags:
- mcmc
- warm-up
- burn-in
- thinning
- starting-values
- transient
- gelman
title: Burn-in and Warm-up (MCMC)
understanding: 0
---

## Definition
Warm-up (Gelman's preferred term; classically 'burn-in') is the practice of discarding the early iterations of each MCMC sequence to diminish the influence of the starting values. Inference assumes the saved draws ω^t, for large enough t, are close to the target p(ω|y); early iterations still reflect the (overdispersed) starting distribution rather than the stationary distribution, so including them biases summaries. The amount to discard is context-dependent — a fast-mixing Gibbs sampler may need only a few iterations dropped, while a slowly-mixing Metropolis run needs more — but Gelman adopts the conservative default of discarding the *first half* of every sequence. Practically: run e.g. 200 iterations and discard the first 100; if convergence is not yet reached, run another 200 and discard all of the first 200.

Warm-up interacts with the convergence machinery: starting points should be drawn from an overdispersed distribution (a crude estimate or a normal approximation) and multiple sequences run, so that between- vs within-sequence comparison (the Gelman-Rubin diagnostic) can detect non-convergence; the default first-half warm-up is what is discarded *before* chains are split in half for that diagnostic.

A distinct, optional post-convergence step is *thinning*: keeping only every k-th saved draw and discarding the rest. Thinning does not improve inference per se — autocorrelated draws are still validly distributed as p(ω|y) at convergence — but is useful in high-dimensional problems where storage is the constraint (e.g. choosing k so the total saved is ≤ 1000). Whether or not sequences are thinned, once approximate convergence is reached the saved draws are used directly for posterior inference.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]