---
aliases: []
also_type: []
applies:
- deep-feedforward-network
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
- deep-learning
- numerical-methods
id: pkis:technique:backpropagation-algorithm
instantiates:
- backpropagation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- gradient-descent
related_concepts: []
sources:
- goodfellow-deeplearning-ch06
specializes:
- automatic-differentiation
tags:
- gradient-computation
- chain-rule
- computational-graph
- autodiff
- dynamic-programming
title: Backpropagation Algorithm
understanding: 0
uses:
- computational-graph
- chain-rule-multivariate
---

## Definition
Backpropagation is an $O(|E|)$ algorithm for computing the gradient $\nabla_\theta J(\theta)$ of a scalar loss $J$ with respect to all parameters in a computational graph $G = (V, E)$. It proceeds in two passes:
1. **Forward pass**: evaluate each node $u^{(i)} = f^{(i)}(\text{parents}(u^{(i)}))$ in topological order, caching intermediate activations.
2. **Backward pass**: initialize $\partial u^{(n)}/\partial u^{(n)} = 1$ and propagate gradients in reverse topological order via the multivariate chain rule: $$\frac{\partial u^{(n)}}{\partial u^{(j)}} = \sum_{i:\,j\in\text{Pa}(u^{(i)})} \frac{\partial u^{(n)}}{\partial u^{(i)}} \frac{\partial u^{(i)}}{\partial u^{(j)}}.$$ Each edge is visited exactly once; dynamic programming avoids the exponentially many paths of naive chain-rule expansion.

Backprop is a specific efficient implementation of the chain rule on DAGs; it computes the gradient, not the full Hessian.

### Why it matters
Without backprop, gradient-based training of deep networks would require $O(|E|^2)$ or exponential time. The algorithm scales linearly in graph size and enables training networks with billions of parameters. Modern autodiff frameworks (TensorFlow, PyTorch) implement the symbol-to-symbol variant, building a gradient graph that itself can be differentiated for higher-order derivatives.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[deep-feedforward-network]] — applies
- [[gradient-descent]] — prerequisite-of
- [[automatic-differentiation]] — specializes
- [[chain-rule-multivariate]] — uses
- [[computational-graph]] — uses
- [[backpropagation]] — instantiates: Chapter formalizes backprop as efficient chain-rule evaluation on a DAG.
[To be populated during integration]