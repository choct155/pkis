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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:framework:cart-decision-trees
instantiates:
- decision-trees
- bias-variance-tradeoff
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch18
tags:
- decision-tree
- CART
- classification
- regression
- tree-model
- interpretability
title: Classification and Regression Trees (CART)
understanding: 0
uses:
- supervised-learning
- gini-impurity
- entropy
- overfitting-and-underfitting
- missing-data-mechanisms
---

## Definition
$$f(\mathbf{x}; \theta) = \sum_{j=1}^{J} w_j \mathbb{I}(\mathbf{x} \in R_j)$$

where the input space is recursively partitioned into axis-aligned rectangular regions $R_j$ via greedy binary splits, each leaf $j$ predicts a constant output $w_j$ (mean response for regression, class distribution for classification), and $\theta = \{(R_j, w_j)\}_{j=1}^J$ is learned by minimizing a node cost (MSE or Gini/entropy impurity) at each split.

A decision tree represents a piecewise-constant function whose structure is a binary tree with one region per leaf.

### Why it matters
CART is the foundational building block for bagging, random forests, and gradient boosting. Its interpretability, ability to handle mixed-type inputs, automatic variable selection, robustness to monotone input transformations, and native handling of missing data (surrogate splits) make it a widely used baseline. Its instability under small data perturbations is the key property exploited by ensemble methods.

### Fitting and regularization
The greedy top-down split criterion selects feature $j^*$ and threshold $t^*$ as
$$( j_i, t_i) = \arg\min_{j,t} \frac{|D_i^L|}{|D_i|}c(D_i^L) + \frac{|D_i^R|}{|D_i|}c(D_i^R)$$
Finding the globally optimal partition is NP-complete; regularization is achieved via early stopping or post-hoc pruning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[missing-data-mechanisms]] — uses: surrogate splits handle missing inputs at test time
- [[bias-variance-tradeoff]] — instantiates
- [[overfitting-and-underfitting]] — uses: regularization via pruning or early stopping addresses overfitting
- [[entropy]] — uses: entropy/deviance is an alternative node-splitting cost
- [[gini-impurity]] — uses
- [[supervised-learning]] — uses
- [[decision-trees]] — instantiates
[To be populated during integration]