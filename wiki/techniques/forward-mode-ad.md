---
aliases: []
also_type: []
applies:
- neural-networks
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
- numerical-methods
id: pkis:technique:forward-mode-ad
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch06
specializes:
- automatic-differentiation
tags:
- autodiff
- JVP
- tangent
- differentiation
title: Forward-Mode Automatic Differentiation
understanding: 0
uses:
- jvp-vjp
- gradient-and-jacobian
---

## Definition
Given a function $f = f_T \circ \cdots \circ f_1$ and an input perturbation $v$, forward-mode AD computes the Jacobian-vector product (JVP)
$$\partial f(x)[v] = \partial f_T(\cdots)[\cdots[\partial f_2(f_1(x))[\partial f_1(x)[v]]\cdots]]$$
by propagating a **tangent vector** $\dot{x} = v$ forward through the computation graph alongside the primal values $x, f_1(x), f_2(f_1(x)), \ldots$

Intuitively, each primitive node multiplies the running tangent by its local Jacobian before passing it to the next node.

### Why it matters
Forward-mode is preferred when the input dimension $n$ is small relative to the output dimension $m$ (one forward pass per input direction). It uses $O(1)$ additional memory beyond the primal computation, making it attractive for wide outputs or memory-constrained settings. It is the dual of reverse-mode (backpropagation) and both modes compose to enable full Jacobian computation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[neural-networks]] — applies
- [[gradient-and-jacobian]] — uses
- [[jvp-vjp]] — uses
- [[automatic-differentiation]] — specializes
[To be populated during integration]