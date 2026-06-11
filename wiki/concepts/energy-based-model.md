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
- machine-learning
- probabilistic-modeling
- statistical-physics
id: pkis:concept:energy-based-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch16
- murphy-pml2-advanced-ch24
tags:
- graphical-models
- undirected-models
- deep-learning
- boltzmann-machine
- partition-function
title: Energy-Based Model (EBM)
understanding: 0
---

## Definition
$$\tilde{p}(\mathbf{x}) = \exp(-E(\mathbf{x})), \quad p(\mathbf{x}) = \frac{\exp(-E(\mathbf{x}))}{Z}$$

An undirected probabilistic model in which the unnormalized probability of every configuration is guaranteed positive by defining it as the exponential of a negative scalar *energy function* $E(\mathbf{x})$; lower energy means higher probability.

### Why it matters
The exponential form removes the non-negativity constraint on learning, allowing unconstrained optimization of $E$. It unifies a large family of models (Boltzmann machines, Ising models, restricted Boltzmann machines) under one framework and connects statistical mechanics terminology (energy, partition function, free energy) to probabilistic modeling. The free energy for models with latent variables $h$ is $\mathcal{F}(x) = -\log \sum_h \exp(-E(x,h))$, which collapses the latent variables into an effective energy over visible variables.

### Connections
The product-of-experts interpretation: each additive term in $E(\mathbf{x})$ corresponds to a separate factor (expert) in $\tilde{p}$, so the joint model enforces multiple soft constraints simultaneously via multiplication of probabilities.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]