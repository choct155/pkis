---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:framework:prototype-methods
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch13
tags:
- classification
- nonparametric
- memory-based
title: Prototype Methods
understanding: 0
---

## Definition
A family of model-free classifiers that represent the training data by a set of points (prototypes) in feature space, each carrying a class label; a query point x is classified to the class of its closest prototype, where 'closest' is usually Euclidean distance after standardizing each feature to mean 0 and variance 1. Prototypes are typically NOT examples from the training sample (the exception is 1-nearest-neighbor, where every training point is a prototype). Such methods are unstructured 'black box' engines: poor for explaining the feature-outcome relationship, but often among the best performers in practice because, with enough prototypes well-positioned, they can represent highly irregular class boundaries. The central design problem is how many prototypes to use and where to place them; methods (K-means classification, learning vector quantization, Gaussian mixtures) differ precisely in how the number and locations of prototypes are chosen. A weakness of per-class K-means placement is that the other classes have no say in positioning a given class's prototypes; LVQ and discriminant methods repair this by using all the data to position all prototypes relative to the decision boundaries.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]