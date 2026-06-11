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
extends:
- convolution-operation-nn
id: pkis:concept:tiled-convolution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch09
specializes:
- locally-connected-layer
tags:
- tiled convolution
- parameter sharing
- CNN variants
- learned invariance
title: Tiled Convolution
understanding: 0
uses:
- max-pooling
---

## Definition
**Tiled convolution** cycles through a set of $t$ distinct kernels as the filter moves across space, so position $(j,k)$ uses kernel $(j\bmod t,\; k\bmod t)$:
$$Z_{i,j,k} = \sum_{l,m,n} V_{l,\,j+m-1,\,k+n-1}\,K_{i,l,m,n,\,j\%t+1,\,k\%t+1}$$

This is a middle ground between standard convolution ($t=1$, full sharing) and locally connected layers ($t=$ output width, no sharing).

### Why it matters
When combined with max-pooling, tiled convolution allows adjacent spatial positions to be processed by different filters; pooling over these filters then confers invariance to whatever transformations those filters capture, generalising beyond pure translation invariance.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[max-pooling]] — uses: Tiled conv + max-pool yields invariance to learned transformations.
- [[locally-connected-layer]] — specializes
- [[convolution-operation-nn]] — extends
[To be populated during integration]