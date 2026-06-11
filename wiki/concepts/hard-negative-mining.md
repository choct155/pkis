---
aliases: []
also_type: []
applies:
- triplet-loss
- contrastive-loss-siamese
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
- machine-learning
- metric-learning
id: pkis:concept:hard-negative-mining
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch16
tags:
- triplet-loss
- curriculum
- sampling
- mining
- deep-metric-learning
title: Hard Negative Mining
understanding: 0
---

## Definition
A training strategy for ranking / metric losses that selects, for each anchor $a$ with nearest positive $p$, *hard negatives* $n$ satisfying $d(x_a,x_n)<d(x_a,x_p)$ (violate the margin) or *semi-hard negatives* satisfying $d(x_a,x_p) < d(x_a,x_n) < d(x_a,x_p)+m$. Only these informative triplets contribute non-zero gradient.

### Why it matters
The vast majority of randomly sampled triplets satisfy the margin constraint and contribute zero loss, wasting computation. Hard-negative mining reduces the effective $O(N^3)$ cost of triplet loss to near-linear by focusing gradient updates on boundary-violating examples. It is critical in large-scale face recognition (FaceNet) and image retrieval. However, selecting *too hard* negatives (noisy labels, out-of-class lookalikes) can destabilize training.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[contrastive-loss-siamese]] — applies
- [[triplet-loss]] — applies
[To be populated during integration]