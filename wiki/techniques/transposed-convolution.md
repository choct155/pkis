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
id: pkis:technique:transposed-convolution
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch14
tags:
- upsampling
- encoder-decoder
- segmentation
- generative-models
title: Transposed Convolution (Deconvolution)
understanding: 0
---

## Definition
An operation that produces a *larger* spatial output from a *smaller* input by placing a weighted copy of the kernel at each input location and summing overlapping contributions:
```
Y[i:i+h, j:j+w] += X[i,j] * K   # for all (i,j)
```
Formally, if standard convolution corresponds to multiplication by matrix $C$, transposed convolution corresponds to multiplication by $C^T$. For a kernel of size $h\times w$, a strided transposed convolution upsamples the spatial resolution by the stride factor.

### Why it matters
Transposed convolution is the standard learned upsampling primitive in encoder–decoder architectures (U-Net, segmentation decoders, generative models), allowing the network to learn how to map low-resolution feature maps back to full image resolution.

### Note on terminology
"Deconvolution" is sometimes used as a synonym but is technically incorrect; true deconvolution recovers the original signal from a known blurring kernel.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]