---
aliases: []
also_type: []
analogous-to:
- masked-language-modeling
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- contrastive-representation-learning
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- computer-vision
- self-supervised-learning
extends:
- autoencoder
id: pkis:technique:masked-autoencoder
instantiates:
- self-supervised-learning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch32
tags:
- masked-prediction
- vision-transformer
- self-supervised
- pretext-task
- denoising
title: Masked Autoencoder (MAE)
understanding: 0
uses:
- transformer-attention-mechanisms
---

## Definition
A self-supervised representation learning method that randomly masks a large fraction (typically 75%) of image patches and trains an encoder–decoder system to reconstruct the pixel content of the masked patches:

$$\mathcal{L}_{\text{MAE}} = \frac{1}{|\mathcal{M}|}\sum_{p \in \mathcal{M}} \|x_p - \hat{x}_p\|_2^2$$

where $\mathcal{M}$ is the set of masked patch indices. The encoder (a Vision Transformer) operates only on the visible tokens, making training efficient; a lightweight decoder reconstructs masked patches from encoder outputs and mask tokens. The learned encoder representations are subsequently used as a pretrained backbone for downstream tasks.

### Why it matters
MAE achieves state-of-the-art ImageNet fine-tuned accuracy without labels or complex data-augmentation pipelines. By masking most of the input, it creates a non-trivial reconstruction task that forces the encoder to learn holistic image semantics rather than local texture statistics.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[contrastive-representation-learning]] — contrasts-with: MAE uses reconstruction rather than contrastive objective
- [[self-supervised-learning]] — instantiates
- [[transformer-attention-mechanisms]] — uses
- [[masked-language-modeling]] — analogous-to
- [[autoencoder]] — extends
[To be populated during integration]