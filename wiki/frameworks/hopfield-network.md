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
- deep-learning
- statistical-learning
id: pkis:framework:hopfield-network
instantiates:
- associative-memory
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch42
specializes:
- ising-model
- neural-networks
tags:
- hopfield-network
- feedback-network
- recurrent-network
- energy-based-model
- hebbian-learning
- attractor-network
title: Hopfield Network
understanding: 0
uses:
- lyapunov-function
---

## Definition
A **Hopfield network** is a fully connected *feedback* (recurrent) network of $I$ neurons with **symmetric** weights ($w_{ij}=w_{ji}$) and no self-connections ($w_{ii}=0$). Each neuron updates with a threshold (binary, $x_i\in\{-1,1\}$) or sigmoid/tanh (continuous, $x_i\in(-1,1)$) activation applied to its activation $a_i=\sum_j w_{ij}x_j$. Updates may be **synchronous** (all neurons at once) or **asynchronous** (one at a time); the model's behaviour can be sensitive to this choice.

Desired memories $\{\mathbf{x}^{(n)}\}$ are typically installed by the one-shot **Hebb rule** (sum of outer products):
$$w_{ij} = \eta \sum_n x_i^{(n)} x_j^{(n)},$$
so that each memory becomes a stable state (attractor) of the dynamics.

### Two faces of one model
A Hopfield network has two classic uses. As an **associative memory**, its attractors store patterns and its dynamics perform pattern completion and error correction. As an **optimizer**, weights are hand-designed so that the network's energy equals the objective of a constraint-satisfaction problem (e.g. the travelling salesman problem of Hopfield & Tank, 1985), and settling approximately minimizes it.

### Why it matters
The Hopfield network is the canonical *energy-based, attractor* neural model: it shows how a simple symmetric recurrent architecture with local Hebbian learning yields content-addressable memory and graceful, brain-like degradation, and it bridges neural computation, statistical physics (spin glasses), and optimization.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[neural-networks]] — specializes: It is the canonical fully-connected, symmetric-weight feedback (recurrent) neural network.
- [[ising-model]] — specializes: The Hopfield energy is an Ising Hamiltonian (w plays the role of couplings J); continuous Hopfield updates are its mean-field equations.
- [[lyapunov-function]] — uses: Convergence and the attractor/optimizer interpretation rest on the variational free energy being a Lyapunov function of the dynamics.
- [[associative-memory]] — instantiates: A Hopfield network is the canonical realization of a content-addressable associative memory via attractor pattern-completion.
[To be populated during integration]