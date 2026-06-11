---
aliases: []
also_type: []
analogous-to:
- information-criteria
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
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:concept:tree-pruning
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch14
specializes:
- regularization
tags:
- decision-tree
- regularisation
- bias-variance
- cross-validation
- model-complexity
title: Tree Pruning (Cost-Complexity Pruning)
understanding: 0
uses:
- bias-variance-tradeoff
- cross-validation
---

## Definition
A post-hoc regularisation procedure for decision trees that selects a subtree $T\subset T_0$ of a fully grown tree $T_0$ by minimising the penalised cost
$$C(T) = \sum_{\tau=1}^{|T|} Q_\tau(T) + \lambda\,|T|$$
where $Q_\tau(T)$ is the node impurity (sum-of-squares or cross-entropy), $|T|$ is the number of leaf nodes, and the regularisation parameter $\lambda$ is chosen by cross-validation.

### Why it matters
Greedy tree growing often builds over-complex trees that overfit training data. Pruning navigates the bias–variance tradeoff by penalising tree size; the $\lambda$ parameter plays the role of a regulariser analogous to ridge or lasso penalties in linear models. The pruning criterion is equivalent to the MDL / AIC/BIC-style information criteria applied to partition models. Using misclassification rate (rather than cross-entropy or Gini) for the pruning stage is standard practice because it directly targets the deployment objective.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[information-criteria]] — analogous-to
- [[cross-validation]] — uses
- [[bias-variance-tradeoff]] — uses
- [[regularization]] — specializes
- [[cart]] — applies
[To be populated during integration]