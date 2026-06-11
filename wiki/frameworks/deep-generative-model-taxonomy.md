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
- generative-models
id: pkis:framework:deep-generative-model-taxonomy
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch20
tags:
- generative-models
- taxonomy
- DGM
- VAE
- GAN
- normalizing-flows
- diffusion
- EBM
- autoregressive
title: Deep Generative Model Taxonomy
understanding: 0
---

## Definition
A classification of deep generative models (DGMs) along five axes:

| Axis | Questions |
|------|-----------|
| **Density** | Is $p(x)$ tractable? Exact, lower-bound, approximate, or unavailable? |
| **Sampling** | Is $x \sim p(x)$ fast or slow, exact or approximate? |
| **Training** | MLE, MLE lower-bound (MLE-LB), MLE-approximate (MLE-A), or min-max? |
| **Latents** | None; same-size $z \in \mathbb{R}^D$; or compressed $z \in \mathbb{R}^L$, $L \ll D$? |
| **Architecture** | Are there structural constraints (e.g., invertibility for flows)? |

The six canonical DGM families — VAE, ARM, Normalizing Flows, EBM, Diffusion, GAN — each occupy a distinct region of this taxonomy.

The framework distills the engineering trade-offs: GANs give fast sampling but no density; flows give exact density but slow sampling; VAEs give fast sampling but only a likelihood lower bound.

### Why it matters
Provides a principled language for comparing generative architectures and guides architecture choice given downstream requirements (density evaluation, sampling speed, controllable generation, etc.).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]