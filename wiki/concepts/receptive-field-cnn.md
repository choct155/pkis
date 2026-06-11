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
- neuroscience
id: pkis:concept:receptive-field-cnn
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch09
tags:
- receptive field
- spatial context
- CNN
- hierarchy
- depth
title: Receptive Field (CNNs)
understanding: 0
uses:
- sparse-interactions-cnn
- feature-detection-vision
---

## Definition
The **receptive field** of a unit in a convolutional network is the region of the input space that can affect that unit's activation. For a unit in layer $\ell$, the receptive field size grows with depth: a chain of $\ell$ layers with kernel width $k$ and stride 1 yields a receptive field of size $1 + \ell(k-1)$.

Shallower units respond to small local patches; deeper units effectively integrate information over much larger input regions, enabling hierarchical feature composition.

### Why it matters
Receptive field size determines what spatial context a unit can use. Designing architectures with appropriate receptive fields — via kernel size, stride, dilation, and depth — is central to matching the CNN's inductive bias to the task's spatial scale.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[feature-detection-vision]] — uses
- [[sparse-interactions-cnn]] — uses
[To be populated during integration]