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
- statistics
- machine-learning
id: pkis:concept:categorical-and-multinomial-distributions
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch02
tags:
- categorical
- multinomial
- discrete-distribution
- classification
- one-hot
title: Categorical and Multinomial Distributions
understanding: 0
---

## Definition
The **categorical distribution** over $K$ classes is
$$\mathrm{Cat}(x \mid \boldsymbol{\theta}) = \prod_{k=1}^{K} \theta_k^{\mathbb{I}(x=k)}, \qquad \sum_k \theta_k = 1, \; \theta_k \geq 0.$$
It is the multi-class generalization of the Bernoulli. The **multinomial distribution** counts the occurrences of each class in $N$ i.i.d. categorical draws:
$$\mathcal{M}(\mathbf{x} \mid N, \boldsymbol{\theta}) = \binom{N}{x_1 \cdots x_K} \prod_{k=1}^{K} \theta_k^{x_k}, \qquad \sum_k x_k = N.$$
The categorical is the $N=1$ special case of the multinomial.

### Why it matters
Categorical/multinomial distributions are the building blocks of discrete generative models (language models, topic models, naive Bayes classifiers) and arise naturally as the likelihood in any classification or count-data setting with $K > 2$ classes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]