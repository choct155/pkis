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
contrasts-with:
- tangent-propagation
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- computer-vision
id: pkis:technique:convolutional-neural-network-architecture
instantiates:
- convolutional-neural-networks
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch05
specializes:
- feed-forward-neural-network
tags:
- CNN
- translation-invariance
- weight-sharing
- image-recognition
title: Convolutional Neural Network
understanding: 0
uses:
- error-backpropagation
---

## Definition
A feed-forward architecture for structured (e.g. image) data that enforces translation invariance through three mechanisms applied in alternating layers:

1. **Local receptive fields**: each unit connects only to a small spatial patch of the preceding layer.
2. **Weight sharing**: all units within a *feature map* share the same weights, implementing a discrete convolution $z_{j}^{(m)} = h\!\left(\sum_{p,q} w_{pq}^{(m)} x_{j+p,j+q}\right)$.
3. **Subsampling (pooling)**: a pooling layer reduces spatial resolution (e.g. $2\times 2$ average), making responses robust to small shifts.

Multiple convolutional+pooling stages are stacked, increasing invariance and feature abstraction, then followed by fully connected layers with a softmax output for classification.

The full network is trained end-to-end by backpropagation, with shared-weight constraints enforced by accumulating gradients across all units sharing each weight.

### Why it matters
Dramatically reduces parameter count vs. fully connected networks on image data, exploits spatial correlation, and achieves near-human performance on vision benchmarks. The weight-sharing principle extends to 1-D sequences (temporal convolution) and graphs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[error-backpropagation]] — uses
- [[tangent-propagation]] — contrasts-with
- [[feed-forward-neural-network]] — specializes
- [[convolutional-neural-networks]] — instantiates
[To be populated during integration]