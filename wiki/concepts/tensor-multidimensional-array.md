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
- linear-algebra
- deep-learning
id: pkis:concept:tensor-multidimensional-array
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch02
tags:
- tensor
- array
- broadcasting
- rank
- shape
title: Tensor (Multi-dimensional Array)
understanding: 0
---

## Definition
$$A_{i,j,k,\ldots}$$

A tensor is a multi-dimensional array of numbers arranged on a regular grid with an arbitrary number of axes; scalars are rank-0, vectors rank-1, matrices rank-2, and higher-rank objects extend this hierarchy.

Tensors provide a uniform notation for the multi-dimensional data structures (feature maps, weight banks) that appear throughout deep learning.

### Why it matters
Deep learning frameworks (TensorFlow, PyTorch) treat tensors as the primitive data type. Understanding rank, shape, and indexing conventions is prerequisite to reading any modern ML implementation. Broadcasting—the implicit replication of lower-rank arrays along new axes—is defined precisely in terms of tensor shapes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]