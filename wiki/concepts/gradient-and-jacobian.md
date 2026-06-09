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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- deep-learning
- statistical-learning
id: pkis:concept:gradient-and-jacobian
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch05
tags: []
title: Gradient and Jacobian
understanding: 0
---

## Definition
The Jacobian collects all first-order partial derivatives of a (possibly vector-valued) function into a matrix; the gradient is its special case for scalar-valued functions.

$$\mathbf{J} = \frac{d\mathbf{f}(\mathbf{x})}{d\mathbf{x}} = \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial f_m}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_n} \end{bmatrix} \in \mathbb{R}^{m \times n}, \qquad \mathbf{J}(i,j) = \frac{\partial f_i}{\partial x_j}.$$

The gradient generalizes the scalar derivative to functions of several variables by varying one input at a time and holding the rest fixed.

### Gradient as a special case
For a scalar field $f:\mathbb{R}^n \to \mathbb{R}$ the Jacobian collapses to a single row vector $\nabla_x f = \left[\frac{\partial f}{\partial x_1}\,\cdots\,\frac{\partial f}{\partial x_n}\right] \in \mathbb{R}^{1 \times n}$. For $f:\mathbb{R}^n \to \mathbb{R}^m$ the full Jacobian is $m \times n$ (numerator layout: outputs index rows, inputs index columns). The gradient points in the direction of steepest ascent.

### Why the row-vector convention
Defining the gradient as a row vector lets the multivariate chain rule reduce to ordinary matrix multiplication without transposition, and generalizes cleanly to vector-valued functions where the result becomes a matrix rather than a vector.

### Geometric reading
The Jacobian is the best local linear approximation of $\mathbf{f}$ at a point: $\mathbf{f}(\mathbf{x}) \approx \mathbf{f}(\mathbf{x}_0) + \mathbf{J}(\mathbf{x} - \mathbf{x}_0)$. The absolute value of its determinant, $|\det \mathbf{J}|$, is the local factor by which the map scales areas/volumes, which underlies change-of-variable formulas for densities.

### Why it matters
Nearly every learning algorithm optimizes an objective via gradient information; the Jacobian is also the object the chain rule chains together, making it the atomic unit of backpropagation and automatic differentiation. Gradients can be numerically verified against finite differences ($h \approx 10^{-4}$).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]