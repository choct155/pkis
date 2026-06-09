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
extends:
- regularization
id: pkis:concept:multilayer-perceptron
instantiates:
- universal-approximation-theorem
- learning-as-inference
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch44
specializes:
- neural-networks
- projection-pursuit-regression
tags:
- neural-networks
- function-approximation
- statistical-learning
- regression
- classification
title: Multilayer Perceptron (Feedforward Network)
understanding: 0
uses:
- gradient-descent
- weight-decay-as-prior
- cross-entropy-loss
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
- [[projection-pursuit-regression]] — specializes: The MLP is a restricted PPR with the parametric ridge form g_m = beta_m sigma(alpha_0m + ||alpha_m|| omega_m^T X).
- [[learning-as-inference]] — instantiates: Minimizing the MLP objective M(w) is MAP inference: error is a negative log likelihood and weight decay a negative log prior.
- [[regularization]] — extends: Training adds a regularizing weight-decay term to the data error to combat overfitting.
- [[cross-entropy-loss]] — uses: Classification MLPs (logistic / softmax outputs) are trained with the cross-entropy negative log likelihood.
- [[weight-decay-as-prior]] — uses: Quadratic weight decay (Gaussian prior on weights) controls the effective complexity of the fitted MLP.
- [[universal-approximation-theorem]] — instantiates: A one-hidden-layer MLP with enough units realizes the universal approximation property, producing functions far richer than linear regression.
- [[gradient-descent]] — uses: MLP parameters are fit by gradient descent on the (regularized) error function.
- [[neural-networks]] — specializes: The MLP is the canonical feedforward neural network instantiated with one or more hidden layers.
[To be populated during integration]