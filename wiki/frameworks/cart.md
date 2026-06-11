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
id: pkis:framework:cart
instantiates:
- decision-trees
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- random-forests
- gradient-boosting
related_concepts: []
sources:
- bishop-prml-ch14
tags:
- decision-tree
- greedy-splitting
- pruning
- interpretability
- nonparametric
title: CART (Classification and Regression Trees)
understanding: 0
uses:
- gini-impurity
- tree-pruning
- regularization
- cross-validation
---

## Definition
CART (Breiman et al., 1984) learns a binary decision tree by recursively partitioning input space into axis-aligned cuboid regions and fitting a simple (e.g. constant) model in each leaf.

**Growing:** At each node, choose the split variable $j$ and threshold $\theta$ minimising residual sum-of-squares (regression) or impurity (classification). The greedy search is tractable because, for fixed $j$ and $\theta$, optimal leaf predictions are local averages or plurality classes.

**Impurity measures for classification:**
$$\text{Cross-entropy: } Q_\tau=-\sum_k p_{\tau k}\ln p_{\tau k}$$
$$\text{Gini index: } Q_\tau=\sum_k p_{\tau k}(1-p_{\tau k})$$

**Pruning:** Grow a large tree $T_0$, then prune by minimising the penalised cost $C(T)=\sum_\tau Q_\tau(T)+\lambda|T|$ where $|T|$ is the number of leaves and $\lambda$ is chosen by cross-validation.

### Why it matters
CART produces human-interpretable models via sequences of binary decisions, handles mixed input types, and requires no feature scaling. Its instability (small data changes can flip the entire tree) and axis-aligned splits motivate ensembles such as random forests and gradient boosting.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gradient-boosting]] — prerequisite-of
- [[random-forests]] — prerequisite-of
- [[cross-validation]] — uses
- [[regularization]] — uses
- [[tree-pruning]] — uses
- [[gini-impurity]] — uses
- [[decision-trees]] — instantiates
[To be populated during integration]