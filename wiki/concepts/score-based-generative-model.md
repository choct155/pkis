---
aliases: []
also_type: []
analogous-to:
- ddpm
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- energy-based-model
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- generative-models
- information-theory
id: pkis:concept:score-based-generative-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch25
tags:
- score-matching
- Langevin-dynamics
- diffusion
- generative-model
title: Score-Based Generative Model (SGM)
understanding: 0
uses:
- denoising-score-matching
- diffusion-processes
---

## Definition
A generative model that directly learns the **score function** $s_\theta(x)\approx\nabla_x\log p_D(x)$ of the data distribution (instead of the density itself), then generates samples via **Langevin dynamics** or reverse-SDE/ODE integration:

$$x_{k+1} = x_k + \frac{\delta}{2}s_\theta(x_k) + \sqrt{\delta}\,z_k, \quad z_k\sim\mathcal{N}(0,I)$$

The score network is trained with a score-matching objective; a **noise-conditional score network** $s_\theta(x,\sigma)$ is shared across multiple noise levels to handle low-density regions and multi-modal distributions.

### Why it matters
SGMs provide a principled probabilistic framing of diffusion-based generation and directly connect to continuous-time SDEs/ODEs. They explain why noise perturbation at multiple scales is necessary (disjoint supports make single-scale score matching fail), and they unify DDPM and flow-based generation under one mathematical framework.

### Equivalence to DDPM
The SGM training loss with $\lambda_t=\sigma_t^2$ weighting is algebraically identical to $L_{\text{simple}}$ in DDPM, establishing that the two families are the same model viewed from different perspectives.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[energy-based-model]] — contrasts-with: EBMs learn an energy function; SGMs directly learn its gradient (the score)
- [[diffusion-processes]] — uses
- [[ddpm]] — analogous-to: SGM with lambda_t=sigma_t^2 recovers L_simple, establishing formal equivalence
- [[denoising-score-matching]] — uses
[To be populated during integration]