---
aliases: []
also_type: []
applies:
- random-forests
- gradient-boosting
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- interpretability
id: pkis:technique:feature-importance-tree-ensembles
instantiates:
- variable-importance-for-tree-ensembles
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch18
tags:
- feature-selection
- interpretability
- decision-tree
- random-forest
- gradient-boosting
title: Feature Importance for Tree Ensembles
understanding: 0
uses:
- cart-decision-trees
---

## Definition
For a single tree $T$, the importance of feature $k$ is the total impurity reduction attributed to splits on that feature:

$$R_k(T) = \sum_{j=1}^{J-1} G_j \, \mathbb{I}(v_j = k)$$

where $G_j$ is the gain (reduction in node cost) at internal node $j$ and $v_j$ is the feature used at node $j$. For an ensemble of $M$ trees the scores are averaged:

$$R_k = \frac{1}{M} \sum_{m=1}^M R_k(T_m)$$

Scores are typically normalised so the most important feature scores 100.

Feature importance aggregates how much each input variable reduces prediction error, summed across all splits in all trees.

### Why it matters
This measure provides a global, model-intrinsic summary of variable relevance that requires no additional computation beyond training. It is widely used for feature selection and model interpretation in random forests and gradient boosting. A known limitation is that it can favour high-cardinality features; alternatives include permutation importance and SHAP values.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[cart-decision-trees]] — uses
- [[gradient-boosting]] — applies
- [[random-forests]] — applies
- [[variable-importance-for-tree-ensembles]] — instantiates
[To be populated during integration]