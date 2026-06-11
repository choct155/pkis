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
- statistics
id: pkis:concept:generalization-error-training-error
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch05
tags:
- generalization
- overfitting
- underfitting
- capacity
- iid-assumption
title: Generalization Error and Training Error
understanding: 0
---

## Definition
$$\text{Gen. Error} = \mathbb{E}_{(\mathbf{x},y)\sim p_{\text{data}}}[L(f(\mathbf{x}),y)], \quad \text{Train Error} = \frac{1}{m}\sum_{i=1}^m L(f(\mathbf{x}^{(i)}),y^{(i)})$$

Generalization error (test error) is the expected loss on new examples drawn from $p_{\text{data}}$; training error is the empirical mean loss on the fixed training set. Because parameters are chosen to reduce training error, the expected training error is always $\leq$ expected generalization error.

### Why it matters
The gap between the two quantities is the primary diagnostic for underfitting vs. overfitting. Statistical learning theory bounds this gap as a function of model capacity and training-set size, providing the intellectual foundation for regularization and capacity control in all of machine learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]