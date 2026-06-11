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
- deep-learning
- computer-vision
- generative-models
- multimodal-learning
id: pkis:framework:dall-e
instantiates:
- autoregressive-model-arm
- foundation-model
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch22
tags:
- DALL-E
- text-to-image
- multimodal
- autoregressive
- discrete-VAE
- CLIP
- reranking
title: DALL-E (Autoregressive Text-to-Image Generation)
understanding: 0
uses:
- gpt-pretraining
- variational-autoencoder
---

## Definition
DALL-E generates images from text prompts by combining a discrete VAE image tokeniser with a large autoregressive transformer:
1. **Tokenisation**: encode image $x$ into discrete token sequence $z$ via a dVAE (Section 21.6.5).
2. **Joint modelling**: fit a transformer to $p(z, y)$ where $y$ is the text token sequence, concatenated with $z$.
3. **Conditional generation**: sample $z \sim p(z \mid y)$, decode $x \sim p(x \mid z)$.
4. **Reranking**: score $N$ candidates with a contrastive CLIP model and return the best.

### Why it matters
DALL-E demonstrated that the autoregressive framework, when scaled to 12B parameters and 250M image-text pairs, achieves open-domain text-to-image generation of remarkable quality and compositional creativity. The CLIP-based reranking step showed that discriminative models can guide generative sampling.

### Limitations
Variable binding (e.g., assigning attributes to the correct noun) remains imperfect; output quality is sensitive to prompt phrasing.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[foundation-model]] — instantiates
- [[autoregressive-model-arm]] — instantiates
- [[variational-autoencoder]] — uses: DALL-E uses a discrete VAE to tokenise images
- [[gpt-pretraining]] — uses: DALL-E uses a GPT-style autoregressive transformer over image+text tokens
[To be populated during integration]