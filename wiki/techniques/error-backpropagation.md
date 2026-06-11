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
- machine-learning
- numerical-methods
id: pkis:technique:error-backpropagation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch05
tags:
- gradient
- chain-rule
- training
- automatic-differentiation
title: Error Backpropagation
understanding: 0
---

## Definition
An $O(W)$ algorithm for computing $\nabla_{\mathbf{w}} E_n$ in a feed-forward network by applying the chain rule in two passes:

**Forward pass**: given input $\mathbf{x}_n$, compute all pre-activations $a_j = \sum_i w_{ji}z_i$ and activations $z_j = h(a_j)$ up to the output.

**Backward pass**: initialise output errors
$$\delta_k = \frac{\partial E_n}{\partial a_k} = y_k - t_k$$
and recurse through hidden layers via the *backpropagation formula*
$$\delta_j = h'(a_j)\sum_k w_{kj}\delta_k.$$

**Weight gradient**: for every weight $w_{ji}$,
$$\frac{\partial E_n}{\partial w_{ji}} = \delta_j\, z_i.$$

Compared with finite differences ($O(W^2)$), backpropagation delivers all $W$ partial derivatives in $O(W)$ operations, enabling practical gradient descent on networks with millions of parameters.

### Why it matters
Backpropagation is the algorithmic foundation of virtually all neural network training. It generalises immediately to Jacobian and Hessian computation, arbitrary loss functions, and arbitrary feed-forward topologies.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]