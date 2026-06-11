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
id: pkis:concept:rectified-linear-unit
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch01
tags:
- activation-function
- nonlinearity
- vanishing-gradients
- neural-networks
title: Rectified Linear Unit (ReLU)
understanding: 0
---

## Definition
The rectified linear unit activation function is defined as:
$$f(z) = \max(0, z)$$

It outputs its input directly when positive and zero otherwise, introducing piecewise-linear nonlinearity with a sub-gradient of 1 in the active region and 0 elsewhere.

### Why it matters
ReLU largely solved the **vanishing gradient problem** that plagued sigmoid/tanh networks: because the gradient does not saturate for positive inputs, gradients flow back through many layers without exponential decay. Combined with modern initialization and normalization, ReLU enabled the training of very deep supervised networks and became the de-facto default activation function.

### Biological inspiration vs. engineering
The ReLU was influenced by neuroscience (half-wave rectification in neurons) but is a deliberate simplification: Nair & Hinton (2010) and Glorot et al. (2011) showed it outperforms biologically closer models, illustrating the pragmatic rather than literal neuroscientific stance of modern deep learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]