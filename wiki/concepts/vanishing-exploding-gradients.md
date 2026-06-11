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
- deep-learning
- optimization
- recurrent-networks
id: pkis:concept:vanishing-exploding-gradients
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch08
- murphy-pml1-intro-ch13
tags:
- gradients
- deep-learning
- recurrent-networks
- stability
title: Vanishing and Exploding Gradients
understanding: 0
---

## Definition
In a deep network (or recurrent network) with $t$ layers/time-steps, gradients are multiplied by the Jacobian (or weight matrix $\mathbf{W}$) at each step. For a repeated matrix multiplication $\mathbf{W}^t = V\,\text{diag}(\lambda)^t V^{-1}$:
- Eigenvalues $|\lambda_i|>1$ cause gradients to grow exponentially (*exploding gradients*).
- Eigenvalues $|\lambda_i|<1$ cause gradients to shrink exponentially (*vanishing gradients*).

Intuition: the network is effectively running the power method, amplifying or suppressing components of the gradient vector along eigenvectors of the weight matrix.

### Why it matters
Vanishing gradients make it impossible to assign credit to early layers/time-steps; exploding gradients cause unstable parameter updates. These pathologies are the primary reason vanilla RNNs fail on long sequences and motivate gradient clipping, careful weight initialisation (Glorot, orthogonal), LSTM/GRU gating, and residual connections. Feedforward networks largely avoid this problem because they use different weight matrices at each layer.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]