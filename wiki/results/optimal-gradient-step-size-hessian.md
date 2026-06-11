---
aliases: []
also_type: []
applies:
- gradient-descent
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- optimization
- machine-learning
id: pkis:result:optimal-gradient-step-size-hessian
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch04
tags:
- learning-rate
- curvature
- eigenvalue
- step-size
- Hessian
title: Optimal Gradient Descent Step Size from Hessian
understanding: 0
uses:
- hessian-matrix
- condition-number
- taylor-series
---

## Definition
Given the second-order Taylor approximation of $f$ at $\mathbf{x}^{(0)}$ and a gradient step $\mathbf{x}' = \mathbf{x}^{(0)} - \epsilon\mathbf{g}$, the step size that minimises the quadratic approximation is

$$\epsilon^* = \frac{\mathbf{g}^\top\mathbf{g}}{\mathbf{g}^\top\mathbf{H}\mathbf{g}}.$$

In the worst case, when $\mathbf{g}$ aligns with the eigenvector of $\mathbf{H}$ corresponding to $\lambda_{\max}$,

$$\epsilon^* = \frac{1}{\lambda_{\max}}.$$

This shows the Hessian's maximum eigenvalue sets the scale of the safe learning rate for gradient descent.

### Why it matters
This result directly motivates adaptive learning-rate methods (AdaGrad, Adam) and preconditioning: they implicitly approximate $1/\lambda_{\max}$ per-coordinate. It also explains why poorly conditioned problems (large $\lambda_{\max}/\lambda_{\min}$) force tiny global step sizes and slow convergence.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[taylor-series]] — uses
- [[condition-number]] — uses
- [[gradient-descent]] — applies
- [[hessian-matrix]] — uses
[To be populated during integration]