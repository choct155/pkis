---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- generative-models
- evaluation
id: pkis:principle:likelihood-sample-quality-decoupling
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch20
tags:
- evaluation
- log-likelihood
- sample-quality
- generative-models
- GAN
title: Likelihood–Sample Quality Decoupling
understanding: 0
---

## Definition
**Likelihood–sample quality decoupling** is the empirical and theoretical observation that a generative model's log-likelihood on held-out data is often poorly correlated with the perceptual quality of samples it produces.

Two canonical failure modes illustrate the principle:

1. **Good likelihood, bad samples:** A mixture $q_2 = 0.01\,q_0 + 0.99\,q_1$, where $q_0$ is an excellent model and $q_1$ is white noise, barely reduces the per-sample log-likelihood when $D$ is large ($\log q_2(x) \geq \log q_0(x) - 2$, and $|\log q_0(x)| \sim D$), yet 99% of its samples are garbage.
2. **Bad likelihood, good samples:** A GMM centered on training images with tiny variance achieves near-perfect sample quality (training images look real) but catastrophically overfits, yielding poor test-set likelihood.

### Why it matters
This principle justifies the development of alternative evaluation metrics (FID, IS, precision/recall, MMD) and alternative training objectives (Wasserstein GAN, score matching, diffusion) that are better aligned with perceptual quality. It also shows that standard model selection by NLL may be misleading for high-dimensional generative tasks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]