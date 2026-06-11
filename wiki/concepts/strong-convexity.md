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
extends:
- stationary-point-optimality-conditions
id: pkis:concept:strong-convexity
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch08
specializes:
- convex-set-and-function
tags:
- convexity
- condition-number
- convergence-rate
- Hessian
title: Strong Convexity
understanding: 0
uses:
- condition-number-hessian
---

## Definition
A differentiable function $f : \mathbb{R}^n \to \mathbb{R}$ is **strongly convex** with parameter $m > 0$ if for all $x, y$ in its domain:

$$\bigl(\nabla f(x) - \nabla f(y)\bigr)^T(x - y) \;\geq\; m\|x - y\|_2^2$$

Equivalently (when $f$ is twice differentiable): $\nabla^2 f(x) \succeq mI$ for all $x$. Strong convexity implies strict convexity but not vice versa.

### Why it matters
Strong convexity guarantees a **unique** global minimum and gives explicit linear convergence rates for gradient descent (rate $\mu = (\kappa - 1)/(\kappa + 1)$ where $\kappa = \lambda_{\max}/\lambda_{\min}$). It is the key assumption for proving that SGD and its variants converge at linear rather than sub-linear rates on well-conditioned problems.

### Connection to condition number
The ratio $\kappa = L/m$ (Lipschitz constant of gradient divided by strong-convexity constant) is the condition number, and directly determines how much momentum or preconditioning can help.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[stationary-point-optimality-conditions]] — extends
- [[condition-number-hessian]] — uses
- [[convex-set-and-function]] — specializes
[To be populated during integration]