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
extends:
- k-means-clustering
id: pkis:technique:k-means-plus-plus
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch21
tags:
- initialization
- k-means
- approximation-guarantee
- clustering
title: K-means++ Initialization
understanding: 0
---

## Definition
K-means++ is a seeding strategy for K-means that selects initial centroids sequentially to spread them across the data. The first centroid is chosen uniformly at random; each subsequent centroid $\mu_t$ is drawn from the remaining points with probability proportional to the squared distance to the nearest existing centroid:
$$p(\mu_t = x_n) = \frac{D_{t-1}(x_n)}{\sum_{n'} D_{t-1}(x_{n'})}, \quad D_{t-1}(x) = \min_{k<t}\|x - \mu_k\|_2^2$$
Also called **farthest-point clustering**, this provides a provable $O(\log K)$ approximation guarantee on the reconstruction error relative to the global optimum [Arthur & Vassilvitskii, 2007].

### Why it matters
Poor initialization is a key failure mode of K-means; K-means++ dramatically reduces the risk of converging to a bad local minimum at essentially no extra asymptotic cost, and is the default initialization in scikit-learn.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[k-means-clustering]] — extends
[To be populated during integration]