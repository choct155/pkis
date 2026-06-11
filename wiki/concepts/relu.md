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
- machine-learning
- deep-learning
id: pkis:concept:relu
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch06
tags:
- activation-function
- ReLU
- piecewise-linear
- gradient-flow
title: Rectified Linear Unit (ReLU)
understanding: 0
---

## Definition
The rectified linear unit activation function is defined element-wise as $$g(z) = \max\{0, z\}.$$ It is piecewise linear with two pieces: zero for negative pre-activations and the identity for non-negative ones.

ReLU preserves most properties that make linear models easy to optimize—large, consistent gradients wherever the unit is active—while introducing the nonlinearity required for universal approximation.

### Why it matters
ReLU is the default hidden-unit activation in modern feedforward networks. Unlike sigmoid/tanh units, ReLU does not saturate for positive inputs, so gradients do not vanish during backprop in that regime. Its piecewise-linear structure means the second derivative is zero almost everywhere, making gradient directions highly informative. The set of functions representable by deep ReLU networks grows exponentially with depth (Montufar et al., 2014), providing formal justification for depth.

### Generalizations
- **Leaky ReLU**: $h_i = \max(0,z_i) + \alpha_i \min(0,z_i)$ with fixed small $\alpha_i$.
- **PReLU**: $\alpha_i$ is a learned parameter.
- **Absolute value rectification**: $\alpha_i = -1$, giving $|z|$.
- **Maxout**: outputs $\max_{j \in G^{(i)}} z_j$ over groups of $k$ linear filters, learning the activation function itself.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]