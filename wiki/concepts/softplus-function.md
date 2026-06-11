---
aliases: []
also_type: []
applies:
- gaussian-distribution
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
- deep-learning
id: pkis:concept:softplus-function
instantiates:
- activation-functions
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch03
tags:
- activation
- positive-part
- smooth-approximation
title: Softplus Function
understanding: 0
uses:
- logistic-sigmoid
---

## Definition
The **softplus function** is
$$\zeta(x) = \log(1 + \exp(x)).$$
It is a smooth approximation to the positive-part (ReLU) function $x^+ = \max(0, x)$, with range $(0, \infty)$, making it suitable for producing positive parameters such as standard deviations or precision values.

### Why it matters
Softplus appears in probabilistic deep learning wherever a strictly positive quantity must be predicted (e.g., scale parameters of a normal distribution). Its derivative is $\sigma(x)$, linking it tightly to the sigmoid, and the identity $\zeta(x)-\zeta(-x)=x$ mirrors the decomposition $x^+-x^-=x$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gaussian-distribution]] — applies: used to produce positive scale/precision parameters
- [[activation-functions]] — instantiates
- [[logistic-sigmoid]] — uses
[To be populated during integration]