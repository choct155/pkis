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
- probabilistic-graphical-models
- supervised-learning
id: pkis:concept:tree-augmented-naive-bayes
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch04
tags:
- naive-Bayes
- tree-structure
- generative-classifier
- conditional-independence
title: Tree-Augmented Naive Bayes (TAN)
understanding: 0
---

## Definition
A discriminative/generative classifier that extends naive Bayes by allowing a class-conditional tree structure over the features:
$$p(\mathbf{x},y) = p(y)\prod_{d=1}^D p(x_d \mid x_{\text{pa}(d)}, y)$$
where $\text{pa}(d)$ is at most one other feature node, forming a tree for each class $y$. The optimal tree can be found in $O(D^2)$ using maximum spanning tree on class-conditional mutual information.

A principled relaxation of the naive Bayes conditional independence assumption that remains computationally tractable.

### Why it matters
TAN provides a sweet spot between fully factored naive Bayes and unconstrained discriminative models: it captures the most important pairwise feature dependencies while retaining $O(D)$ inference complexity. When the tree topology varies per class, the model becomes a Bayesian multi-net (supervised mixture of trees).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]