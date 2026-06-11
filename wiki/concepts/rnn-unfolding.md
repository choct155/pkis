---
aliases: []
also_type: []
applies:
- recurrent-neural-network
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
id: pkis:concept:rnn-unfolding
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- backpropagation-through-time
related_concepts: []
sources:
- goodfellow-deeplearning-ch10
tags:
- RNN
- computational-graph
- parameter-sharing
- DAG
- unrolling
title: RNN Computational Graph Unfolding
understanding: 0
uses:
- automatic-differentiation
---

## Definition
**Unfolding** (or unrolling) converts a recurrent computation with cycles,
$$h^{(t)} = f(h^{(t-1)}, x^{(t)}; \theta),$$
into an equivalent directed acyclic graph (DAG) by replicating the state node and the function $f$ once per time step:
$$h^{(\tau)} = g^{(\tau)}(x^{(\tau)}, \ldots, x^{(1)}) = f(f(\cdots f(h^{(0)}, x^{(1)}; \theta) \cdots, x^{(\tau-1)}; \theta), x^{(\tau)}; \theta).$$

Two key benefits follow: (1) the model input size is fixed (transition from one state to the next) regardless of sequence length; (2) parameter sharing across time steps is made explicit, enabling standard backpropagation on the unrolled DAG.

### Why it matters
Unfolding is the conceptual foundation that connects RNNs to feedforward networks and makes BPTT a straightforward application of the chain rule. It also clarifies why training cost is $O(\tau)$ and cannot be parallelized across time steps.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[backpropagation-through-time]] — prerequisite-of
- [[automatic-differentiation]] — uses
- [[recurrent-neural-network]] — applies
[To be populated during integration]