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
- deep-learning
- statistical-learning
id: pkis:concept:lyapunov-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- hopfield-network-capacity
related_concepts: []
sources:
- mackay-itila-ch42
tags:
- lyapunov-function
- energy-function
- attractor
- basin-of-attraction
- convergence
- dynamical-systems
- steepest-descent
title: Lyapunov Function and Attractor Dynamics
understanding: 0
---

## Definition
A **Lyapunov function** for a dynamical system is a scalar function of state that is bounded below and *never increases* along the system's trajectories (or, in a second flavour, stays exactly constant). Its existence is a powerful guarantee: the dynamics cannot be chaotic and must settle to a fixed point — a local minimum of the Lyapunov function — or to a limit cycle along which it is constant. State space then partitions into **basins of attraction**, one per attractor.

For the **continuous Hopfield network** with symmetric weights, the variational free energy
$$\beta\tilde{F}(\mathbf{x}) = -\tfrac{\beta}{2}\,\mathbf{x}^{T}W\mathbf{x} - \sum_i H_2^{(e)}\!\big[(1+x_i)/2\big]$$
is a Lyapunov function: every component of $\tfrac{d}{dt}x_i$ shares the sign of $\partial\tilde{F}/\partial x_i$, so the dynamics perform (metric-weighted) steepest descent and always converge to a stable fixed point. The proof relies on **symmetric** connections; asymmetric weights or synchronous updates can break convergence (yielding oscillation).

### Why it matters
The Lyapunov/energy view is what *justifies* using a Hopfield network as a memory or optimizer: because settling minimizes a well-defined energy, attractors are predictable and the network is guaranteed to halt. The same idea recurs across MacKay's puzzles (e.g. the conserved 'weight' in the southeast puzzle) and grounds modern energy-based models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hopfield-network-capacity]] — prerequisite-of: The energy/attractor (Lyapunov) framing underlies the notion of stable states whose existence the capacity analysis counts.
[To be populated during integration]