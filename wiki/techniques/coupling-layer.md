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
- generative-models
id: pkis:technique:coupling-layer
instantiates:
- normalizing-flows
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch23
tags:
- normalizing-flow
- coupling
- invertible
- generative-model
title: Coupling Layer (Coupling Flow)
understanding: 0
uses:
- elementwise-flow
- neural-networks
---

## Definition
Given a partition $(u^A, u^B)$ of the input $u \in \mathbb{R}^D$, a coupling layer is defined by
$$x^A = \hat{f}(u^A;\,\Theta(u^B)), \qquad x^B = u^B,$$
where $\hat{f}(\cdot;\theta)$ is a scalar-wise bijection and $\Theta$ is an arbitrary (e.g. deep-network) conditioner. The Jacobian is block-triangular, so $\det J(f) = \det J(\hat{f})$, computable in $O(D)$ when $\hat{f}$ is elementwise.

### Why it matters
Coupling layers allow arbitrarily non-linear dimension mixing through $\Theta$ (any architecture: MLP, CNN, ResNet) while keeping inversion and Jacobian determinant computation cheap. NICE, Real-NVP, GLOW, and neural spline flows are all instances. Alternating partitions (e.g., checkerboard masks) ensure every variable participates.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[neural-networks]] — uses: The conditioner Θ is typically a deep neural network
- [[elementwise-flow]] — uses
- [[normalizing-flows]] — instantiates
[To be populated during integration]