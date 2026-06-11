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
id: pkis:technique:autoregressive-flow
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch23
tags:
- normalizing-flow
- autoregressive
- MAF
- IAF
- masked-network
title: Autoregressive Flow
understanding: 0
---

## Definition
An autoregressive bijection $f : \mathbb{R}^D \to \mathbb{R}^D$ is defined component-wise by
$$x_i = h(u_i;\,\Theta_i(x_{1:i-1})), \quad i = 1, \ldots, D,$$
where $h(\cdot;\theta)$ is a scalar bijection and $\Theta_i$ is an arbitrary conditioner. The Jacobian is lower-triangular, giving
$$\det J(f) = \prod_{i=1}^D \frac{dh}{du_i}.$$
The forward direction $f$ is sequential ($O(D)$ serial steps); the inverse $f^{-1}$ is parallel. The **Masked Autoregressive Flow (MAF)** variant shares conditioner parameters via masked MLPs (MADE), enabling fast density evaluation but slow sampling. The **Inverse Autoregressive Flow (IAF)** reverses the dependency to $\Theta_i(u_{1:i-1})$, enabling fast sampling but slow density evaluation.

### Why it matters
Autoregressive flows unify autoregressive generative models and normalizing flows: any continuous autoregressive model can be re-expressed as a one-layer autoregressive flow via inverse-CDF reparameterization. Stacking layers with permutations dramatically increases expressiveness.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]