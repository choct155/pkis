---
aliases: []
also_type: []
applies:
- intractable-posterior
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
uses:
- elbo
- kl-divergence
- variational-free-energy
---

## Definition
$$q^* = \underset{q \in \mathcal{Q}}{\operatorname{argmin}}\; D_{\mathrm{KL}}(q_\psi(z) \| p_\theta(z|x))$$

Variational inference (VI) reduces posterior inference to optimization: rather than sampling from an intractable posterior $p_\theta(z|x)$, one finds the member $q_\psi$ of a tractable family $\mathcal{Q}$ that is closest in KL divergence. Because $\log p_\theta(x)$ is constant w.r.t. $\psi$, minimizing the KL is equivalent to maximizing the **ELBO** $\mathcal{L}(\theta,\psi|x) = \mathbb{E}_{q_\psi}[\log p_\theta(x,z) - \log q_\psi(z)]$, or equivalently minimizing the variational free energy.

### Why it matters
VI scales approximate Bayesian inference to large models and datasets — it underpins VAEs, topic models, and probabilistic programming — offering a tractable alternative to MCMC with GPU-friendly, gradient-based implementations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[variational-free-energy]] — uses: The variational free energy is the physics dual of the negative ELBO; minimizing VFE = maximizing ELBO.
- [[intractable-posterior]] — applies: VI is motivated by and designed to address the intractable posterior problem.
- [[kl-divergence]] — uses: VI minimizes forward KL divergence between the variational distribution and the true posterior.
- [[elbo]] — uses: Maximizing the ELBO is equivalent to minimizing KL(q||p) — the ELBO is the primary objective of VI.
[To be populated during integration]