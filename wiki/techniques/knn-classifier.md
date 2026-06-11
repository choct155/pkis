---
aliases: []
also_type: []
applies:
- open-set-recognition
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
- classification
id: pkis:technique:knn-classifier
instantiates:
- k-nearest-neighbors
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch16
tags:
- nonparametric
- instance-based
- exemplar-based
- nearest-neighbor
title: K-Nearest Neighbor (KNN) Classifier
understanding: 0
uses:
- curse-of-dimensionality
- mahalanobis-distance
- cover-hart-theorem
- locality-sensitive-hashing
---

## Definition
$$p(y = c \mid x, D) = \frac{1}{K} \sum_{n \in N_K(x,D)} \mathbb{I}(y_n = c)$$

where $N_K(x, D)$ denotes the $K$ training points closest to $x$ under a chosen distance metric. Classification is performed by majority vote (or soft probability) over the $K$ nearest neighbors in the stored training set.

### Why it matters
KNN is the canonical exemplar-based classifier: it requires no explicit model fitting, gracefully handles multi-class problems, and—as $N\to\infty$—achieves error within a factor of 2 of the Bayes-optimal error (Cover–Hart theorem). It also naturally extends to open-set and few-shot settings by updating the gallery without retraining.

### Limitations
Performance degrades in high dimensions (curse of dimensionality): the expected edge-length of the hypercube needed to capture a fraction $p$ of data in $D$ dimensions is $p^{1/D}$, which approaches 1 rapidly. Memory cost is $O(N)$ and naive query cost is $O(ND)$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[open-set-recognition]] — applies: KNN classifiers are naturally suited to open-set and incremental learning via gallery comparison
- [[locality-sensitive-hashing]] — uses: LSH is the primary hashing-based speedup for approximate NN search
- [[cover-hart-theorem]] — uses: Cover-Hart theorem provides the 2x Bayes error bound for KNN
- [[k-nearest-neighbors]] — instantiates: knn-classifier is the classification instantiation of the general k-nearest-neighbors technique
- [[mahalanobis-distance]] — uses: Mahalanobis distance is the standard configurable metric for KNN
- [[curse-of-dimensionality]] — uses: curse of dimensionality is the primary failure mode of KNN in high dimensions
[To be populated during integration]