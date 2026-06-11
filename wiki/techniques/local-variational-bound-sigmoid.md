---
aliases: []
also_type: []
applies:
- logistic-regression
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
- approximate-inference
id: pkis:technique:local-variational-bound-sigmoid
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch10
tags:
- logistic-sigmoid
- variational-bound
- Jaakkola-Jordan
- Gaussian-approximation
- local-variational
title: Local Variational Bound for Logistic Sigmoid
understanding: 0
uses:
- convex-set-and-function
- convex-conjugate
- taylor-series
- gaussian-distribution
---

## Definition
Using the convexity of $f(x)=-\ln(e^{x/2}+e^{-x/2})$ in the variable $x^2$, a lower bound on the logistic sigmoid is obtained by a first-order Taylor expansion in $x^2$ around $\xi^2$:

$$\sigma(x) \geq \sigma(\xi)\exp\!\left\{\tfrac{x-\xi}{2} - \lambda(\xi)(x^2-\xi^2)\right\}$$

where $\lambda(\xi) = \frac{1}{2\xi}\left[\sigma(\xi)-\tfrac{1}{2}\right]$. The bound is Gaussian in shape (exponential of a quadratic), tight at $x=\xi$, and is parameterized by a variational parameter $\xi$.

### Why it matters
Converts an intractable logistic-likelihood integral $\int\sigma(\mathbf{w}^T\boldsymbol{\phi})\,p(\mathbf{w})\,d\mathbf{w}$ into an analytically tractable Gaussian integral, enabling fully Bayesian logistic regression via a closed-form Gaussian posterior approximation. Also used in the Jaakkola–Jordan variational EM for Bayesian classification.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gaussian-distribution]] — uses
- [[taylor-series]] — uses
- [[logistic-regression]] — applies
- [[convex-conjugate]] — uses
- [[convex-set-and-function]] — uses
[To be populated during integration]