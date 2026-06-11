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
id: pkis:technique:k-medoids
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch21
tags:
- clustering
- medoid
- pam
- robustness
- pairwise-distance
title: K-medoids / PAM Algorithm
understanding: 0
---

## Definition
K-medoids generalizes K-means by representing each cluster center with an actual data point (the **medoid**) rather than a coordinate mean. Given an $N\times N$ pairwise distance matrix $D(n,n')$, the medoid of cluster $k$ is:
$$m_k = \arg\min_{n: z_n=k} \sum_{n': z_{n'}=k} D(n, n')$$
The classic **PAM** (Partitioning Around Medoids) algorithm evaluates all swap pairs $(m, o)$ at each iteration. The Voronoi-iteration variant alternates: (1) re-assign each point to its nearest medoid; (2) update each medoid as above; cost $O(N^2 K T)$.

### Why it matters
By working with pairwise distances rather than feature averages, K-medoids applies to non-Euclidean data (strings, graphs, sequences) where means are undefined. It is also more robust to outliers than K-means.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]