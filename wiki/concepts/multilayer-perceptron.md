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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- deep-learning
id: pkis:concept:multilayer-perceptron
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch44
tags:
- neural-networks
- function-approximation
- statistical-learning
- regression
- classification
title: Multilayer Perceptron (Feedforward Network)
understanding: 0
---

## Definition
A **multilayer perceptron (MLP)** is a feedforward network defining a nonlinear parameterized mapping $y = y(\mathbf{x}; \mathbf{w}, A)$ from input $\mathbf{x}$ to output $y$, where $\mathbf{w}$ collects the weights and biases and $A$ denotes the architecture. With one hidden layer it computes

$$a_j^{(1)} = \sum_l w_{jl}^{(1)} x_l + \theta_j^{(1)},\quad h_j = f^{(1)}\!\big(a_j^{(1)}\big),$$

$$a_i^{(2)} = \sum_j w_{ij}^{(2)} h_j + \theta_i^{(2)},\quad y_i = f^{(2)}\!\big(a_i^{(2)}\big),$$

where typically $f^{(1)}=\tanh$ and the output nonlinearity $f^{(2)}$ is chosen by task: identity for regression, logistic $1/(1+e^{-a})$ for binary classification, and softmax $y_i = e^{a_i}/\sum_{i'} e^{a_{i'}}$ for multi-class. MacKay's convention counts *layers of neurons* (excluding inputs), so this is a 'two-layer' network.

### Why the hidden nonlinearity matters
The sigmoid $f^{(1)}$ at the hidden layer is what lifts the model beyond linear regression (whose surface is a flat plane); composing affine maps with a nonlinearity yields functions of arbitrary complexity (figure 44.4).

### Function space and complexity control
Drawing $\mathbf{w}$ at random and plotting $y(x)$ reveals the prior over functions the architecture implies: vertical scale $\sim \sqrt{H}\,\sigma_{\text{out}}$, horizontal range $\sim \sigma_{\text{bias}}/\sigma_{\text{in}}$, shortest length-scale $\sim 1/\sigma_{\text{in}}$. Neal (1996) showed that as the number of hidden units $H\to\infty$ the statistics of these functions become *independent of $H$*; complexity is governed by the characteristic magnitude of the weights, not the parameter count — motivating weight decay as the real complexity control.

### Why it matters
The MLP is the canonical trainable nonlinear curve-fitter underpinning modern deep learning. Its layered, differentiable form is exactly what makes gradient-based training via backpropagation possible, and its infinite-width limit connects it to Gaussian processes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]