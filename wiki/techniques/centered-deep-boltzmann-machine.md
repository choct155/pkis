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
- deep-learning
- generative-models
- optimisation
id: pkis:technique:centered-deep-boltzmann-machine
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch20
tags:
- reparameterisation
- conditioning
- Boltzmann-machine
- joint-training
title: Centered Deep Boltzmann Machine
understanding: 0
---

## Definition
A reparametrisation of the Boltzmann machine energy that subtracts a fixed offset vector $\boldsymbol{\mu}$ from all unit states:
$$E'(\mathbf{x};U,\mathbf{b})=-(\mathbf{x}-\boldsymbol{\mu})^{\top}U(\mathbf{x}-\boldsymbol{\mu})-(\mathbf{x}-\boldsymbol{\mu})^{\top}\mathbf{b},$$
where $\boldsymbol{\mu}$ is chosen so that $\mathbf{x}-\boldsymbol{\mu}\approx\mathbf{0}$ at initialisation. The representational capacity is unchanged, but the Hessian of the cost becomes better conditioned, enabling joint training of deep Boltzmann machines without greedy layer-wise pretraining.

### Why it matters
The centering trick (Montavon & Müller, 2012) is equivalent to the enhanced gradient technique (Cho et al., 2011) and resolves the numerical instability that makes naive joint DBM training fail. It obtains state-of-the-art log-likelihood and sample quality, demonstrating that appropriate reparametrisation can transform an untrainable model into a trainable one.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]