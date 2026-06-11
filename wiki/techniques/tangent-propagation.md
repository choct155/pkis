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
- machine-learning
- neural-networks
id: pkis:technique:tangent-propagation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch05
- goodfellow-deeplearning-ch07
tags:
- invariance
- regularisation
- data-augmentation
- Jacobian
title: Tangent Propagation
understanding: 0
---

## Definition
A regularisation technique that enforces approximate local invariance of a network's outputs to a continuous transformation $s(\mathbf{x}, \xi)$ (e.g. rotation, translation). The tangent vector at each training point is
$$\boldsymbol{\tau}_n = \left.\frac{\partial s(\mathbf{x}_n,\xi)}{\partial\xi}\right|_{\xi=0}.$$
An invariance penalty is added to the loss:
$$\tilde{E} = E + \frac{\lambda}{2}\sum_n\sum_k\left(\sum_i J_{nki}\,\tau_{ni}\right)^2$$
where $\mathbf{J}$ is the network Jacobian.

For small-variance additive noise ($\mathbf{x}\to\mathbf{x}+\boldsymbol{\xi}$) the penalty reduces to **Tikhonov regularisation** $\Omega = \tfrac{1}{2}\int\|\nabla y(\mathbf{x})\|^2 p(\mathbf{x})\,d\mathbf{x}$, equivalent to training with noisy inputs.

### Why it matters
Provides a principled alternative to data augmentation for building transformation invariance into neural networks. The regulariser's derivatives with respect to weights are obtained via an extended backpropagation pass, making it computationally feasible.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]