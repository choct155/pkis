---
aliases: []
also_type: []
analogous-to:
- convolution-of-distributions
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
- signal-processing
id: pkis:concept:convolution-operation-nn
instantiates:
- convolutional-neural-networks
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch09
specializes:
- linear-mapping
tags:
- convolution
- feature-map
- kernel
- cross-correlation
- CNN
title: Convolution Operation (Neural Networks)
understanding: 0
uses:
- toeplitz-matrices
---

## Definition
$$S(i,j) = (I * K)(i,j) = \sum_m \sum_n I(m,n)\,K(i-m,\,j-n)$$

For 2-D inputs, the convolution of input $I$ with kernel $K$ slides the (flipped) kernel over every spatial position and computes an inner product, producing a feature map. In practice, neural-network libraries implement the closely related *cross-correlation* (no kernel flip) and call it convolution: $S(i,j)=\sum_m\sum_n I(i+m,j+n)K(m,n)$.

### Why it matters
Convolution is the core linear operation of CNNs; it exploits spatial structure to drastically reduce parameters and computation relative to dense matrix multiplication, and its discrete form is equivalent to multiplication by a Toeplitz (1-D) or doubly block-circulant (2-D) matrix.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[convolution-of-distributions]] — analogous-to: Neural-network convolution is a discrete, finite-support version of the continuous convolution integral.
- [[linear-mapping]] — specializes
- [[toeplitz-matrices]] — uses: 1-D discrete convolution corresponds to multiplication by a Toeplitz matrix; 2-D convolution to a doubly block-circulant matrix.
- [[convolutional-neural-networks]] — instantiates
[To be populated during integration]