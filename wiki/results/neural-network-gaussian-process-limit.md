---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- statistical-learning
- bayesian-stats
id: pkis:result:neural-network-gaussian-process-limit
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch45
tags:
- gaussian-process
- neural-networks
- infinite-width
- bayesian-neural-networks
- weight-decay
title: Neural Network → Gaussian Process Limit (Infinite Width)
understanding: 0
---

## Definition
**Neal's result (1996):** the prior over functions defined by a one-hidden-layer neural network with weight $\mathbf{w}$ priors,
$$y(\mathbf{x};\mathbf{w})=\sum_{h=1}^{H} w_h^{(2)}\tanh\!\Big(\sum_i w_{hi}^{(1)}x_i+w_{h0}^{(1)}\Big)+w_0^{(2)},$$
*converges to a Gaussian process* as the number of hidden units $H\to\infty$, provided standard scaled 'weight-decay' (Gaussian) priors are placed on the weights. The covariance function of the limiting GP is determined by the weight priors and the hidden-unit activation function.

### Why it holds
Each hidden unit contributes an independent, identically distributed term to the output. If the output-weight variance is scaled as $\sim 1/H$, the sum of $H$ such i.i.d. contributions obeys the central limit theorem, so the output — and jointly the outputs at any finite set of inputs — becomes Gaussian. This is exactly the defining property of a GP.

### Why it matters
The result demystifies Bayesian neural networks: in the wide-network limit, the implicit prior over functions is *just a Gaussian process*, and the architecture/weight priors merely select a kernel. It explains why GP samples and wide-MLP prior samples look so similar, and it reframes the apparent power of neural nets as, in this regime, sophisticated smoothing. It also motivates the question of whether feature discovery — the part GPs cannot do — survives outside this limit.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]