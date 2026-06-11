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
- representation-learning
id: pkis:framework:beta-vae
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch21
tags:
- VAE
- disentanglement
- rate-distortion
- information-bottleneck
title: β-VAE
understanding: 0
---

## Definition
$$\mathcal{L}_\beta(\theta,\phi|x) = -\mathbb{E}_{q_\phi(z|x)}[\log p_\theta(x|z)] + \beta\,D_{KL}(q_\phi(z|x)\|p_\theta(z)), \quad \beta \geq 0$$

The β-VAE modifies the standard VAE by scaling the KL regulariser by $\beta$. Setting $\beta=1$ recovers the standard ELBO; $\beta<1$ reduces blurriness by storing more bits per input; $\beta>1$ encourages disentangled latent representations by compressing the code more aggressively.

### Why it matters
By sweeping $\beta$ one traces the rate–distortion curve, trading off reconstruction quality against code compressibility. Large $\beta$ is empirically linked to lower total correlation $\mathrm{TC}(z)$, promoting disentanglement. The β-VAE is also a special case of the InfoVAE objective (with $\alpha=1-\lambda$), unifying several VAE variants under one framework.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]