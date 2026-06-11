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
- computer-vision
- deep-learning
- preprocessing
id: pkis:technique:local-contrast-normalization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch12
tags:
- normalisation
- preprocessing
- image
- contrast
- separable-convolution
title: Local Contrast Normalization (LCN)
understanding: 0
---

## Definition
Local contrast normalization modifies each pixel $(i,j,k)$ of an image by subtracting a local mean $\mu_{i,j}$ and dividing by a local standard deviation $\sigma_{i,j}$ computed over a spatial neighbourhood $\mathcal{N}(i,j)$:
$$X'_{i,j,k} = \frac{X_{i,j,k} - \mu_{i,j}}{\max(\epsilon,\, \sigma_{i,j})}.$$
Neighbourhood statistics may use uniform or Gaussian spatial weights; colour channels may be processed jointly or separately. LCN can be implemented efficiently via separable convolution for the mean and standard deviation maps, and is differentiable, making it usable as a non-linearity inside a network.

### Why it matters
Unlike global contrast normalisation, LCN highlights local edges and textures within dark or bright regions, encoding the *relative* contrast that drives early visual processing. It closely mirrors classical centre-surround receptive field responses in mammalian retinal and cortical neurons.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]