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
- statistical-learning-theory
id: pkis:concept:model-capacity-hypothesis-space
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch05
tags:
- capacity
- hypothesis-space
- representational-capacity
- overfitting
- underfitting
title: Model Capacity and Hypothesis Space
understanding: 0
---

## Definition
The **capacity** of a learning algorithm is its ability to fit a wide variety of functions; it is controlled by the **hypothesis space** — the set of functions the algorithm is permitted to select. Representational capacity is the size of the family of functions the model can express; **effective capacity** may be smaller due to optimization imperfections.

$$\text{Effective capacity} \leq \text{Representational capacity}$$

For polynomial regression of degree $d$, the hypothesis space is $\{\hat{y}=b+\sum_{i=1}^d w_i x^i\}$, so degree is a capacity hyperparameter.

### Why it matters
Capacity directly mediates the bias–variance tradeoff: too-low capacity causes underfitting (high bias), too-high causes overfitting (high variance). Choosing capacity to match task complexity and training-set size is the core engineering decision in machine learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]