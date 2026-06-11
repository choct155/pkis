---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
contrasts-with:
- vc-dimension
- curse-of-dimensionality
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- representation-learning
- deep-learning
- statistical-learning-theory
id: pkis:result:exponential-regions-distributed-representation
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch15
tags:
- distributed-representation
- hyperplane-arrangement
- exponential-capacity
- generalization
- vc-theory
title: Exponential Regions from Distributed Binary Features
understanding: 0
uses:
- distributed-representation
- linear-separability
---

## Definition
For a representation that extracts $n$ binary features by thresholding linear functions of a $d$-dimensional input, the number of distinct input regions that can be distinguished is
$$\sum_{j=0}^{d} \binom{n}{j} = O(n^d).$$
This follows from Zaslavsky's (1975) theorem on hyperplane arrangements applied to $n$ half-space boundaries in $\mathbb{R}^d$ (Pascanu et al., 2014).

### Why it matters
The result gives a precise geometric justification for the statistical efficiency of distributed representations: with only $O(nd)$ parameters one can distinguish $O(n^d)$ input regions, whereas a non-distributed (lookup-table) scheme would require $O(n^d)$ examples to cover the same number of regions. It quantitatively explains why neural networks generalise far beyond the number of training examples when using distributed hidden representations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[linear-separability]] — uses
- [[curse-of-dimensionality]] — contrasts-with
- [[vc-dimension]] — contrasts-with: VC dimension remains O(w log w) despite exponential region count
- [[distributed-representation]] — uses
[To be populated during integration]