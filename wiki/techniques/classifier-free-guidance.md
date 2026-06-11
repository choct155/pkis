---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- generative-models
extends:
- classifier-guidance
id: pkis:technique:classifier-free-guidance
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch25
tags:
- conditional-generation
- text-to-image
- guidance
- diffusion
title: Classifier-Free Guidance
understanding: 0
uses:
- bayesian-inference
---

## Definition
A conditional generation technique that derives an implicit classifier from the generative model itself rather than from a separately trained discriminator:

$$\nabla_x\log\tilde p_w(x|c) = (1+w)\nabla_x\log p_\theta(x|c) - w\,\nabla_x\log p_\theta(x)$$

In practice, a **single** neural network is trained jointly on conditional inputs $c$ and on the unconditional case $c=\emptyset$ (randomly dropped during training); at test time the two score estimates are linearly combined with guidance weight $w\geq 0$.

### Why it matters
Classifier-free guidance avoids the adversarial-gradient pathologies of classifier guidance (which can ignore image structure) while still enabling strong conditioning on class labels or text prompts. Increasing $w$ trades sample diversity for individual sample fidelity. It is the dominant conditioning mechanism in large-scale text-to-image systems such as DALL-E 2, Stable Diffusion, and Imagen.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-inference]] — uses
- [[classifier-guidance]] — extends: Derives the classifier from the generative model to avoid adversarial-gradient issues
[To be populated during integration]