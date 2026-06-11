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
- MCMC
- bayesian-computation
id: pkis:technique:random-walk-metropolis
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch07
- murphy-pml2-advanced-ch12
tags:
- Metropolis
- random-walk
- acceptance-rejection
- MCMC
- proposal
title: Random Walk Metropolis Algorithm
understanding: 0
---

## Definition
$$\theta' \sim \mathcal{N}(\theta'|\theta_t, \sigma^2 I), \quad \alpha = \min\left(1,\, \frac{p(D,\theta')}{p(D,\theta_t)}\right), \quad \theta_{t+1} = \begin{cases}\theta' & \text{with prob. }\alpha \\ \theta_t & \text{otherwise}\end{cases}$$

The simplest Metropolis-Hastings variant: propose a Gaussian perturbation from the current state, accept with probability equal to the unnormalised density ratio (clamped at 1), otherwise stay.

### Why it matters
Random walk Metropolis requires only evaluation of the log joint $\log p(\theta, D)$ — no gradients needed — making it applicable to any differentiable or even non-differentiable model. It is the conceptual baseline for all MCMC methods. Its key weakness is diffusive exploration: mixing time scales as $O(D^2)$ in dimension $D$, making it impractical for high-dimensional posteriors without tuning $\sigma$ to achieve ~23% acceptance rate (optimal for Gaussian targets).

### Scaling
For Gaussian targets in $D$ dimensions the optimal step-size scales as $\sigma \propto D^{-1/2}$, yielding $O(D)$ autocorrelation and $O(D^2)$ cost per independent sample — motivating gradient-based methods like HMC.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]