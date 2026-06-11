---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- deep-learning
- sequence-modeling
id: pkis:framework:gated-recurrent-unit
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch10
- murphy-pml1-intro-ch15
tags:
- gated-RNN
- update-gate
- reset-gate
- long-term-dependencies
- GRU
title: Gated Recurrent Unit (GRU)
understanding: 0
---

## Definition
The **GRU** (Cho et al., 2014b) is a simplified gated RNN that merges the LSTM's forget and input gates into a single **update gate** $u_i^{(t)}$ and adds a **reset gate** $r_i^{(t)}$:
$$h_i^{(t)} = u_i^{(t-1)} h_i^{(t-1)} + (1 - u_i^{(t-1)})\,\sigma\!\left(b_i + U x^{(t-1)} + W (r^{(t-1)} \odot h^{(t-1)})\right)$$
$$u_i^{(t)} = \sigma\!\left(b_i^u + U^u x^{(t)} + W^u h^{(t)}\right)$$
$$r_i^{(t)} = \sigma\!\left(b_i^r + U^r x^{(t)} + W^r h^{(t)}\right)$$

The update gate acts as a conditional leaky integrator, linearly interpolating between copying the past state and adopting a new candidate state. The reset gate determines how much of the past state influences the candidate.

### Why it matters
GRUs have fewer parameters than LSTMs (no separate cell state or output gate) while achieving comparable empirical performance on many tasks. They are preferred when computational budget or data is limited. The architectural competition between GRU and LSTM remains largely task-dependent.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]