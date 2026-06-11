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
id: pkis:technique:transpose-convolution
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch09
tags:
- backpropagation
- upsampling
- autoencoder
- encoder-decoder
- gradient
title: Transpose Convolution (Deconvolution)
understanding: 0
uses:
- strided-convolution
- backpropagation
- autoencoder
---

## Definition
The **transpose convolution** (sometimes called deconvolution) computes the gradient of a loss $J$ with respect to the input $V$ of a strided convolution:
$$h(\mathbf{K},\mathbf{G},s)_{i,j,k} = \frac{\partial J}{\partial V_{i,j,k}} = \sum_{\substack{l,m:\,(l-1)s+m=j}}\sum_{\substack{n,p:\,(n-1)s+p=k}}\sum_q K_{q,i,m,p}\,G_{q,l,n}$$

It maps from the output space back to the input space, effectively upsampling the gradient tensor.

### Why it matters
Transpose convolution is required for backpropagation through convolutional layers, and is also the decoding primitive in encoder–decoder architectures (autoencoders, U-Net, FCNs) where spatial resolution must be restored. Together with forward convolution and the kernel-gradient operation, it forms the complete computational triple needed to train any feedforward CNN.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[autoencoder]] — uses
- [[backpropagation]] — uses
- [[strided-convolution]] — uses
[To be populated during integration]