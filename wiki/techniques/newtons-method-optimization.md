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
- optimization
- numerical-computation
id: pkis:technique:newtons-method-optimization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch04
- murphy-pml1-intro-ch08
tags:
- second-order
- Hessian
- quadratic-convergence
- quasi-Newton
title: Newton's Method for Optimization
understanding: 0
---

## Definition
Newton's method replaces gradient descent's linear model of $f$ with a local quadratic (second-order Taylor) approximation and jumps to its minimum in one step:

$$\mathbf{x}^{(t+1)} = \mathbf{x}^{(t)} - \mathbf{H}(f)(\mathbf{x}^{(t)})^{-1}\,\nabla_{\mathbf{x}} f(\mathbf{x}^{(t)}).$$

For a strictly convex quadratic $f$, this converges in a single iteration regardless of condition number. For general smooth $f$ near a local minimum, convergence is locally quadratic (error squares each iteration).

### Why it matters
Newton's method is the archetype of all **second-order optimization algorithms**. It naturally incorporates curvature information, eliminating the step-size sensitivity of gradient descent on ill-conditioned problems. However, it is attracted to saddle points (where $\mathbf{H}$ is indefinite) and requires $O(n^2)$ memory and $O(n^3)$ work to invert $\mathbf{H}$, making it impractical for large-scale deep learning without approximations (quasi-Newton, natural gradient, K-FAC).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]