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
- machine-learning
id: pkis:concept:empirical-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch03
- murphy-pml1-intro-ch04
tags:
- nonparametric
- MLE
- empirical-risk
- training-data
title: Empirical Distribution
understanding: 0
---

## Definition
The **empirical distribution** over a dataset $\{x^{(1)},\ldots,x^{(m)}\}$ is
$$\hat{p}(x) = \frac{1}{m}\sum_{i=1}^{m}\delta(x - x^{(i)}),$$
placing equal probability mass $1/m$ on each observed sample. For discrete data it reduces to a multinoulli with empirical frequencies.

### Why it matters
The empirical distribution is the implicit training distribution in supervised learning: minimizing empirical risk is equivalent to computing expectations under $\hat{p}$. It is also the nonparametric MLE of the true data-generating distribution, directly connecting maximum likelihood estimation to sample averages.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]