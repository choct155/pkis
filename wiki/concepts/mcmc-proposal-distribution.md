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
date_updated: '2026-06-22'
domain:
- MCMC
- bayesian-computation
- stochastic-processes
id: pkis:concept:mcmc-proposal-distribution
instantiates:
- random-walk-metropolis
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- metropolis-hastings
- hmc
related_concepts: []
sources:
- murphy-pml2-advanced-ch07
- neal-mcmc-2012
tags:
- proposal
- Metropolis-Hastings
- random-walk
- HMC
- acceptance-rejection
title: Proposal Distribution (MCMC)
understanding: 0
uses:
- mcmc
---

## Definition
$$\theta' \sim q(\theta'|\theta)$$

A proposal distribution generates candidate states for a Markov chain given the current state; in Metropolis-Hastings the proposal is accepted or rejected based on the density ratio of the unnormalised target.

### Why it matters
The proposal determines mixing speed: too narrow and the chain explores slowly; too wide and most proposals fall in low-probability regions and are rejected. The random walk Metropolis uses $q(\theta'|\theta) = \mathcal{N}(\theta'|\theta, \sigma^2 I)$ (isotropic diffusion), while HMC uses gradient-driven Hamiltonian dynamics as the proposal, dramatically reducing autocorrelation in high-dimensional posteriors. Choosing a good proposal is the central practical challenge in MCMC design.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mcmc]] — uses
- [[hmc]] — prerequisite-of
- [[random-walk-metropolis]] — instantiates
- [[metropolis-hastings]] — prerequisite-of
[To be populated during integration]