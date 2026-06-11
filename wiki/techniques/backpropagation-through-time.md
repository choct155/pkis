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
- deep-learning
- sequence-modeling
id: pkis:technique:backpropagation-through-time
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch10
- murphy-pml1-intro-ch15
tags:
- RNN
- gradient
- training
- backpropagation
- sequence
title: Backpropagation Through Time (BPTT)
understanding: 0
---

## Definition
$$\nabla_W L = \sum_t \operatorname{diag}\!\left(1-(h^{(t)})^2\right)(\nabla_{h^{(t)}}L)\, h^{(t-1)\top}$$

BPTT is the application of the standard reverse-mode automatic differentiation (backpropagation) algorithm to the *unrolled* computational graph of a recurrent network, propagating gradients backward in time step by step from $t=\tau$ down to $t=1$. Because the same weight matrices $U, V, W$ appear at every step, their total gradient is the sum of per-step contributions.

### Why it matters
BPTT is the canonical training algorithm for RNNs. Its $O(\tau)$ time and memory cost (states must be cached on the forward pass) and its inherently sequential nature are the main practical constraints on training deep sequence models. Understanding BPTT is prerequisite to diagnosing vanishing/exploding gradients and to motivating LSTM, gradient clipping, and truncated BPTT.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]