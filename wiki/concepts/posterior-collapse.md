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
- generative-models
id: pkis:concept:posterior-collapse
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch21
tags:
- VAE
- KL-collapse
- latent-variable
- failure-mode
title: Posterior Collapse (Variational Pruning)
understanding: 0
---

## Definition
Posterior collapse (also called variational pruning or variational overpruning) occurs when a VAE learns $q_\phi(z|x) \approx p_\theta(z)$ for one or more latent dimensions, so those dimensions carry no information about the input:

$$D_{KL}(q_\phi(z_i|x)\|p_\theta(z_i)) \approx 0 \implies I_q(z_i;x) \approx 0$$

This happens when a powerful decoder can model $p_D(x)$ without using the latent code, causing the ELBO to be maximised by a degenerate solution that ignores $z$.

### Why it matters
Posterior collapse is the primary failure mode of VAEs with expressive decoders (e.g., RNNs, PixelCNNs, transformers). It prevents the model from learning useful latent representations. Mitigation strategies include KL annealing, free bits, skip-VAE, InfoVAE, and improved variational inference (aggressive encoder updates). Understanding it motivates the design of nearly all advanced VAE variants.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]