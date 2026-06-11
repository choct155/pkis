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
- generative-models
id: pkis:concept:elementwise-flow
instantiates:
- normalizing-flows
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch23
tags:
- normalizing-flow
- scalar-bijection
- monotone-function
title: Elementwise Flow
understanding: 0
uses:
- activation-functions
---

## Definition
An elementwise flow applies a scalar bijection $h : \mathbb{R} \to \mathbb{R}$ independently to each dimension:
$$f(u) = (h(u_1; \theta_1), \ldots, h(u_D; \theta_D)).$$
The Jacobian is diagonal, so $\det J(f) = \prod_{i=1}^D \frac{dh}{du_i}$, computable in $O(D)$.

### Why it matters
Elementwise flows alone do not mix dimensions, but they are the key building block inside coupling layers and autoregressive layers. The scalar bijection $h$ can be an affine function, a monotonic MLP (all-positive-weight network), an integral of a positive neural network (UMNN), or a piecewise-rational spline (neural spline flow), trading expressiveness against analytical tractability of the inverse.

### Scalar bijection constructions
- **Affine**: $h(u) = au + b$, $a > 0$.
- **Non-linear squared**: adds inverse-quadratic perturbation, closed-form inverse.
- **Monotonic MLP**: positive-weight composition of sigmoids; bisection inverse.
- **UMNN**: integrate a positive neural network derivative numerically.
- **Polynomial**: integrate squared polynomial; closed-form integral.
- **Spline**: piecewise-rational/polynomial through learnable knots.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[activation-functions]] — uses: Strictly monotone activations serve as scalar bijections
- [[normalizing-flows]] — instantiates
[To be populated during integration]