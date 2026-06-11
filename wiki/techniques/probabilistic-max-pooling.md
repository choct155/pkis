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
- convolutional-networks
- energy-based-models
id: pkis:technique:probabilistic-max-pooling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch20
tags:
- pooling
- convolutional-rbm
- energy-based
- tractability
title: Probabilistic Max Pooling
understanding: 0
---

## Definition
A pooling operation for convolutional energy-based models that constrains each pooling region of $n$ binary detector units $\{d_i\}$ so that **at most one** may be active at a time, yielding $n+1$ total states. The pooling unit $p=1$ iff any $d_i=1$, and the all-off state is assigned zero energy. This reduces the $2^n$ states that a naive max pooling would require to evaluate.

### Why it matters
Probabilistic max pooling makes pooling tractable within the Boltzmann machine (energy-based) framework, enabling convolutional deep Boltzmann machines. The mutual-exclusivity constraint acts as a regulariser but limits model capacity and makes overlapping pooling regions difficult, restricting performance compared to standard convolutional networks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]