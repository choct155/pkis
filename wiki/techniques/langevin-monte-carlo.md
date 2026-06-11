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
id: pkis:technique:langevin-monte-carlo
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch12
tags:
- mcmc
- langevin
- gradient-mcmc
- sgld
- stochastic-differential-equations
title: Langevin Monte Carlo (MALA)
understanding: 0
---

## Definition
A gradient-based MCMC method obtained as the $L=1$ leapfrog special case of HMC, proposing:
$$\theta^* = \theta_{t-1} - \tfrac{\eta^2}{2}\Sigma^{-1}\nabla\mathcal{E}(\theta_{t-1}) + \eta\,\Sigma^{-1}v_{t-1}, \quad v_{t-1}\sim\mathcal{N}(0,\Sigma)$$
with an optional Metropolis–Hastings correction (the corrected version is called MALA; without it, ULA). In continuous time this converges to Langevin diffusion: $d\theta_t = -\nabla\mathcal{E}(\theta_t)\,dt + \sqrt{2}\,dB_t$.

### Why it matters
LMC/MALA bridges MCMC and optimisation: the gradient term drives the chain toward high-probability regions (like gradient descent) while the noise term ensures stochasticity and ergodicity. Setting $\Sigma$ to the Fisher information recovers natural gradient descent with noise. Replacing exact gradients with mini-batch stochastic gradients yields SGLD (stochastic gradient Langevin dynamics), enabling scalable approximate Bayesian inference.

### Connection to SGD
The stochastic gradient noise in SGD plays the role of the injected Langevin noise; in the continuous-time limit SGD approximates a Langevin diffusion, linking optimisation and sampling.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]