---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- physics
- statistics
id: pkis:result:liouvilles-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- hybrid-monte-carlo
related_concepts: []
sources:
- bishop-prml-ch11
tags:
- hamiltonian-dynamics
- mcmc
- phase-space
- volume-preservation
title: Liouville's Theorem (Phase-Space Volume Preservation)
understanding: 0
uses:
- hamiltonian-classical-mechanics
---

## Definition
For a Hamiltonian system with equations of motion
$$\frac{dz_i}{d\tau} = \frac{\partial H}{\partial r_i}, \qquad \frac{dr_i}{d\tau} = -\frac{\partial H}{\partial z_i},$$
the divergence of the phase-space flow field vanishes identically:
$$\operatorname{div}\mathbf{V} = \sum_i\left(\frac{\partial}{\partial z_i}\frac{dz_i}{d\tau} + \frac{\partial}{\partial r_i}\frac{dr_i}{d\tau}\right) = \sum_i\left(\frac{\partial^2 H}{\partial z_i \partial r_i} - \frac{\partial^2 H}{\partial r_i \partial z_i}\right) = 0.$$
Hence Hamiltonian flow preserves phase-space volume for all time.

### Why it matters
Liouville's theorem, together with the conservation of $H$ along trajectories, implies that the canonical distribution $p(\mathbf{z},\mathbf{r}) \propto \exp(-H)$ is invariant under Hamiltonian dynamics. The leapfrog integrator preserves this property exactly at the discrete level, which is what makes the Metropolis correction in Hybrid Monte Carlo both valid and efficient.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hybrid-monte-carlo]] — prerequisite-of
- [[hamiltonian-classical-mechanics]] — uses
[To be populated during integration]