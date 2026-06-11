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
- probability-theory
- machine-learning
id: pkis:concept:multinoulli-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch03
tags:
- categorical
- discrete
- classification
- softmax
title: Multinoulli (Categorical) Distribution
understanding: 0
---

## Definition
The **multinoulli** (or **categorical**) distribution is a distribution over a single discrete variable with $k$ states, parametrized by a probability vector $\mathbf{p} \in [0,1]^{k-1}$ where the $k$-th probability is $1 - \mathbf{1}^\top \mathbf{p}$:
$$P(x = i) = p_i, \quad i = 1,\ldots,k-1; \quad P(x=k) = 1 - \sum_{i=1}^{k-1}p_i.$$
It generalizes the Bernoulli distribution to more than two outcomes and is the natural distribution over category labels.

### Why it matters
The multinoulli distribution is fundamental to multi-class classification, language modelling (next-token prediction), and mixture models where a latent component identity must be sampled. It pairs naturally with the softmax output layer.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]