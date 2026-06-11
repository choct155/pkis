---
aliases: []
also_type: []
applies:
- vanishing-exploding-gradients-rnn
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
- sequence-modeling
extends:
- recurrent-neural-network
id: pkis:concept:leaky-units-multiscale-rnn
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- long-short-term-memory
related_concepts: []
sources:
- goodfellow-deeplearning-ch10
tags:
- RNN
- time-constant
- skip-connection
- multi-scale
- long-term-dependencies
title: Leaky Units and Multi-Scale RNN
understanding: 0
---

## Definition
A **leaky unit** maintains a running average of its previous state via a linear self-connection with weight $\alpha \in (0,1)$:
$$\mu^{(t)} \leftarrow \alpha\, \mu^{(t-1)} + (1-\alpha)\, v^{(t)}.$$
When $\alpha \approx 1$ the unit retains information for many steps; when $\alpha \approx 0$ it acts like a standard unit. Multi-scale RNNs assign different time constants to different groups of units, or use **skip connections** (delays of $d>1$ steps) to shorten the effective gradient path from $O(\tau)$ to $O(\tau/d)$, or actively remove short-lag connections to force units to operate at coarse time scales.

### Why it matters
Leaky units are a continuous, differentiable precursor to LSTM gating (Mozer, 1992; El Hihi & Bengio, 1996). They motivate the GRU update gate, which can be seen as an input-conditioned leaky integrator. Multi-scale hierarchical processing also underlies clockwork RNNs (Koutnik et al., 2014) and the hierarchical structure of deep RNNs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[long-short-term-memory]] — prerequisite-of
- [[vanishing-exploding-gradients-rnn]] — applies
- [[recurrent-neural-network]] — extends
[To be populated during integration]