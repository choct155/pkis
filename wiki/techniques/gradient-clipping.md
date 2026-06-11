---
aliases: []
also_type: []
applies:
- vanishing-exploding-gradients-rnn
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
- optimization
extends:
- stochastic-gradient-descent
id: pkis:technique:gradient-clipping
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch10
tags:
- RNN
- optimization
- gradient
- exploding-gradient
- training-stability
title: Gradient Clipping
understanding: 0
uses:
- backpropagation-through-time
---

## Definition
**Gradient clipping** rescales the parameter gradient $\mathbf{g}$ before applying the update whenever its norm exceeds a threshold $v$:
$$\text{if } \|\mathbf{g}\| > v, \quad \mathbf{g} \leftarrow \frac{v}{\|\mathbf{g}\|}\mathbf{g}.$$
Element-wise clipping (Mikolov, 2012) clips each coordinate independently, while norm clipping (Pascanu et al., 2013) preserves gradient direction.

### Why it matters
RNN loss surfaces contain 'cliff' regions where the gradient norm spikes catastrophically, throwing parameters far from a good solution. Clipping ensures the effective step size remains bounded in these regions without discarding gradient direction information. It is a standard, low-cost intervention in RNN and Transformer training pipelines and is particularly critical when combined with regularizers that encourage gradient flow (Pascanu et al., 2013).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[stochastic-gradient-descent]] — extends
- [[backpropagation-through-time]] — uses
- [[vanishing-exploding-gradients-rnn]] — applies: Addresses the exploding gradient aspect
[To be populated during integration]