---
aliases: []
also_type: []
analogous-to:
- regularization
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
id: pkis:concept:parameter-sharing-cnn
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch09
tags:
- tied weights
- translation equivariance
- CNN
- parameter efficiency
title: Parameter Sharing (CNNs)
understanding: 0
uses:
- convolution-operation-nn
- translation-equivariance
---

## Definition
**Parameter sharing** (or *tied weights*) in a convolutional layer means the same kernel weights are reused at every spatial position of the input, so learning one kernel teaches the detector for all positions simultaneously.

Instead of one weight per (input unit, output unit) pair, the network stores one weight per (kernel position, channel pair), reducing the parameter count from $O(m \times n)$ to $O(k \times c_{\text{in}} \times c_{\text{out}})$.

### Why it matters
Parameter sharing encodes translation equivariance as a hard constraint, dramatically reduces the number of free parameters, and improves statistical efficiency — the network needs far fewer examples to learn a feature because evidence is pooled over all spatial locations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[regularization]] — analogous-to
- [[translation-equivariance]] — uses
- [[convolution-operation-nn]] — uses
[To be populated during integration]