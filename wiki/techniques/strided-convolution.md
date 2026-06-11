---
aliases: []
also_type: []
analogous-to:
- max-pooling
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
- convolution-operation-nn
id: pkis:technique:strided-convolution
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- transpose-convolution
related_concepts: []
sources:
- goodfellow-deeplearning-ch09
tags:
- stride
- downsampling
- CNN
- transpose convolution
- efficiency
title: Strided Convolution
understanding: 0
uses:
- zero-padding-cnn
---

## Definition
A **strided convolution** with stride $s$ samples the convolution output at every $s$-th spatial position:
$$Z_{i,j,k} = \sum_{l,m,n} V_{l,\,(j-1)\times s+m,\,(k-1)\times s+n}\,K_{i,l,m,n}$$

This is equivalent to computing the full convolution and then downsampling, but is more computationally efficient.

### Why it matters
Stride $>1$ reduces spatial resolution and computational cost downstream, serving as an alternative to pooling for controlled downsampling. The backpropagation gradient through a strided convolution requires a *transpose convolution* (deconvolution) step, relevant for autoencoders and generative models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[zero-padding-cnn]] — uses
- [[transpose-convolution]] — prerequisite-of
- [[max-pooling]] — analogous-to: Both reduce spatial resolution; strided convolution learns the downsampling implicitly.
- [[convolution-operation-nn]] — extends
[To be populated during integration]