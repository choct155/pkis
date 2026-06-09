---
aliases: []
also_type: []
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
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:technique:discriminant-adaptive-nearest-neighbor
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch13
specializes:
- k-nearest-neighbors
tags:
- nearest-neighbors
- adaptive-metric
- local-dimension-reduction
- classification
title: Discriminant Adaptive Nearest-Neighbors (DANN)
understanding: 0
---

## Definition
A nearest-neighbor method (Hastie & Tibshirani, 1996a) that adapts the distance metric locally at each query point to combat the curse of dimensionality. In high dimensions a fixed neighborhood implicitly assumes class probabilities are roughly constant within it, but they often vary along only a few directions; the neighborhood should be stretched in directions where class probability changes little. At each query point x_0, a preliminary neighborhood (e.g. 50 points) supplies local within-class (W) and between-class (B) covariance matrices, defining the metric D(x,x_0) = (x-x_0)^T Sigma (x-x_0) with Sigma = W^{-1/2}[B* + eps I]W^{-1/2}, where B* = W^{-1/2} B W^{-1/2}. Operationally it spheres the data by W, then stretches the neighborhood in the zero-eigenvalue directions of B* (where local class means do not differ); eps (default 1) rounds the neighborhood from an infinite strip to an ellipsoid. A potentially different metric is used at every query point — local dimension reduction. Where only one class is present B=0 and Sigma=I (circular neighborhood). A global variant averages the local between-class matrices, B-bar = (1/N) sum_i B_i, and uses the leading eigenvectors of B-bar (best rank-L approximation by least squares) to define a global subspace for nearest-neighbor classification, related to sliced inverse regression (Duan & Li, 1991). DANN significantly reduces error versus standard k-NN and LVQ on problems where the discriminant direction varies across feature space.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[curse-of-dimensionality]] — applies: DANN adapts the metric specifically to mitigate high-dimensional neighborhood degradation.
- [[k-nearest-neighbors]] — specializes: DANN is k-NN with a locally adapted discriminant metric.
[To be populated during integration]