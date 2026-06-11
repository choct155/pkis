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
- deep-learning
id: pkis:concept:logistic-sigmoid
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch03
tags:
- activation
- sigmoid
- Bernoulli
- saturation
title: Logistic Sigmoid Function
understanding: 0
---

## Definition
The **logistic sigmoid** is the function
$$\sigma(x) = \frac{1}{1+\exp(-x)} = \frac{\exp(x)}{\exp(x)+1}.$$
It maps $\mathbb{R}$ to $(0,1)$, making it natural for parameterizing Bernoulli probabilities and binary classifiers. Key identities: $\sigma'(x)=\sigma(x)(1-\sigma(x))$, $1-\sigma(x)=\sigma(-x)$, and it *saturates* (gradient $\approx 0$) for large $|x|$.

### Why it matters
The sigmoid is ubiquitous in neural networks as a binary output activation and as a building block for gating mechanisms (e.g., LSTMs). Its saturation property is the root cause of the vanishing-gradient problem in deep networks.

### Relationship to softplus
The softplus function $\zeta(x)=\log(1+\exp(x))$ is the antiderivative of $\sigma$: $\frac{d}{dx}\zeta(x)=\sigma(x)$, and $\zeta(x)-\zeta(-x)=x$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]