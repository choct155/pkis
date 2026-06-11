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
- machine-learning
- bayesian-inference
- probabilistic-graphical-models
id: pkis:framework:variational-inference-framework
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch10
tags:
- variational-inference
- ELBO
- posterior-approximation
- optimization
title: Variational Inference (VI)
understanding: 0
---

## Definition
$$q^* = \underset{q \in \mathcal{Q}}{\operatorname{argmin}}\; D_{\mathrm{KL}}(q_\psi(z) \| p_\theta(z|x))$$

Variational inference (VI) reduces posterior inference to optimization: rather than sampling from an intractable posterior $p_\theta(z|x)$, one finds the member $q_\psi$ of a tractable family $\mathcal{Q}$ that is closest in KL divergence. Because $\log p_\theta(x)$ is constant w.r.t. $\psi$, minimizing the KL is equivalent to maximizing the **ELBO** $\mathcal{L}(\theta,\psi|x) = \mathbb{E}_{q_\psi}[\log p_\theta(x,z) - \log q_\psi(z)]$, or equivalently minimizing the variational free energy.

### Why it matters
VI scales approximate Bayesian inference to large models and datasets — it underpins VAEs, topic models, and probabilistic programming — offering a tractable alternative to MCMC with GPU-friendly, gradient-based implementations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]