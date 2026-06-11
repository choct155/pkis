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
- machine-learning
- statistics
- unsupervised-learning
id: pkis:technique:hierarchical-agglomerative-clustering
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch21
tags:
- clustering
- dendrogram
- linkage
- agglomerative
- hierarchical
title: Hierarchical Agglomerative Clustering (HAC)
understanding: 0
---

## Definition
Given an $N \times N$ dissimilarity matrix $D_{ij} \geq 0$, HAC starts with $N$ singleton clusters and at each step merges the two most similar clusters until a single cluster remains, producing a binary tree (dendrogram). The inter-cluster dissimilarity is defined by a linkage criterion:
$$d_{SL}(G,H) = \min_{i\in G, i'\in H} d_{i,i'}, \quad d_{CL}(G,H) = \max_{i\in G, i'\in H} d_{i,i'}, \quad d_{avg}(G,H) = \frac{1}{n_G n_H}\sum_{i\in G}\sum_{i'\in H} d_{i,i'}$$
for single, complete, and average linkage respectively. The dendrogram encodes a full hierarchy of nested partitions that can be cut at any height to yield any desired number of clusters.

### Why it matters
HAC requires no pre-specified number of clusters, produces interpretable dendrograms, and works from raw pairwise dissimilarities rather than feature vectors — making it broadly applicable across data types. Single-link HAC is equivalent to computing a minimum spanning tree and runs in $O(N^2)$; average- and complete-link run in $O(N^3)$ (reducible to $O(N^2 \log N)$ via a priority queue).

### Linkage variants
**Single link** (nearest-neighbor) produces elongated, chained clusters and is invariant to monotone transformations of $d$. **Complete link** (furthest-neighbor) produces compact, small-diameter clusters and is also invariant to monotone transforms. **Average link** is a compromise that tends to produce both compact and well-separated clusters but is sensitive to measurement scale.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]