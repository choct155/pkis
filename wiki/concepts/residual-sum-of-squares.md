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
- statistics
- machine learning
id: pkis:concept:residual-sum-of-squares
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch11
tags:
- goodness of fit
- linear regression
- loss function
title: Residual Sum of Squares (RSS)
understanding: 0
---

## Definition
$$\text{RSS}(\mathbf{w}) = \sum_{n=1}^N (y_n - \mathbf{w}^T\mathbf{x}_n)^2 = \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2$$

RSS measures the total squared discrepancy between the model's predictions and the observed targets; minimising it is equivalent to maximising the Gaussian likelihood.

### Why it matters
RSS is the central training objective for linear regression and its penalised variants (ridge adds $\lambda\|\mathbf{w}\|_2^2$; lasso adds $\lambda\|\mathbf{w}\|_1$). The coefficient of determination $R^2 = 1 - \text{RSS}/\text{TSS}$ normalises RSS by the total sum of squares to give an interpretable [0,1] goodness-of-fit measure.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]