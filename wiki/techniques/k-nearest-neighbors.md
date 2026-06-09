---
aliases: []
also_type: []
analogous-to:
- prototype-methods
applies:
- curse-of-dimensionality
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- linear-regression
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:technique:k-nearest-neighbors
instantiates:
- statistical-decision-theory-regression
- memory-based-function-approximation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch19
specializes:
- supervised-learning
tags: []
title: k-Nearest Neighbors
understanding: 0
uses:
- bias-variance-tradeoff
---

## Definition
A nonparametric (instance-based / memory-based) supervised learning method that makes predictions directly from the stored training examples rather than from a fixed-size parameter vector. Given a query x_q, it retrieves the set NN(k,x_q) of the k training examples nearest to x_q. For classification it returns the plurality (for binary, majority) vote of their labels -- k is usually odd to break ties. For regression it returns the mean or median of the k neighbors' outputs, or fits a local linear regression to them.

Distance is measured by a Minkowski (L_p) metric L_p(x_j,x_q)=(sum_i |x_{j,i}-x_{q,i}|^p)^{1/p}: p=2 is Euclidean, p=1 is Manhattan, and on Boolean attributes the count of differing attributes is the Hamming distance; the Mahalanobis distance accounts for covariance between dimensions. Because raw scales distort distances, dimensions are typically normalized to zero mean and unit standard deviation. The hyperparameter k controls the bias-variance balance: k=1 overfits (reacts to outliers), large k underfits; cross-validation selects k.

KNN suffers acutely from the curse of dimensionality -- in high dimensions the 'nearest' neighbors are not actually near. A naive query is O(N); the computation is accelerated with k-d trees (good up to ~10-20 dimensions given enough examples) or, for high dimensions, approximate near-neighbor search via locality-sensitive hashing. Locally weighted regression generalizes KNN by weighting examples with a kernel function of distance to remove the discontinuities of hard k-neighborhoods.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[memory-based-function-approximation]] — instantiates: k-NN stores training examples and answers queries by retrieving nearest neighbors — the canonical memory-based method.
- [[prototype-methods]] — analogous-to: 1-NN is the limiting prototype method where every training point is a prototype.
- [[curse-of-dimensionality]] — applies: kNN breaks down in high dimensions as neighborhoods stop being local
- [[linear-regression]] — contrasts-with: flexible/high-variance vs rigid/high-bias ends of the model spectrum
- [[bias-variance-tradeoff]] — uses: k controls effective parameters N/k; small k = high variance, large k = high bias
- [[statistical-decision-theory-regression]] — instantiates: kNN directly approximates f(x)=E(Y|X=x) / the Bayes classifier by sample averaging over a neighborhood
- [[supervised-learning]] — specializes
[To be populated during integration]