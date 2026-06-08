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
id: pkis:framework:boltzmann-machine
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch43
tags:
- boltzmann-machine
- stochastic-hopfield-network
- energy-based-model
- generative-model
- gibbs-sampling
- hinton-sejnowski
title: Boltzmann Machine
understanding: 0
---

## Definition
A **Boltzmann machine** (Hinton and Sejnowski, 1986) is a *stochastic* Hopfield network: a fully connected network of binary units $x_i \in \{-1,+1\}$ with symmetric weights $w_{ij}=w_{ji}$ that explicitly realizes the energy-based probability distribution
$$P(x\mid W) = \frac{1}{Z(W)}\exp\!\left[\tfrac{1}{2}\,x^{\mathsf T} W x\right],\qquad Z(W)=\sum_{x}\exp\!\left[\tfrac{1}{2}\,x^{\mathsf T} W x\right].$$
Whereas the deterministic Hopfield network *descends* the energy $E(x)=-\tfrac{1}{2}x^{\mathsf T} W x$ to a fixed point, the Boltzmann machine *samples* from the full Gibbs distribution.

### Stochastic activity rule
After computing the activation $a_i = \sum_j w_{ij} x_j$, set
$$x_i = +1 \text{ with probability } \frac{1}{1+e^{-2a_i}},\quad \text{else } x_i = -1.$$
Iterating this update over units is exactly **Gibbs sampling** of $P(x\mid W)$: each unit is resampled from its conditional given the others. After many sweeps the network visits configurations with frequency proportional to $e^{-E(x)}$, turning the recurrent net into a generative model of binary data rather than a mere attractor memory.

### Why it matters
The Boltzmann machine reframes a neural network as a Markov-random-field generative model whose parameters can be fit by maximum likelihood. It is the bridge from associative memory to *learning* the statistics of an environment, and the conceptual ancestor of restricted Boltzmann machines, contrastive-divergence training, and modern energy-based and deep generative models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]