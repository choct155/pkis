---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- deep-learning
id: pkis:concept:activation-functions
knowledge_type: concept
maturity: settled
related_concepts:
- '[[neural-networks]]'
- '[[vanishing-gradient-problem]]'
- '[[universal-approximation-theorem]]'
- '[[backpropagation]]'
sources:
- '[[nielsen-nndl]]'
- nielsen-nndl-ch04
tags:
- neural-networks
- nonlinearity
- sigmoid
- tanh
- relu
title: Activation Functions
understanding: 0
---

Element-wise nonlinear functions applied after each linear transformation in a neural network layer, providing the expressive power necessary for universal approximation; common choices include sigmoid σ(z) = 1/(1+e^{−z}) (smooth, bounded, saturates), tanh (zero-centered sigmoid rescaling), and rectified linear units (ReLU) max(0,z) (non-saturating, sparse, computationally efficient); the choice affects gradient flow, saturation behavior, and training speed.

## Reading Path
- [[nielsen-nndl-ch03]] (unread) — covers sigmoid, tanh, and ReLU with motivation for each; theoretical argument for zero-centering of tanh over sigmoid
- [[nielsen-nndl-ch04]] (unread) — activation functions as the mechanism enabling universal approximation