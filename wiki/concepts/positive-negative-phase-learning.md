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
- probabilistic-graphical-models
- deep-learning
id: pkis:concept:positive-negative-phase-learning
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch18
tags:
- partition-function
- undirected-models
- energy-based-models
- MCMC-training
title: Positive and Negative Phase of Learning
understanding: 0
---

## Definition
The gradient of the log-likelihood for an undirected model decomposes as:
$$\nabla_\theta \log p(x;\theta) = \nabla_\theta \log \tilde{p}(x;\theta) - \mathbb{E}_{x \sim p(x)}\nabla_\theta \log \tilde{p}(x;\theta)$$
where the first term is the **positive phase** (pushes up on the energy of data points, equivalently increases $\log\tilde{p}$ at data) and the second term is the **negative phase** (pushes down by decreasing $\log\tilde{p}$ at model samples, equivalently increases $\log Z$). The key difficulty is that the negative phase requires samples from the model distribution, whose partition function is intractable.

### Why it matters
This decomposition is the foundation for all MCMC-based training algorithms for undirected models (CD, PCD/SML) and gives an energy-based interpretation: the model must simultaneously learn to assign low energy to the training data and high energy to everything else. The analogy to dreaming (Crick & Mitchison, 1983) connects the negative phase to biological sleep.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]