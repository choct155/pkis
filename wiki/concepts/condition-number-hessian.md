---
aliases: []
also_type: []
applies:
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
- optimization
- linear-algebra
id: pkis:concept:condition-number-hessian
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch08
tags:
- convergence-rate
- ill-conditioning
- preconditioning
- gradient-descent
title: Condition Number of Hessian
understanding: 0
uses:
- hessian-matrix
- strong-convexity
---

## Definition
The **condition number** of a positive-definite matrix $A$ (or the Hessian $H$ at a critical point) is

$$\kappa(A) = \frac{\lambda_{\max}(A)}{\lambda_{\min}(A)} \geq 1$$

For steepest descent with exact line search applied to a quadratic $L(\theta) = \frac{1}{2}\theta^T A\theta + b^T\theta + c$, the linear convergence rate is

$$\mu = \left(\frac{\kappa - 1}{\kappa + 1}\right)^2$$

so a large $\kappa$ (ill-conditioned problem) implies slow convergence. For non-quadratic functions the local rate depends on $\kappa(H^*)$ at the optimum.

### Why it matters
The condition number is the fundamental quantity governing first-order optimizer speed. It motivates second-order methods (Newton, BFGS) and preconditioning strategies that aim to reduce the effective condition number, as well as batch normalization and weight normalization in deep learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[strong-convexity]] — uses
- [[gradient-descent]] — applies
- [[hessian-matrix]] — uses
[To be populated during integration]