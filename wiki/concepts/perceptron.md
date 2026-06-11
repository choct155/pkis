---
aliases: []
also_type: []
analogous-to:
- linear-regression
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
id: pkis:concept:perceptron
instantiates:
- single-neuron-classifier
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- stochastic-gradient-descent
- connectionism
related_concepts: []
sources:
- goodfellow-deeplearning-ch01
tags:
- linear-classifier
- online-learning
- convergence
- history
title: Perceptron
understanding: 0
uses:
- linear-separability
---

## Definition
The perceptron (Rosenblatt, 1958) is a **single-layer linear classifier** that learns a weight vector $\mathbf{w}$ and bias $b$ such that the decision rule $\hat{y} = \text{sign}(\mathbf{w}^\top \mathbf{x} + b)$ correctly classifies training examples presented one at a time.

The **perceptron learning rule** updates weights on misclassified examples: $\mathbf{w} \leftarrow \mathbf{w} + y_i \mathbf{x}_i$.

### Why it matters
The perceptron was the **first algorithm proven to converge** to a correct classifier for linearly separable data (Perceptron Convergence Theorem), making it the foundational result of computational learning theory. Its limitations — inability to solve XOR and other non-linearly separable problems — directly motivated the development of multi-layer networks and the second wave of neural network research.

### Connection to ADALINE
The contemporaneous ADALINE (Widrow & Hoff, 1960) used the same linear model but minimized mean squared error via what is now recognized as stochastic gradient descent, predating the modern SGD formulation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[linear-separability]] — uses: The perceptron convergence theorem applies only to linearly separable data.
- [[connectionism]] — prerequisite-of
- [[stochastic-gradient-descent]] — prerequisite-of: The ADALINE weight update rule is a special case of SGD.
- [[linear-regression]] — analogous-to: ADALINE uses the same linear model as the perceptron but with regression output and MSE loss, precursor to SGD.
- [[single-neuron-classifier]] — instantiates
[To be populated during integration]