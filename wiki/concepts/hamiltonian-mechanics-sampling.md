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
- physics
- statistics
- machine-learning
id: pkis:concept:hamiltonian-mechanics-sampling
instantiates:
- hamiltonian-classical-mechanics
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- detailed-balance
related_concepts: []
sources:
- murphy-pml2-advanced-ch12
tags:
- hamiltonian-dynamics
- phase-space
- potential-energy
- kinetic-energy
- mcmc
title: Hamiltonian Mechanics for Sampling
understanding: 0
---

## Definition
The application of classical Hamiltonian mechanics to MCMC, defining phase space $\mathcal{X} = (\theta, v) \in \mathbb{R}^{2D}$ and total energy:
$$\mathcal{H}(\theta, v) = \mathcal{E}(\theta) + \mathcal{K}(v) = -\log\tilde{p}(\theta) + \tfrac{1}{2}v^T\Sigma^{-1}v$$
Hamilton's equations govern the flow:
$$\frac{d\theta}{dt} = \frac{\partial\mathcal{H}}{\partial v} = \Sigma^{-1}v, \qquad \frac{dv}{dt} = -\frac{\partial\mathcal{H}}{\partial\theta} = \nabla\log\tilde{p}(\theta)$$
Energy is conserved along trajectories, $d\mathcal{H}/dt = 0$. The canonical distribution $p(\theta,v) \propto e^{-\mathcal{H}(\theta,v)}$ has the desired marginal $p(\theta) \propto e^{-\mathcal{E}(\theta)}$.

### Why it matters
Hamiltonian flow is volume-preserving (Liouville's theorem) and time-reversible. When discretised with the leapfrog integrator and corrected with a Metropolis step, these properties guarantee exact detailed balance. The gradient guidance allows the sampler to follow level sets of constant energy, making proposals that are far away yet energetically consistent, which is the key to HMC's efficiency advantage over random-walk methods.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[detailed-balance]] — prerequisite-of
- [[hamiltonian-classical-mechanics]] — instantiates
[To be populated during integration]