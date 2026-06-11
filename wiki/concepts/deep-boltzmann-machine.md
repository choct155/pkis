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
- deep-learning
- probabilistic-graphical-models
- generative-models
id: pkis:concept:deep-boltzmann-machine
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch20
tags:
- energy-based-model
- undirected-model
- mean-field
- generative-model
title: Deep Boltzmann Machine (DBM)
understanding: 0
---

## Definition
A deep Boltzmann machine is a fully undirected energy-based model with multiple layers of binary latent variables. For a three-hidden-layer instance the joint distribution is:
$$P\!\left(\mathbf{v},\mathbf{h}^{(1)},\mathbf{h}^{(2)},\mathbf{h}^{(3)};\boldsymbol{\theta}\right)=\frac{1}{Z}\exp\!\left(\mathbf{v}^{\top}\mathbf{W}^{(1)}\mathbf{h}^{(1)}+\mathbf{h}^{(1)\top}\mathbf{W}^{(2)}\mathbf{h}^{(2)}+\mathbf{h}^{(2)\top}\mathbf{W}^{(3)}\mathbf{h}^{(3)}\right).$$
Layers form a bipartite graph (odd vs. even), enabling block Gibbs sampling in two alternating sweeps and exact mean-field fixed-point inference of the posterior. Intuitively, the model passes information bidirectionally through all layers, supporting top-down feedback—unlike DBNs or feed-forward networks.

### Why it matters
DBMs allow variational mean-field inference to capture top-down feedback interactions, making them neuroscientiflcally plausible and applicable to tasks requiring reasoning about missing data. They require greedy layer-wise pre-training (stacking RBMs) and stochastic maximum likelihood for joint training, with extensions such as the centered DBM and multi-prediction DBM addressing joint-training difficulties.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]