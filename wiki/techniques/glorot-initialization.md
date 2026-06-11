---
aliases: []
also_type: []
applies:
- vanishing-exploding-gradients
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
- optimization
id: pkis:technique:glorot-initialization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch08
specializes:
- weight-initialization
tags:
- weight-initialization
- deep-learning
- variance
- training
title: Glorot (Xavier) Initialization
understanding: 0
---

## Definition
Glorot & Bengio (2010) proposed *normalized initialization* to keep activation and gradient variances approximately equal across layers. For a layer with $m$ fan-in and $n$ fan-out, weights are sampled from:
$$W_{i,j} \sim U\!\left(-\sqrt{\frac{6}{m+n}},\, \sqrt{\frac{6}{m+n}}\right).$$
The derivation assumes a chain of linear matrix multiplications and requires unit variance of both forward activations and backward gradients, yielding the harmonic compromise $\text{Var}(W) = \frac{2}{m+n}$.

Intuition: initialising too large causes saturation and exploding activations; too small causes vanishing signals — this formula balances the two.

### Why it matters
Glorot initialisation is the default in most deep learning frameworks (Keras, PyTorch). It substantially reduces the number of epochs needed to reach convergence and prevents activation saturation at initialisation. Extensions include He (Kaiming) initialisation for ReLU layers ($\text{Var}=2/m$) and orthogonal initialisation with gain factors.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[vanishing-exploding-gradients]] — applies: balanced variance prevents signal loss at initialisation
- [[weight-initialization]] — specializes
[To be populated during integration]