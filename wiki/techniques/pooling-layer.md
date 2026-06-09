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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- deep-learning
id: pkis:technique:pooling-layer
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch21
tags:
- convolutional-network
- downsampling
- subsampling
- spatial-invariance
title: Pooling Layer
understanding: 0
---

## Definition
A layer in a convolutional network that summarizes a set of adjacent units from the preceding layer with a single value. It operates like a convolution layer with a kernel size l and stride s, but the operation is fixed rather than learned and there is typically no activation function. Average-pooling computes the mean of its l inputs (equivalent to convolution with uniform kernel [1/l,...,1/l]); with l = s it coarsens resolution — downsamples — by a factor of s, facilitating multiscale recognition and reducing weights in subsequent layers. Max-pooling computes the maximum of its l inputs and acts as a kind of logical disjunction, signaling that a feature exists somewhere in the unit's receptive field. In the mammalian-vision analogy, a pooling layer's output corresponds to a 'complex cell' invariant to small spatial translations, whereas a convolution output corresponds to a 'simple cell.'

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]