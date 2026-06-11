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
- probability-theory
- machine-learning
generalizes:
- bernoulli-distribution
id: pkis:concept:categorical-distribution
instantiates:
- exponential-family
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- multinomial-logistic-regression
related_concepts: []
sources:
- murphy-pml1-intro-ch02
tags:
- multiclass
- discrete
- classification
- softmax
title: Categorical Distribution
understanding: 0
uses:
- softmax-function
- dirichlet-distribution
---

## Definition
$$\text{Cat}(y|\boldsymbol{\theta}) \triangleq \prod_{c=1}^{C}\theta_c^{\mathbb{I}(y=c)}, \quad \theta_c \geq 0,\; \sum_{c=1}^{C}\theta_c = 1$$

The **categorical distribution** is a discrete distribution over $C$ mutually exclusive outcomes parameterized by a probability vector $\boldsymbol{\theta}\in\Delta^{C-1}$. With a one-hot encoding it can be written $\text{Cat}(y|\boldsymbol{\theta})=\prod_c \theta_c^{y_c}$. It generalizes the Bernoulli ($C=2$) and is a special case of the Multinomial with $N=1$.

### Why it matters
The categorical distribution is the output model for multiclass classification. Paired with the softmax function it yields **multinomial logistic regression** (softmax regression), the dominant baseline for $C$-class problems and the output head of virtually every neural classifier.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[exponential-family]] — instantiates
- [[multinomial-logistic-regression]] — prerequisite-of
- [[dirichlet-distribution]] — uses: Dirichlet is conjugate prior for Categorical parameter
- [[softmax-function]] — uses
- [[bernoulli-distribution]] — generalizes
[To be populated during integration]