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
- ddpm
id: pkis:technique:classifier-guidance
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch25
tags:
- conditional-generation
- diffusion
- guidance
- classifier
title: Classifier Guidance
understanding: 0
uses:
- bayesian-inference
---

## Definition
A conditional sampling technique for diffusion models that steers the reverse diffusion process using the gradient of a **pre-trained discriminative classifier** $p_\phi(c|x_t)$:

$$\nabla_x\log p_w(x|c) = \nabla_x\log p(x) + w\,\nabla_x\log p_\phi(c|x)$$

In practice, the reverse step becomes:
$$x_{t-1}\sim\mathcal{N}(\mu_\theta(x_t,t)+w\,\Sigma_\theta(x_t,t)\nabla_{x_t}\log p_\phi(c|x_t),\; \Sigma_\theta(x_t,t))$$

where $w>1$ amplifies the conditioning signal.

### Why it matters
Classifier guidance enables conditional generation from an **unconditionally trained** diffusion model using any off-the-shelf classifier, without retraining the generator. It motivated the development of classifier-free guidance, which avoids the adversarial-gradient failure modes of discriminative classifiers applied to intermediate noisy images.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[ddpm]] — extends
- [[bayesian-inference]] — uses: Uses Bayes' rule to decompose the conditional score into unconditional score plus classifier gradient
[To be populated during integration]