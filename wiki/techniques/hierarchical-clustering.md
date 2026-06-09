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
- statistical-learning
id: pkis:technique:hierarchical-clustering
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch14
tags:
- clustering
- unsupervised-learning
title: Hierarchical Clustering
understanding: 0
---

## Definition
A family of clustering methods that produce a nested sequence of groupings rather than a single partition, requiring no pre-specified K. **Agglomerative** (bottom-up) methods start with N singletons and at each of N−1 steps merge the two least-dissimilar groups; **divisive** (top-down) methods start with one cluster and recursively split. The result is a rooted binary tree displayed as a **dendrogram**, whose node heights equal the intergroup dissimilarity at merge (under a monotonicity property), and which is cut horizontally to extract a flat clustering. Agglomerative methods differ in the intergroup dissimilarity d(G,H): **single linkage** (nearest neighbor, min d_{ii'}) tends to chain and produce large-diameter clusters; **complete linkage** (furthest neighbor, max) produces compact clusters that may violate closeness; **group average** (mean d_{ii'}) is a compromise with a statistical consistency property (it estimates ∫∫d(x,x')p_G p_H) but, unlike single/complete linkage, is not invariant to monotone transformations of the dissimilarities. The fidelity of the imposed hierarchy is assessed by the **cophenetic correlation** between input dissimilarities and the cophenetic dissimilarities (which obey the ultrametric inequality C_{ii'} ≤ max{C_{ik},C_{i'k}}).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]