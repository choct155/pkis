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
id: pkis:technique:leapfrog-integrator
instantiates:
- liouvilles-theorem
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- hybrid-monte-carlo
- detailed-balance
related_concepts: []
sources:
- bishop-prml-ch11
- murphy-pml2-advanced-ch12
tags:
- numerical-integration
- hamiltonian-dynamics
- volume-preserving
- mcmc
title: Leapfrog Integrator
understanding: 0
uses:
- hamiltonian-classical-mechanics
- hamiltonian-mechanics-sampling
---

## Definition
The leapfrog (Störmer-Verlet) integrator discretises Hamiltonian dynamics while exactly preserving phase-space volume and maintaining time-reversibility:
$$\hat{r}_i(\tau+\tfrac{\epsilon}{2}) = \hat{r}_i(\tau) - \tfrac{\epsilon}{2}\frac{\partial E}{\partial z_i}(\hat{\mathbf{z}}(\tau))$$
$$\hat{z}_i(\tau+\epsilon) = \hat{z}_i(\tau) + \epsilon\,\hat{r}_i(\tau+\tfrac{\epsilon}{2})$$
$$\hat{r}_i(\tau+\epsilon) = \hat{r}_i(\tau+\tfrac{\epsilon}{2}) - \tfrac{\epsilon}{2}\frac{\partial E}{\partial z_i}(\hat{\mathbf{z}}(\tau+\epsilon)).$$
Each update shears a region of phase space without changing its volume (Liouville's theorem holds exactly for the discrete map).

### Why it matters
Volume preservation and time-reversibility are precisely the properties needed to establish detailed balance in Hybrid Monte Carlo. The integrator's $O(\epsilon^2)$ local error means the Metropolis correction step has high acceptance even for moderately large $\epsilon$, enabling efficient large-step proposals that are essential for low-autocorrelation MCMC.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[detailed-balance]] — prerequisite-of
- [[hamiltonian-mechanics-sampling]] — uses
- [[hamiltonian-classical-mechanics]] — uses
- [[hybrid-monte-carlo]] — prerequisite-of
- [[liouvilles-theorem]] — instantiates
[To be populated during integration]