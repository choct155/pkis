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
- probability-theory
- statistics
id: pkis:concept:sigmoid-logistic-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch02
tags:
- sigmoid
- logistic
- binary-classification
- link-function
title: Sigmoid (Logistic) Function
understanding: 0
---

## Definition
$$\sigma(a) \triangleq \frac{1}{1+e^{-a}} = \frac{e^a}{1+e^a}, \quad a\in\mathbb{R},\quad \sigma(a)\in(0,1)$$

The **sigmoid** (or logistic) function is a smooth, monotonically increasing S-shaped map from the real line to $(0,1)$. Its inverse is the **logit** (log-odds) function: $\text{logit}(p)=\log(p/(1-p))$. It is a soft version of the Heaviside step function and the $C=2$ special case of the softmax.

### Why it matters
The sigmoid is the canonical link function for binary probabilistic models: $p(y=1|x;\theta)=\sigma(w^\top x+b)$ defines logistic regression. It also appears as a gate in LSTMs, as an activation in early neural networks, and underlies the logit/probit models in statistics. Key properties: $\sigma(-a)=1-\sigma(a)$, $\sigma'(a)=\sigma(a)(1-\sigma(a))$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]