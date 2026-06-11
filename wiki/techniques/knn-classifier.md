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
- classification
id: pkis:technique:knn-classifier
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
[To be populated during integration]