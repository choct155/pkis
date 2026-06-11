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
- machine-learning
id: pkis:concept:support-vectors
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch07
tags:
- sparsity
- svm
- kernel-methods
- KKT
title: Support Vectors
understanding: 0
---

## Definition
Support vectors are the training data points $\mathbf{x}_n$ for which the dual Lagrange multiplier $a_n > 0$ in the SVM optimisation. By the KKT complementarity condition $a_n\{t_n y(\mathbf{x}_n)-1\}=0$, these are exactly the points that lie on or within the margin boundaries ($t_n y(\mathbf{x}_n) = 1 - \xi_n$). All other points have $a_n = 0$ and play no role in the prediction
$$y(\mathbf{x}) = \sum_{n \in \mathcal{S}} a_n t_n k(\mathbf{x},\mathbf{x}_n) + b.$$

The decision boundary is entirely determined by this sparse subset of training examples.

### Why it matters
Sparsity in support vectors is the central computational advantage of SVMs: after training, only the support vectors need to be stored, and prediction cost is proportional to their number rather than $N$. The margin and decision boundary are geometrically defined by the support vectors alone, giving an intuitive measure of which training examples are informative.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]