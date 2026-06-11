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
id: pkis:concept:sparse-interactions-cnn
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch09
tags:
- sparse connectivity
- receptive field
- CNN
- inductive bias
- efficiency
title: Sparse Interactions (CNNs)
understanding: 0
---

## Definition
A convolutional layer has **sparse interactions** (also called sparse connectivity or sparse weights) when each output unit is connected to only $k \ll m$ input units via a local kernel, reducing parameters from $O(m \times n)$ to $O(k \times n)$ and runtime proportionally.

Using a small kernel that is much narrower than the input means each output unit detects a local feature while deeper layers build up wider *effective receptive fields* through composition.

### Why it matters
Sparse connectivity is one of the three core efficiency/inductive-bias arguments for CNNs. It reduces memory, speeds up inference, and encodes the prior that nearby inputs are more informative for local feature detection than distant ones.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]