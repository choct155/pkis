---
aliases: []
also_type: []
applies:
- solving-linear-systems
- gradient-descent
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
- numerical-computation
- linear-algebra
- optimization
id: pkis:concept:condition-number
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- numerical-underflow-overflow
- first-order-vs-second-order-optimization
related_concepts: []
sources:
- goodfellow-deeplearning-ch04
- murphy-pml1-intro-ch07
specializes:
- linear-algebra
tags:
- ill-conditioned
- eigenvalue
- matrix-inversion
- numerical-stability
title: Condition Number
understanding: 0
uses:
- hessian-matrix
- eigendecomposition
- singular-value-decomposition
- positive-definite-matrix
---

## Definition
For a square matrix $A$ with eigenvalue decomposition, the condition number is

$$\kappa(A) = \max_{i,j} \left|\frac{\lambda_i}{\lambda_j}\right|,$$

i.e., the ratio of the largest to smallest eigenvalue magnitude. More generally, $\kappa(A) = \|A\|\,\|A^{-1}\|$ for any consistent matrix norm.

It quantifies how much a small perturbation in the input is amplified in the output of $f(\mathbf{x}) = A^{-1}\mathbf{x}$; a large condition number signals that the system is *ill-conditioned*.

### Why it matters
An ill-conditioned Hessian causes gradient descent to perform poorly: the optimal step size is $1/\lambda_{\max}$, which is far too small to make progress along low-curvature directions. Understanding conditioning is prerequisite to choosing learning rates and to motivating second-order and preconditioning methods.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gradient-descent]] — applies
- [[positive-definite-matrix]] — uses
- [[solving-linear-systems]] — applies
- [[singular-value-decomposition]] — uses
- [[linear-algebra]] — specializes
- [[first-order-vs-second-order-optimization]] — prerequisite-of
- [[numerical-underflow-overflow]] — prerequisite-of
- [[eigendecomposition]] — uses
- [[hessian-matrix]] — uses
[To be populated during integration]