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
- optimization
- machine-learning
id: pkis:concept:critical-points-saddle-points
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch04
tags:
- saddle-point
- local-minimum
- second-derivative-test
- Hessian
- gradient-descent
title: Critical Points and Saddle Points
understanding: 0
uses:
- gradient-descent
- hessian-matrix
---

## Definition
A **critical point** (stationary point) of $f:\mathbb{R}^n\to\mathbb{R}$ is any $\mathbf{x}^*$ where $\nabla_{\mathbf{x}} f(\mathbf{x}^*) = \mathbf{0}$. Critical points are classified by the Hessian $\mathbf{H}$ at $\mathbf{x}^*$:

| $\mathbf{H}$ spectrum | Type |
|---|---|
| All eigenvalues $> 0$ | local minimum |
| All eigenvalues $< 0$ | local maximum |
| Mixed signs | **saddle point** |
| Some zero eigenvalues | inconclusive |

A saddle point is simultaneously a local minimum in some directions and a local maximum in others.

### Why it matters
Deep neural network loss surfaces are dominated by saddle points rather than poor local minima. Gradient descent (a first-order method) is not attracted to saddle points unless the gradient points directly toward them, but second-order methods like Newton's method can be attracted to them, motivating trust-region and damping modifications.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hessian-matrix]] — uses
- [[gradient-descent]] — uses
[To be populated during integration]