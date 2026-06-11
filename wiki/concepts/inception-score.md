---
aliases: []
also_type: []
applies:
- generative-adversarial-network
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
- evaluation
id: pkis:concept:inception-score
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch20
tags:
- evaluation
- generative-models
- GAN
- image-quality
- diversity
title: Inception Score
understanding: 0
uses:
- kl-divergence
- entropy
---

## Definition
The **Inception Score (IS)** measures the quality and diversity of samples from a generative model $p_\theta(x)$ via
$$\text{IS} = \exp\!\Bigl(\mathbb{E}_{p_\theta(x)}\,D_{\mathrm{KL}}\bigl(p_{\mathrm{disc}}(Y|x)\,\|\,p_\theta(Y)\bigr)\Bigr),$$
where $p_{\mathrm{disc}}(y|x)$ is a pretrained classifier (typically Inception-v3) and $p_\theta(Y) = \int p_{\mathrm{disc}}(y|x)p_\theta(x)\,dx$ is the marginal label distribution.

Equivalently, $\log(\text{IS}) = H(p_\theta(Y)) - \mathbb{E}_{p_\theta(x)}[H(p_{\mathrm{disc}}(Y|x))]$: high IS requires both high marginal class entropy (diversity) and low per-sample class entropy (sharpness).

### Why it matters
IS was the first widely adopted automated metric for image generation, enabling reproducible comparisons between GANs. Its limitations — no reference to real data, insensitivity to intra-class diversity, dependence on a single classifier — motivated the development of FID and precision/recall metrics.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[generative-adversarial-network]] — applies
- [[entropy]] — uses
- [[kl-divergence]] — uses
[To be populated during integration]