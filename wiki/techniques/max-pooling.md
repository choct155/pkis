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
extends:
- translation-equivariance
id: pkis:technique:max-pooling
instantiates:
- simple-cells-complex-cells-v1
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch09
specializes:
- pooling-layer
tags:
- pooling
- translation invariance
- downsampling
- CNN
- spatial hierarchy
title: Max Pooling
understanding: 0
---

## Definition
$$z_{i,j} = \max_{(m,n)\in\mathcal{N}(i,j)} a_{m,n}$$

**Max pooling** replaces a rectangular neighborhood $\mathcal{N}$ of detector activations with their maximum value, summarising the presence of a feature while discarding exact location.

### Why it matters
Max pooling provides approximate translation invariance, reduces spatial resolution (and thus computation in subsequent layers), and can be viewed as imposing an infinitely strong prior that feature presence rather than precise location matters. It also enables the network to handle variable-size inputs when pooling regions scale with input size.

### Relationship to complex cells
The operation is biologically motivated by V1 *complex cells*, which respond to a feature regardless of small positional shifts; the max aggregates over a quadrature-pair-like set of detector responses.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[simple-cells-complex-cells-v1]] — instantiates: Motivated by complex-cell pooling over quadrature-pair simple-cell responses.
- [[translation-equivariance]] — extends: Max pooling converts equivariance into approximate local translation invariance.
- [[pooling-layer]] — specializes
[To be populated during integration]