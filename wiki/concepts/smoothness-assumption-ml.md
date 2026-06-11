---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistical-learning-theory
- machine-learning
id: pkis:concept:smoothness-assumption-ml
instantiates:
- inductive-priors-representation-learning
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- curse-of-dimensionality
related_concepts: []
sources:
- goodfellow-deeplearning-ch15
specializes:
- inductive-bias
tags:
- smoothness
- regularization
- generalization
- curse-of-dimensionality
- inductive-bias
title: Smoothness Assumption in Machine Learning
understanding: 0
uses:
- kernel-regression-rl
- k-nearest-neighbors
---

## Definition
The prior belief that the target function $f$ varies slowly relative to the input space: for unit direction $\mathbf{d}$ and small $\epsilon$,
$$f(\mathbf{x} + \epsilon\mathbf{d}) \approx f(\mathbf{x}).$$
It allows a learner to generalise from a training example $(\mathbf{x}, y)$ to nearby inputs $\mathbf{x} + \epsilon\mathbf{d}$ without additional observations.

### Why it matters
The smoothness assumption underlies kernel methods, nearest-neighbour algorithms, and many classical regularisers. However, it is *insufficient* alone to overcome the curse of dimensionality: for a function that varies in many directions across exponentially many regions, a number of training examples proportional to the number of regions is required. Deep distributed representations supplement smoothness with structural priors (depth, causality, sparsity) that allow far more efficient generalisation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[k-nearest-neighbors]] — uses
- [[kernel-regression-rl]] — uses
- [[inductive-bias]] — specializes
- [[curse-of-dimensionality]] — prerequisite-of
- [[inductive-priors-representation-learning]] — instantiates
[To be populated during integration]