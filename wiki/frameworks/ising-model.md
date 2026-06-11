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
instantiates:
- phase-transition
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- boltzmann-machine
related_concepts: []
sources:
- mackay-itila-ch31
specializes:
- undirected-graphical-models
- markov-random-field
- hopfield-network
- potts-model
tags:
- ising-model
- statistical-physics
- spin-systems
- energy-based-models
- monte-carlo
- phase-transition
title: Ising Model
understanding: 0
uses:
- iterative-proportional-fitting
- exponential-family
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
- [[potts-model]] — specializes
- [[hopfield-network]] — specializes: Hopfield network is a fully connected Ising model
- [[boltzmann-machine]] — prerequisite-of
- [[markov-random-field]] — specializes
- [[exponential-family]] — uses: Ising MLE matches sufficient statistics to model expectations -- the standard exponential-family score equation.
- [[iterative-proportional-fitting]] — uses: IPF performs cyclic coordinate descent on the Ising gradient equations to fit the discrete model.
- [[undirected-graphical-models]] — specializes: An Ising model is a pairwise Markov random field over binary spins with energy = negative log potential.
- [[phase-transition]] — instantiates: The 2D ferromagnetic Ising model is the canonical system exhibiting a temperature-driven phase transition.
[To be populated during integration]

## From Ising Spins to Hopfield Networks
The **Hopfield network** is, formally, an Ising-type spin system repurposed for computation. Its binary states $x_i\in\{-1,1\}$ are spins, its symmetric weights $w_{ij}$ play the role of the couplings $J_{ij}$, and its energy
$$E(\mathbf{x}) = -\tfrac{1}{2}\sum_{m,n} w_{mn}x_m x_n - \sum_n w_{n0} x_n$$
is exactly the Ising Hamiltonian $E(\mathbf{x};J) = -\tfrac{1}{2}\sum_{m,n}J_{mn}x_m x_n - \sum_n h_n x_n$ with $J\to w$ and external field $h\to$ bias. The continuous Hopfield update $x_i=\tanh(\beta a_i)$ is precisely the **mean-field** equation obtained when one approximates this spin system by a separable distribution and minimizes the variational free energy — so Hopfield dynamics *are* mean-field relaxation of an Ising model.

The deep payoff is the capacity result: when too many memories are loaded ($N/I > 0.138$), the Hopfield network's only stable states are uncorrelated **spin-glass** states, and the statistical-physics methods of Amit, Gutfreund & Sompolinsky (1985) used to locate this transition are the same tools developed for disordered Ising spin glasses.