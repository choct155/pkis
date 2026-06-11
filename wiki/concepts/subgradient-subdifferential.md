---
aliases: []
also_type: []
applies:
- lasso
- hinge-loss
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
- convex-set-and-function
id: pkis:concept:subgradient-subdifferential
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch08
tags:
- non-smooth
- convex-analysis
- lasso
- proximal
title: Subgradient and Subdifferential
understanding: 0
---

## Definition
For a convex function $f : \mathbb{R}^n \to \mathbb{R}$, a vector $\mathbf{g} \in \mathbb{R}^n$ is a **subgradient** of $f$ at $\mathbf{x}$ if

$$f(\mathbf{z}) \geq f(\mathbf{x}) + \mathbf{g}^T(\mathbf{z} - \mathbf{x}), \quad \forall\, \mathbf{z} \in \text{dom}(f)$$

The set of all subgradients at $\mathbf{x}$ is the **subdifferential** $\partial f(\mathbf{x})$. When $f$ is differentiable at $\mathbf{x}$, the subdifferential is the singleton $\{\nabla f(\mathbf{x})\}$. For example, $\partial|x| = \{-1\}$ if $x < 0$, $[-1,1]$ if $x = 0$, $\{+1\}$ if $x > 0$.

### Why it matters
Subgradients extend gradient-based optimality conditions to non-smooth objectives (e.g., $\ell_1$ regularization, hinge loss). The optimality condition $0 \in \partial f(\theta^*)$ replaces $\nabla f(\theta^*) = 0$ for non-smooth problems, enabling algorithms such as proximal gradient and subgradient descent.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hinge-loss]] — applies
- [[lasso]] — applies
- [[convex-set-and-function]] — extends
[To be populated during integration]