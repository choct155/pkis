---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- neural-networks
id: pkis:technique:perceptron-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch04
tags:
- online-learning
- convergence-theorem
- linear-separator
- step-function
- perceptron-criterion
- historical
title: Perceptron Learning Algorithm
understanding: 0
---

## Definition
The perceptron (Rosenblatt, 1962) classifies inputs via $y(\mathbf{x}) = f(\mathbf{w}^T\boldsymbol{\phi}(\mathbf{x}))$ with step activation $f(a)=\text{sgn}(a)$. Parameters are updated by stochastic gradient descent on the perceptron criterion

$$E_P(\mathbf{w}) = -\sum_{n\in\mathcal{M}}\mathbf{w}^T\boldsymbol{\phi}_n t_n, \qquad \mathbf{w}^{(\tau+1)} = \mathbf{w}^{(\tau)} + \eta\,\boldsymbol{\phi}_n t_n$$

where $\mathcal{M}$ is the set of currently misclassified patterns and $t_n\in\{-1,+1\}$. The **perceptron convergence theorem** guarantees that if a linear separator exists the algorithm finds one in a finite number of steps; on non-separable data it never converges.

### Why it matters
The perceptron is the historical origin of neural network learning and the credit-assignment-by-error principle. Its convergence theorem is one of the first PAC-style guarantees for a learning algorithm. Its key limitation—failure on non-linearly separable data (Minsky & Papert, 1969)—directly motivated multilayer networks and kernel methods.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]