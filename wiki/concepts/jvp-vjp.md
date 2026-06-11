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
- numerical-methods
- optimization
id: pkis:concept:jvp-vjp
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch06
tags:
- autodiff
- Jacobian
- gradient
- forward-mode
- reverse-mode
title: Jacobian-Vector Product and Vector-Jacobian Product
understanding: 0
---

## Definition
For a differentiable function $f: \mathbb{R}^n \to \mathbb{R}^m$ at a linearization point $x \in \mathbb{R}^n$:

**JVP (forward mode):** given perturbation $v \in \mathbb{R}^n$,
$$\text{JVP}(x, v) = \partial f(x)[v] \in \mathbb{R}^m$$

**VJP (reverse mode):** given co-tangent $u \in \mathbb{R}^m$,
$$\text{VJP}(x, u) = \partial f(x)^\top[u] \in \mathbb{R}^n$$

Neither requires materializing the full $m \times n$ Jacobian matrix; both can be computed in $O(\text{cost}(f))$ time.

### Why it matters
JVP and VJP are the two fundamental primitives of automatic differentiation. Every AD system (JAX, PyTorch, TensorFlow) is built around efficient implementations of one or both. For scalar loss functions ($m=1$) the VJP gives the full gradient in a single pass — this is why reverse-mode AD dominates deep learning. JVPs are preferred for Jacobian rows, directional derivatives, and second-order computations (via JVP-of-VJP = Hessian-vector product).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]