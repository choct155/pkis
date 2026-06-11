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
- sequence-modeling
- NLP
id: pkis:concept:recursive-neural-network
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch10
tags:
- tree-structured
- recursive
- parse-tree
- NLP
- composition
title: Recursive Neural Network (Tree-Structured)
understanding: 0
---

## Definition
A **recursive neural network** applies the same parameterized composition function $f_\theta$ at each internal node of a *tree-structured* computational graph, rather than along a linear chain as in RNNs. For a binary tree over a sequence of length $\tau$, depth is $O(\log \tau)$ compared to the $O(\tau)$ depth of a chain RNN, reducing the longest gradient path by orders of magnitude.

Tree structure can be fixed (balanced binary tree), externally supplied (parse tree from an NLP parser), or inferred by the model itself.

### Why it matters
Recursive nets are particularly natural for hierarchically structured data: parse trees, arithmetic expressions, scene graphs. The logarithmic depth mitigates long-range dependency issues and has been successfully exploited in sentiment analysis (Socher et al., 2011) and relation modeling. Tensor/bilinear composition functions (Socher et al., 2013) extend representational power beyond affine + nonlinearity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]