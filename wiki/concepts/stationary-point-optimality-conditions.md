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
id: pkis:concept:stationary-point-optimality-conditions
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch08
tags:
- first-order
- second-order
- Hessian
- saddle-point
- convergence
title: Stationary Point and Optimality Conditions
understanding: 0
---

## Definition
A point $\theta^*$ is a **stationary point** of a differentiable function $L$ if $\nabla L(\theta^*) = 0$. For twice-differentiable functions the full first- and second-order optimality conditions are:

$$\text{Necessary: } \nabla L(\theta^*) = 0 \text{ and } \nabla^2 L(\theta^*) \succeq 0$$
$$\text{Sufficient: } \nabla L(\theta^*) = 0 \text{ and } \nabla^2 L(\theta^*) \succ 0$$

A stationary point may be a local minimum, local maximum, or a **saddle point** (Hessian has both positive and negative eigenvalues). Zero gradient is necessary but not sufficient for a minimum.

### Why it matters
These conditions underpin every iterative optimizer: algorithms terminate when the gradient norm is small, and the Hessian sign determines whether the converged point is a minimum or a saddle — critical for diagnosing optimizers applied to non-convex deep-learning losses.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]