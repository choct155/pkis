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
- computer-vision
id: pkis:concept:translation-equivariance-invariance
instantiates:
- inductive-bias
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch14
tags:
- symmetry
- inductive-bias
- weight-sharing
- pooling
- image-classification
title: Translation Equivariance and Invariance in CNNs
understanding: 0
uses:
- pooling-layer
---

## Definition
**Equivariance**: a function $f$ is equivariant to translation $T_\delta$ if $f(T_\delta x) = T_\delta f(x)$ — translating the input translates the output feature map by the same amount. Standard convolutional layers are equivariant because the same filter is applied at every location via weight sharing.

**Invariance**: a function $f$ is invariant to $T_\delta$ if $f(T_\delta x) = f(x)$ — the output is unchanged regardless of where the feature appears. Pooling layers (especially global average/max pooling) achieve invariance by aggregating over spatial positions.

### Why it matters
The interplay between equivariance (convolution) and invariance (pooling) is the central architectural principle of CNNs: lower layers localize *where* features occur (equivariant), while higher layers recognize *whether* they occur (invariant). This inductive bias encodes the known statistical structure of natural images and is responsible for the dramatic sample-efficiency of CNNs over fully connected networks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[inductive-bias]] — instantiates: Translation symmetry is encoded as an inductive bias via weight sharing and pooling
- [[pooling-layer]] — uses: Max/average pooling achieves spatial invariance over the receptive field
[To be populated during integration]