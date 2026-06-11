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
id: pkis:concept:diffusion-noise-schedule
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch25
tags:
- diffusion
- hyperparameter
- signal-to-noise-ratio
- VDM
title: Diffusion Noise Schedule
understanding: 0
---

## Definition
$$\beta_1 < \beta_2 < \cdots < \beta_T, \qquad \bar\alpha_t = \prod_{s=1}^t (1-\beta_s) \xrightarrow{t\to T} 0$$

The sequence $\{\beta_t\}$ (or equivalently the signal-to-noise ratio $R(t)=\alpha_t^2/\sigma_t^2$ in continuous time) that controls how quickly structured data is corrupted to noise in the forward diffusion process; common choices include **linear**, **cosine** ($\alpha_t=\cos\!\left(\frac{t/T+s}{1+s}\frac{\pi}{2}\right)$), and learned **monotonic neural-network** schedules (VDM).

### Why it matters
The noise schedule directly governs the trade-off between low-frequency (semantic) and high-frequency (texture) content removal, affects ELBO tightness and sample quality, and determines the SNR range over which the denoising network must operate. Optimising it (as in the Variational Diffusion Model) can significantly improve likelihood scores without changing the network architecture.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]