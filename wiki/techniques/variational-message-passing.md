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
- machine-learning
- probabilistic-graphical-models
id: pkis:technique:variational-message-passing
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch10
tags:
- message-passing
- mean-field
- Markov-blanket
- conjugate-exponential
- variational-inference
title: Variational Message Passing
understanding: 0
---

## Definition
A distributed implementation of mean-field variational inference on conjugate-exponential directed graphical models. The optimal update for node $j$,
$$\ln q_j^*(x_j) = \mathbb{E}_{\text{MB}(j)}[\ln p(x_j|\text{pa}_j)] + \sum_{c\in\text{ch}(j)}\mathbb{E}_{\text{MB}(j)}[\ln p(x_c|\text{pa}_c)] + \text{const}$$
depends only on variables in the **Markov blanket** of node $j$ (parents, children, co-parents). This locality permits the factor updates to be cast as messages passed between neighboring nodes in the graph.

### Why it matters
Enables general-purpose software (e.g., Infer.NET) that performs variational inference automatically for any model expressible as a conjugate-exponential directed graph, with the ELBO also computable locally. Scales to large networks and parallels the sum-product algorithm structurally.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]