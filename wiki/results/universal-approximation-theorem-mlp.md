---
aliases: []
also_type: []
applies:
- deep-feedforward-network
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- deep-learning
- approximation-theory
id: pkis:result:universal-approximation-theorem-mlp
knowledge_type: result
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- depth-efficiency-rectifier-networks
related_concepts: []
sources:
- goodfellow-deeplearning-ch06
specializes:
- universal-approximation-theorem
tags:
- expressivity
- depth
- width
- approximation
- squashing-function
title: Universal Approximation Theorem (Neural Networks)
understanding: 0
---

## Definition
A feedforward network with a linear output layer and at least one hidden layer with a squashing (e.g., sigmoidal) or non-polynomial activation function can approximate any Borel measurable function $f:\mathbb{R}^m\to\mathbb{R}^n$ to arbitrary precision in the sup-norm, provided sufficiently many hidden units are available (Hornik et al., 1989; Cybenko, 1989; extended to ReLU by Leshno et al., 1993). Formally, for any $\epsilon > 0$ and continuous $f$ on a compact set, there exists a one-hidden-layer network $\hat{f}$ such that $\sup_x \|f(x)-\hat{f}(x)\| < \epsilon$.

The theorem guarantees expressive capacity but not learnability: exponentially many units may be required for a shallow network, and no training algorithm is guaranteed to find the approximating parameters.

### Why it matters
The theorem justifies using neural networks as general-purpose function approximators and motivates the depth-vs-width tradeoff. It is paired with the exponential-depth-advantage result (Montufar et al., 2014): deep rectifier networks can represent exponentially more linear regions than shallow networks of the same parameter count, providing formal grounding for the empirical success of depth.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[depth-efficiency-rectifier-networks]] — prerequisite-of
- [[deep-feedforward-network]] — applies
- [[universal-approximation-theorem]] — specializes: Chapter version adds ReLU case and depth-efficiency context.
[To be populated during integration]