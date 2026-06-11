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
- machine-learning
- information-theory
- signal-processing
id: pkis:concept:vector-quantization-clustering
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch21
tags:
- lossy-compression
- codebook
- k-means
- rate-distortion
title: Vector Quantization
understanding: 0
---

## Definition
Vector quantization (VQ) performs lossy compression of real-valued vectors $x_n \in \mathbb{R}^D$ by learning a **codebook** of $K$ prototypes $\{\mu_k\}$ and encoding each vector as the index of its nearest prototype:
$$\text{encode}(x_n) = \arg\min_k \|x_n - \mu_k\|^2, \qquad \text{decode}(k) = \mu_k$$
The **distortion** (reconstruction error) is:
$$J = \frac{1}{N}\sum_{n=1}^N \|x_n - \mu_{z_n}\|^2$$
Storage cost is $O(N\log_2 K + KDB)$ bits versus $O(NDB)$ for raw storage, achieving a compression ratio of $DB / \log_2 K$.

### Why it matters
VQ reveals the deep connection between clustering (K-means) and data compression/density estimation: the optimal codebook is precisely the set of K-means centroids. It is used in image compression, speech coding, and as a building block in modern learned compression systems.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]