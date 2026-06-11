---
aliases: []
also_type: []
applies:
- unsupervised-learning
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- k-means-clustering
- principal-component-analysis
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- representation-learning
generalizes:
- word-embeddings
id: pkis:concept:distributed-vs-one-hot-representations
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch05
tags:
- representation-learning
- distributed-representation
- one-hot
- sparse
- deep-learning
title: Distributed vs. One-Hot Representations
understanding: 0
---

## Definition
A **one-hot (local) representation** encodes each category with a single active unit: $\mathbf{h}\in\{0,1\}^k$, $\|\mathbf{h}\|_1=1$. A **distributed representation** encodes concepts as patterns of activity across many units, allowing $2^n$ distinct concepts to be represented with $n$ binary features.

Formally, if the data has $F$ binary attributes, a one-hot code requires $O(2^F)$ categories while a distributed code requires only $O(F)$ dimensions.

### Why it matters
Distributed representations are a foundational motivation for deep learning: they enable exponentially more efficient generalization across configurations of attributes compared to cluster-based or one-hot schemes. They also support fine-grained similarity comparisons (attribute overlap) that one-hot codes cannot express, underpinning word embeddings, hidden layers, and learned feature spaces.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[principal-component-analysis]] — contrasts-with
- [[k-means-clustering]] — contrasts-with
- [[word-embeddings]] — generalizes
- [[unsupervised-learning]] — applies
[To be populated during integration]