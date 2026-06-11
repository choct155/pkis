---
aliases: []
also_type: []
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
id: pkis:concept:frechet-inception-distance
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
- Frechet-distance
- image-quality
- FID
title: Fréchet Inception Distance
understanding: 0
---

## Definition
The **Fréchet Inception Distance (FID)** measures the dissimilarity between the distribution of real data features $\Phi_\text{data}$ and model-generated features $\Phi_\text{model}$, both extracted by a pretrained Inception network. Fitting Gaussians to each set of features with means $\mu_d, \mu_m$ and covariances $\Sigma_d, \Sigma_m$, the FID is
$$\text{FID} = \|\mu_m - \mu_d\|_2^2 + \operatorname{tr}\!\Bigl(\Sigma_d + \Sigma_m - 2(\Sigma_d\Sigma_m)^{1/2}\Bigr).$$

This is the squared Fréchet (Wasserstein-2) distance between two Gaussians. **Lower FID is better**.

### Why it matters
FID remains the dominant evaluation metric in image generation research. Unlike IS, it directly compares generated to real samples in feature space, capturing both quality and diversity. Its main weaknesses are high estimation bias at small sample sizes (motivating Kernel Inception Distance) and sensitivity to the pretrained classifier's domain.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]