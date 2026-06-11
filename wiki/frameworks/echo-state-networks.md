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
- dynamical-systems
id: pkis:framework:echo-state-networks
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch10
tags:
- reservoir
- spectral-radius
- ESN
- liquid-state-machine
- fixed-weights
- edge-of-chaos
title: Echo State Networks / Reservoir Computing
understanding: 0
---

## Definition
In **reservoir computing** (Lukoševičius & Jaeger, 2009), the input and recurrent weights of an RNN are fixed (randomly initialized and not trained); only the readout (output) weights are learned, typically via linear regression. The fixed recurrent network — the *reservoir* — maps an arbitrary-length input history to a fixed-length state vector $h^{(t)}$, which is treated as a rich nonlinear feature vector. The **spectral radius** $\rho(J)$ of the state-to-state Jacobian $J^{(t)} = \partial s^{(t)}/\partial s^{(t-1)}$ is set near 1 (or slightly above with saturating nonlinearities) to balance memory and stability (the *edge of chaos*).

**Echo State Networks** (Jaeger, 2003/2004) use continuous-valued hidden units; **Liquid State Machines** (Maass et al., 2002) use spiking neurons. Both fall under reservoir computing.

### Why it matters
Reservoir computing makes training convex (linear output layer), avoiding BPTT and the vanishing/exploding gradient problem entirely. It connects RNN dynamics to kernel methods and dynamical systems theory. ESN weight initialization has also been shown to improve fully-trained RNNs as a warm-start (Sutskever et al., 2013).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]