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
id: pkis:concept:population-risk
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch01
tags:
- generalization
- expected-loss
- statistical-learning-theory
- risk
title: Population Risk
understanding: 0
---

## Definition
The true expected loss of a predictor $f(\cdot;\theta)$ under the data-generating distribution $p^*(x,y)$:
$$\mathcal{L}(\theta; p^*) \triangleq \mathbb{E}_{p^*(x,y)}[\ell(y, f(x;\theta))]$$
It is the theoretical quantity that supervised learning ultimately aims to minimize, in contrast to the empirical risk computed on a finite training set.

### Why it matters
Population risk is the formal target of generalization. Empirical risk minimization is justified by the law of large numbers and concentration inequalities that bound the gap between population and empirical risk. Defining it precisely anchors the definitions of underfitting, overfitting, and optimal model complexity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]