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
id: pkis:concept:locally-connected-layer
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch09
tags:
- unshared convolution
- local connectivity
- spatial specificity
- CNN variants
title: Locally Connected Layer (Unshared Convolution)
understanding: 0
---

## Definition
A **locally connected layer** (unshared convolution) uses the same local connectivity pattern as a convolutional layer but assigns independent weights to each spatial location:
$$Z_{i,j,k} = \sum_{l,m,n} V_{l,\,j+m-1,\,k+n-1}\,W_{i,j,k,l,m,n}$$

Unlike convolution, the weight tensor $W$ has separate entries for every output position $(j,k)$, so no parameter is shared across space.

### Why it matters
Locally connected layers are appropriate when spatial symmetry cannot be assumed — e.g., detecting a mouth at the bottom of a face image. They bridge pure convolution (maximal sharing) and full connectivity (no sharing), at the cost of more parameters and weaker generalization across positions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]