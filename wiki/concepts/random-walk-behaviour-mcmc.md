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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
- statistical-learning
id: pkis:concept:random-walk-behaviour-mcmc
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- hmc
related_concepts: []
sources:
- mackay-itila-ch30
tags:
- MCMC
- mixing
- diffusion
- convergence
- efficiency
title: Random-Walk Behaviour in MCMC
understanding: 0
---

## Definition
Random-walk behaviour is the diffusive, undirected exploration of state space exhibited by simple Markov chain Monte Carlo methods (e.g. random-walk Metropolis, Gibbs sampling with correlated variables), in which successive moves are uncorrelated in direction. Its defining signature is that the distance the chain travels grows only as the **square root** of the number of steps, $d \sim \sqrt{t}$, rather than linearly. To traverse a distribution of linear extent $L$ with step size $\epsilon$ therefore requires on the order of $(L/\epsilon)^2$ iterations.

### Where it bites
The pathology is worst when the target has **strong correlations** or **disparate length scales** — a needle-like Gaussian of width $\epsilon$ and length $L \gg \epsilon$. Step sizes must be kept small (of order $\epsilon$) to maintain a reasonable acceptance rate, so the chain crawls along the long direction. The same mechanism appears in hierarchical models: a hyperparameter $\beta$ whose conditional given $N$ data points has width $\propto 1/\sqrt{N}$ forces $\beta$ to random-walk in tiny steps, and no clever initialization fixes it.

### Why it matters
Quantifying random-walk inefficiency is the unifying motivation behind nearly every advanced sampler. Overrelaxation, Hamiltonian Monte Carlo, ordered overrelaxation, and Skilling's leapfrog are all engineered to replace $\sqrt{t}$ diffusion with **directed, ballistic** motion ($d \sim t$, or even exponential growth in the worst direction), collapsing mixing time from $(L/\epsilon)^2$ toward $L/\epsilon$ or $\log L$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hmc]] — prerequisite-of: the random-walk pathology is the motivating problem HMC is built to solve
[To be populated during integration]