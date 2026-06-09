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
id: pkis:concept:hessian-matrix
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch05
tags: []
title: Hessian Matrix
understanding: 0
---

## Definition
The Hessian is the matrix of all second-order partial derivatives of a scalar function, measuring its local curvature.

$$\mathbf{H} = \nabla_x^2 f = \begin{bmatrix} \frac{\partial^2 f}{\partial x_1^2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial^2 f}{\partial x_n \partial x_1} & \cdots & \frac{\partial^2 f}{\partial x_n^2} \end{bmatrix} \in \mathbb{R}^{n \times n}.$$

Where the gradient is the first-order (slope) description of a function, the Hessian is the second-order (curvature) description.

### Symmetry
If $f$ is twice continuously differentiable, mixed partials commute, $\frac{\partial^2 f}{\partial x_i \partial x_j} = \frac{\partial^2 f}{\partial x_j \partial x_i}$ (Schwarz's theorem), so $\mathbf{H}$ is symmetric. For a vector field $f:\mathbb{R}^n \to \mathbb{R}^m$ the Hessian becomes an $(m \times n \times n)$ tensor.

### Curvature and optimization
The sign-definiteness of $\mathbf{H}$ classifies stationary points: positive-definite implies a local minimum, negative-definite a local maximum, indefinite a saddle. The Hessian is exactly the second-order term of a multivariate Taylor expansion, $\tfrac{1}{2}\boldsymbol{\delta}^\top \mathbf{H}\boldsymbol{\delta}$.

### Why it matters
Second-order optimization (Newton's method) preconditions the gradient by $\mathbf{H}^{-1}$ to account for curvature and converge faster near optima. The Hessian also drives the Laplace approximation, which fits a local Gaussian to a posterior at its mode using $\mathbf{H}$ of the log-density. In deep learning its full computation is usually intractable, motivating Hessian-free and quasi-Newton approximations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]