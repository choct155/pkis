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
- bayesian-inference
- scalable-inference
id: pkis:technique:svi
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch10
tags:
- SVI
- stochastic-optimization
- minibatch
- variational-inference
- scalable-bayes
title: Stochastic Variational Inference (SVI)
understanding: 0
---

## Definition
$$\mathcal{L}(\theta,\psi_{1:N}|\mathcal{D}) \approx \frac{N}{B}\sum_{x_n\in\mathcal{B}} \mathbb{E}_{q_{\psi_n}(z_n)}[\log p_\theta(x_n,z_n) - \log q_{\psi_n}(z_n)]$$

SVI replaces the full-data ELBO with an unbiased minibatch estimate (batch size $B \ll N$), enabling stochastic gradient optimization of the variational parameters. This makes VI tractable for large datasets, since each gradient step costs $O(B)$ rather than $O(N)$.

### Why it matters
SVI (Hoffman et al., 2013) was a key enabler of scaling VI to web-scale datasets and is the standard training loop for variational autoencoders and large probabilistic topic models. Combined with amortized inference it becomes the amortized SVI algorithm.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]