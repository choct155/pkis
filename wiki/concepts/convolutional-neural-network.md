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
id: pkis:concept:convolutional-neural-network
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch14
tags:
- convolution
- weight-sharing
- translation-invariance
- image-classification
title: Convolutional Neural Network (CNN)
understanding: 0
---

## Definition
A neural network architecture in which the dense matrix-vector product of each layer is replaced by a convolution operation:
$$z_{i,j,d} = b_d + \sum_{u=0}^{H-1}\sum_{v=0}^{W-1}\sum_{c=0}^{C-1} x_{si+u,\,sj+v,\,c}\;w_{u,v,c,d}$$
where $w_{u,v,c,d}$ is a small learned filter (kernel), $s$ is the stride, and the output $z_{i,j,d}$ is a **feature map**. The key properties are **weight sharing** across spatial locations (enabling translation equivariance) and **local connectivity** (each output depends only on a small receptive field), dramatically reducing parameters relative to a fully connected layer.

### Why it matters
CNNs are the dominant architecture for image, audio, and time-series data because translation invariance/equivariance is a strong inductive bias that matches the structure of natural signals; this was spectacularly demonstrated when AlexNet halved the ImageNet error rate in 2012.

### Key design choices
Filters are typically 3×3 or 5×5; multiple filters produce multiple channels; stacking layers enlarges the effective receptive field; alternating with pooling layers achieves spatial invariance.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]