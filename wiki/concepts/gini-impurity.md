---
aliases: []
also_type: []
analogous-to:
- entropy
applies:
- cart
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- cross-entropy-loss
- entropy
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:concept:gini-impurity
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- cart-decision-trees
related_concepts: []
sources:
- bishop-prml-ch14
- murphy-pml1-intro-ch18
tags:
- impurity
- decision-tree
- classification
- splitting-criterion
title: Gini Impurity Index
understanding: 0
---

## Definition
For a leaf node containing data from $K$ classes with empirical proportions $\{p_{\tau k}\}$:
$$Q_\tau = \sum_{k=1}^{K} p_{\tau k}(1 - p_{\tau k}) = 1 - \sum_k p_{\tau k}^2$$

The Gini index measures the expected misclassification probability of a randomly drawn sample if its label were assigned according to the class distribution in the node.

### Why it matters
Used in CART as a node-splitting criterion, the Gini index is differentiable and more sensitive to class-probability changes than the raw misclassification rate, making it better for growing trees. It equals zero for a pure node and reaches its maximum $1-1/K$ for a uniform class distribution. Together with cross-entropy, it is preferred over misclassification rate for growing steps, while misclassification rate is used for final pruning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[entropy]] — contrasts-with: both measure node impurity; Gini is cheaper, entropy has information-theoretic grounding
- [[cart-decision-trees]] — prerequisite-of
- [[cross-entropy-loss]] — contrasts-with
- [[entropy]] — analogous-to
- [[cart]] — applies
[To be populated during integration]