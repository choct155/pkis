---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- statistical-learning
- information-theory
id: pkis:framework:ising-model
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch31
tags:
- ising-model
- statistical-physics
- spin-systems
- energy-based-models
- monte-carlo
- phase-transition
title: Ising Model
understanding: 0
---

## Definition
An **Ising model** is a system of $N$ spins, each $x_n \in \{-1, +1\}$, coupled along the edges of a graph. Writing $(m,n) \in \mathcal{N}$ for neighbouring spins and $J_{mn} = J$ for neighbours (else $0$), the energy of a configuration is

$$E(x; J, H) = -\left[\tfrac{1}{2}\sum_{m,n} J_{mn} x_m x_n + \sum_n H x_n\right],$$

with $H$ an applied field. The factor $\tfrac12$ corrects for each pair being counted twice. At temperature $T$ the equilibrium distribution is the Boltzmann distribution $P(x \mid \beta) = \exp[-\beta E(x)]/Z(\beta)$, with $\beta = 1/k_B T$.

### Ferromagnet vs. antiferromagnet
If $J > 0$ (ferromagnet) neighbours prefer to agree; if $J < 0$ (antiferromagnet) they prefer to disagree. The ferromagnetic rectangular model has two ground states (all $+1$, all $-1$). On a triangular antiferromagnet no configuration can satisfy every coupling — the system is *frustrated* and retains non-zero entropy at $T=0$.

### Why it matters
The Ising model is the canonical solvable system with a genuine phase transition, and by universality its critical behaviour transfers to many other 2D systems. Generalizing $J_{mn}$ and $H$ to arbitrary couplings $h_n$ yields spin glasses, Hopfield networks, and Boltzmann machines, making it a direct ancestor of energy-based learning models. It is also a standard testbed for Monte Carlo methods such as Gibbs sampling and the Metropolis algorithm.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]