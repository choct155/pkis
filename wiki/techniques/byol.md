---
aliases: []
also_type: []
analogous-to:
- barlow-twins-loss
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
- self-supervised-learning
- computer-vision
id: pkis:technique:byol
instantiates:
- self-supervised-learning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch32
tags:
- non-contrastive
- momentum-encoder
- collapse-prevention
- SimSiam
- DINO
title: BYOL (Bootstrap Your Own Latents)
understanding: 0
uses:
- transfer-learning
---

## Definition
BYOL learns visual representations without negative pairs by minimising the mean-squared error between an **online network** $f_\theta$ (with predictor $g_\phi$) and a **target network** $f_{\theta'}$:

$$\mathcal{L}_{\text{BYOL}} = \mathbb{E}_{x,x^+}\left[\left\|g_\phi(f_\theta(x)) - \text{sg}(f_{\theta'}(x^+))\right\|_2^2\right]$$

where $\text{sg}(\cdot)$ denotes stop-gradient. The target network parameters are an exponential moving average of the online network: $\theta' \leftarrow m\theta' + (1-m)\theta$. Gradients flow only through the online network.

### Why it matters
BYOL demonstrated that competitive self-supervised representations can be learned without any negative examples, challenging the prevailing view that negatives are necessary to prevent representational collapse. The asymmetry between online and target networks (predictor + EMA) is essential to avoid trivial constant-output solutions.

### Variants
SimSiam uses $\theta' \leftarrow \theta$ (stop-gradient only); DINO replaces MSE with cross-entropy and adds centering.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[transfer-learning]] — uses
- [[self-supervised-learning]] — instantiates
- [[barlow-twins-loss]] — analogous-to
- [[contrastive-representation-learning]] — contrasts-with
[To be populated during integration]