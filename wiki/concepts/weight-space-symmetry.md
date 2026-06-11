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
- neural-networks
id: pkis:concept:weight-space-symmetry
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch05
- goodfellow-deeplearning-ch08
tags:
- symmetry
- weight-space
- model-comparison
- local-minima
title: Weight-Space Symmetry in Neural Networks
understanding: 0
---

## Definition
For a two-layer MLP with $M$ tanh hidden units, distinct weight vectors that produce the same input–output mapping arise from two elementary operations:

1. **Sign-flip symmetry**: negating all incoming and outgoing weights of a hidden unit leaves the mapping unchanged (since $\tanh(-a)=-\tanh(a)$), giving $2^M$ equivalent vectors.
2. **Permutation symmetry**: permuting the $M$ hidden units gives $M!$ equivalent vectors.

The total equivalence factor per hidden layer is $M!\,2^M$, and the overall factor for a deep network is the product over all hidden layers.

### Why it matters
Symmetry inflates the number of equivalent local minima in the loss landscape, complicating Bayesian model comparison (the model evidence must account for these factors) and making naive weight-space integration unreliable. It also implies that mode-finding algorithms may converge to any of the $M!2^M$ equivalent solutions without affecting predictive performance.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]