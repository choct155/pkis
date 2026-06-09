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
- bayesian-stats
- statistical-learning
id: pkis:concept:taylor-series
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch05
tags: []
title: Taylor Series
understanding: 0
---

## Definition
The Taylor series represents a smooth function as an infinite sum of polynomial terms built from its derivatives at an expansion point $x_0$.

$$T_\infty(x) = \sum_{k=0}^{\infty} \frac{f^{(k)}(x_0)}{k!}(x - x_0)^k.$$

It is the systematic way to approximate any smooth function locally by a polynomial whose accuracy improves with degree.

### Taylor polynomial and analyticity
Truncating at degree $n$ gives the Taylor polynomial $T_n$, an order-$n$ approximation that is exact in a neighborhood of $x_0$ when $f$ is itself a polynomial of degree $\le n$. If $f = T_\infty$ everywhere, $f$ is called analytic. The expansion at $x_0 = 0$ is the Maclaurin series.

### Multivariate form
For $f:\mathbb{R}^D \to \mathbb{R}$ with $\boldsymbol{\delta} = \mathbf{x} - \mathbf{x}_0$, the series uses $k$-th order derivative tensors: $f(\mathbf{x}) = \sum_{k=0}^\infty \frac{D_x^k f(\mathbf{x}_0)}{k!}\boldsymbol{\delta}^k$. The first three terms are the value $f(\mathbf{x}_0)$, the linear term $\nabla_x f(\mathbf{x}_0)\,\boldsymbol{\delta}$, and the quadratic term $\tfrac{1}{2}\boldsymbol{\delta}^\top \mathbf{H}(\mathbf{x}_0)\,\boldsymbol{\delta}$.

### Why it matters
First-order expansion linearizes nonlinear functions, the basis of the extended Kalman filter and of gradient steps. Second-order expansion supplies the curvature used by Newton's method and the Laplace approximation. Taylor expansion is also the standard route to approximate otherwise-intractable expectations $\mathbb{E}_x[f(x)] = \int f(x)p(x)\,dx$ under a Gaussian $p(x)$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]