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
id: pkis:technique:k-nearest-neighbors
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch19
tags: []
title: k-Nearest Neighbors
understanding: 0
---

## Definition
A nonparametric (instance-based / memory-based) supervised learning method that makes predictions directly from the stored training examples rather than from a fixed-size parameter vector. Given a query x_q, it retrieves the set NN(k,x_q) of the k training examples nearest to x_q. For classification it returns the plurality (for binary, majority) vote of their labels -- k is usually odd to break ties. For regression it returns the mean or median of the k neighbors' outputs, or fits a local linear regression to them.

Distance is measured by a Minkowski (L_p) metric L_p(x_j,x_q)=(sum_i |x_{j,i}-x_{q,i}|^p)^{1/p}: p=2 is Euclidean, p=1 is Manhattan, and on Boolean attributes the count of differing attributes is the Hamming distance; the Mahalanobis distance accounts for covariance between dimensions. Because raw scales distort distances, dimensions are typically normalized to zero mean and unit standard deviation. The hyperparameter k controls the bias-variance balance: k=1 overfits (reacts to outliers), large k underfits; cross-validation selects k.

KNN suffers acutely from the curse of dimensionality -- in high dimensions the 'nearest' neighbors are not actually near. A naive query is O(N); the computation is accelerated with k-d trees (good up to ~10-20 dimensions given enough examples) or, for high dimensions, approximate near-neighbor search via locality-sensitive hashing. Locally weighted regression generalizes KNN by weighting examples with a kernel function of distance to remove the discontinuities of hard k-neighborhoods.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]