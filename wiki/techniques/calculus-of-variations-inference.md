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
- mathematics
- probabilistic-inference
- variational-methods
id: pkis:technique:calculus-of-variations-inference
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch19
tags:
- functional-derivative
- Euler-Lagrange
- variational-inference
- Lagrangian
title: Calculus of Variations for Probabilistic Inference
understanding: 0
---

## Definition
A **functional** $J[f]$ maps a function $f$ to a scalar. Its functional (variational) derivative at point $x$ is:

$$\frac{\delta}{\delta f(x)} \int g(f(x), x)\, dx = \frac{\partial}{\partial y} g(f(x), x)$$

Optimizing $J[f]$ is done by setting the functional derivative to zero at every point, analogously to setting the gradient to zero in finite-dimensional optimization.

In probabilistic inference this is used to derive the optimal $q(h_i | v)$ in continuous mean field: one treats $q$ as an unknown function, forms the ELBO as a functional of $q$, differentiates with respect to $q(h_i)$, and solves for the optimal functional form. The Gaussian maximum-entropy derivation (under fixed mean and variance constraints) is a canonical worked example: the Lagrangian functional yields $p(x) = \mathcal{N}(x; \mu, \sigma^2)$.

### Why it matters
Calculus of variations removes the burden of guessing the parametric family of $q$: the functional form is derived automatically from the model structure. It is the mathematical foundation underlying both classical mean field updates and modern amortized variational inference.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]