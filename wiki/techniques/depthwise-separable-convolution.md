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
- computer-vision
id: pkis:technique:depthwise-separable-convolution
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch14
tags:
- efficient-cnn
- mobilenet
- parameter-efficiency
- pointwise-convolution
title: Depthwise Separable Convolution
understanding: 0
---

## Definition
A factorization of standard convolution into two sequential steps:
1. **Depthwise convolution**: apply a separate $H\times W$ spatial filter to each input channel independently.
2. **Pointwise ($1\times1$) convolution**: mix the $C$ depthwise outputs into $D$ output channels.
$$z_{i,j,d} = b_d + \sum_{c=0}^{C-1} w'_{c,d}\!\left(\sum_{u,v} x_{i+u,j+v,c}\,w_{u,v}\right)$$
For a $k\times k$ filter mapping $C\to D$ channels, the parameter count drops from $k^2 CD$ (standard) to $k^2 C + CD$ (separable), a reduction by roughly a factor of $D/k^2$ — e.g., ~8–9× for $k=3, D=256$.

### Why it matters
Depthwise separable convolution is the core building block of lightweight architectures (MobileNet, EfficientNet) enabling deployment on mobile and edge devices with minimal accuracy loss.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]