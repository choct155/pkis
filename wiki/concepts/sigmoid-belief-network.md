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
id: pkis:concept:sigmoid-belief-network
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch20
tags:
- directed-model
- binary-variables
- amortised-inference
- historical
title: Sigmoid Belief Network
understanding: 0
---

## Definition
A directed graphical model over binary variables $\mathbf{s}\in\{0,1\}^n$ where each unit $s_i$ is conditionally independent of non-ancestors given its parents, with:
$$p(s_i=1\mid\mathrm{pa}(s_i))=\sigma\!\left(\sum_{j<i}W_{j,i}s_j+b_i\right).$$
Ancestral sampling is efficient; the model is a universal approximator of binary distributions given sufficient depth. Inference over hidden variables given observations is intractable, typically addressed by a learned inference (recognition) network (Helmholtz machine approach).

### Why it matters
Sigmoid belief networks are among the earliest deep directed generative models and directly motivated the Helmholtz machine and wake-sleep algorithm. They illustrate the core challenge of directed latent-variable models: easy sampling, hard inference. Modern reweighted wake-sleep and amortised inference restore competitiveness on benchmarks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]