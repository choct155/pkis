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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- deep-learning
- statistical-learning
id: pkis:technique:chain-rule-multivariate
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch05
tags: []
title: Chain Rule (Multivariate)
understanding: 0
---

## Definition
The chain rule differentiates a composition of functions by multiplying the derivatives of the constituent maps; in the multivariate case these derivatives are Jacobian matrices.

$$\frac{\partial}{\partial x}\big(g \circ f\big)(x) = \frac{\partial g}{\partial f}\,\frac{\partial f}{\partial x}.$$

It is the rule that lets us compute the gradient of deeply nested functions one elementary step at a time.

### Dimension bookkeeping
Written with the numerator (row-vector gradient) layout, the chain rule reduces to ordinary matrix multiplication: the shared factor $\partial f$ appears in the denominator of the first factor and numerator of the second, so dimensions match and it formally cancels. For $f:\mathbb{R}^n\to\mathbb{R}^m$ and inputs depending on $(s,t)$, the result is the matrix product $\frac{\partial f}{\partial x}\frac{\partial x}{\partial(s,t)}$.

### Worked pattern
For a least-squares loss $L(\mathbf{e}) = \|\mathbf{e}\|^2$ with $\mathbf{e}(\boldsymbol{\theta}) = \mathbf{y} - \Phi\boldsymbol{\theta}$, the chain rule gives $\frac{\partial L}{\partial \boldsymbol{\theta}} = \frac{\partial L}{\partial \mathbf{e}}\frac{\partial \mathbf{e}}{\partial \boldsymbol{\theta}} = -2\mathbf{e}^\top \Phi$, avoiding the unwieldy expression from differentiating the expanded form directly.

### Why it matters
The chain rule is the engine of backpropagation and automatic differentiation: a deep network $y = (f_K \circ \cdots \circ f_1)(x)$ has its loss gradient assembled by chaining per-layer Jacobians, and intermediate products are reused across layers. Writing gradients explicitly is impractical for deep compositions, so the chain rule applied stepwise over a computation graph is what makes large-scale gradient computation feasible.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]