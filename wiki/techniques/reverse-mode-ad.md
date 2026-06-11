---
aliases: []
also_type: []
applies:
- deep-reinforcement-learning
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
generalizes:
- backpropagation
id: pkis:technique:reverse-mode-ad
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
- VJP
- adjoint
- backprop
- gradient
title: Reverse-Mode Automatic Differentiation (Backpropagation)
understanding: 0
uses:
- jvp-vjp
- gradient-and-jacobian
---

## Definition
Given a function $f = f_T \circ \cdots \circ f_1$ and an output perturbation (adjoint) $u$, reverse-mode AD computes the vector-Jacobian product (VJP)
$$\partial f(x)^\top[u] = \partial f_1(x)^\top[\partial f_2(f_1(x))^\top[\cdots[\partial f_T(\cdots)^\top[u]\cdots]]]$$
by first executing a **forward pass** to store all intermediate values (the "tape"), then executing a **backward pass** that propagates adjoint vectors in reverse topological order, accumulating them at fan-out nodes via summation.

Intuitively, the backward pass is a transposed version of the forward pass; each node multiplies the incoming adjoint by its transposed local Jacobian.

### Why it matters
Reverse-mode is preferred when $m \ll n$ — exactly the setting of scalar loss functions in deep learning (one backward pass gives the full gradient). It is the foundation of the backpropagation algorithm. Its main cost is memory: all primal intermediates must be retained (or recomputed via checkpointing) for the backward pass.

### Fan-out handling
At fan-out nodes (a value used by multiple downstream operations), the backward pass **sums** the incoming adjoint contributions, which corresponds to the transposed Jacobian of the duplication map $\text{dup}(x)=(x,x)$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[neural-networks]] — applies
- [[deep-reinforcement-learning]] — applies
- [[gradient-and-jacobian]] — uses
- [[backpropagation]] — generalizes
- [[jvp-vjp]] — uses
- [[automatic-differentiation]] — specializes
[To be populated during integration]