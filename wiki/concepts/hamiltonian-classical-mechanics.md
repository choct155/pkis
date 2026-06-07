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
coverage: 0
date_created: '2026-06-07'
date_updated: '2026-06-07'
domain:
- bayesian-stats
- optimization
id: pkis:concept:hamiltonian-classical-mechanics
knowledge_type: concept
maturity: evolving
needs_canonical_source: true
prerequisite-of:
- hmc
related_concepts: []
sources: []
tags:
- classical-mechanics
- conservation-laws
- symplectic-geometry
- energy
- HMC
- optimal-control
- phase-space
title: Hamiltonian (Classical Mechanics)
understanding: 0
---

## Definition
The Hamiltonian H is a function describing total energy of a physical system as a function of position q and momentum p:

H(q, p) = T(p) + V(q)

T = kinetic energy (energy of motion)
V = potential energy (energy stored in position)

## Hamilton's Equations of Motion

dq/dt = ∂H/∂p    (position changes according to momentum)
dp/dt = −∂H/∂q   (momentum changes according to negative position gradient)

Key property: conservation. In a closed system, H remains constant along trajectories. The system trades kinetic and potential energy but total never changes. Trajectories live on surfaces of constant total energy in the joint position-momentum space.

## Symplectic Structure

Hamiltonian dynamics preserves a geometric property of the joint position-momentum space called symplecticity — it preserves phase space volumes in a specific sense (not Euclidean volume). This has two consequences for HMC:
(1) Detailed balance is satisfied exactly → stationary distribution is the target posterior
(2) The leapfrog integrator, being symplectic, approximately conserves energy in a bounded way rather than accumulating drift

## To-Do: Mechanical Conservation Example

Work through a concrete numerical example: two-parameter posterior, trace a leapfrog trajectory step by step, verify energy approximately conserved while position moves far across posterior surface. Makes symplectic property concrete.

## Connections Beyond HMC

- Optimal control: Pontryagin maximum principle uses Hamiltonian structure to characterize optimal trajectories
- Quantum mechanics: quantum Hamiltonian operator generates time evolution of quantum states
- Normalizing flows: Hamiltonian-based flows construct volume-preserving transformations
- Neural network geometry: recent work connects loss landscape geometry to Hamiltonian structures

## Mapping to HMC Sampling Context

Physical concept → Sampling analog:
Position q → Model parameters θ
Potential energy V(q) → Negative log posterior −log p(θ|y)
Momentum p → Auxiliary variable drawn fresh N(0, M) each trajectory
Kinetic energy T(p) → ½ pᵀM⁻¹p
Conservation of H → Staying in the typical set of the posterior

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hmc]] — prerequisite-of: Hamiltonian dynamics is the mechanism HMC simulates
[To be populated during integration]

## Needs Canonical Source
This stub was created without a source. Suggested references:

**Already in corpus:**
[none in corpus]

**External candidates (Semantic Scholar):**
[none found]