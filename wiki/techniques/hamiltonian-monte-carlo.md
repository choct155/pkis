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
- physics
id: pkis:technique:hamiltonian-monte-carlo
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch12
tags:
- mcmc
- hamiltonian-dynamics
- leapfrog
- gradient-mcmc
- bayesian-computation
title: Hamiltonian Monte Carlo (HMC)
understanding: 0
---

## Definition
An auxiliary-variable MCMC method that augments the target $p(\theta)$ with a momentum variable $v \sim \mathcal{N}(0,\Sigma)$ to define a joint distribution:
$$p(\theta, v) \propto \exp[-\mathcal{H}(\theta,v)], \quad \mathcal{H}(\theta,v) = \mathcal{E}(\theta) + \tfrac{1}{2}v^T\Sigma^{-1}v$$
where $\mathcal{E}(\theta)=-\log\tilde{p}(\theta)$. A trajectory of $L$ leapfrog integration steps is used as the proposal, followed by a Metropolis accept/reject step with probability $\min(1, \exp[-\mathcal{H}(\theta^*,v^*)+\mathcal{H}(\theta,v)])$.

### Why it matters
By following gradient-guided trajectories in phase space, HMC makes large, nearly independent proposals with high acceptance rates, dramatically outperforming random-walk methods in high dimensions. The leapfrog integrator is symplectic (volume-preserving and time-reversible), guaranteeing that the proposal is exactly reversible and the MH step corrects for discretisation error. HMC is the workhorse of modern probabilistic programming (e.g., Stan, PyMC).

### Key hyperparameters
- Step size $\eta$: target 40–80% acceptance; too large → divergences; too small → slow exploration.
- Number of leapfrog steps $L$: chosen adaptively by NUTS to avoid U-turns.
- Inverse mass matrix $\Sigma$: estimated from warm-up samples to precondition the geometry.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]