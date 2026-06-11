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
id: pkis:concept:hyperparameters-validation-set
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch05
tags:
- hyperparameter
- validation
- model-selection
- train-test-split
- cross-validation
title: Hyperparameters and Validation Set
understanding: 0
---

## Definition
**Hyperparameters** are settings of a learning algorithm that control its behavior but are not themselves adapted by the algorithm on the training set (e.g., polynomial degree $d$, weight-decay coefficient $\lambda$). A **validation set** is a held-out subset of the original training pool used to estimate generalization error during hyperparameter search:

$$\mathcal{D}_{\text{train}} \xrightarrow{\text{split}} \mathcal{D}_{\text{learn}}\;(\approx 80\%) \cup \mathcal{D}_{\text{valid}}\;(\approx 20\%)$$

The test set is never used to choose hyperparameters; it estimates final generalization error only.

### Why it matters
Learning capacity-controlling hyperparameters on the training set leads to degenerate solutions (maximum capacity, zero regularization). The train/valid/test split is therefore a fundamental protocol in empirical ML, and k-fold cross-validation is its extension for small datasets.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]