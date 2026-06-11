---
aliases: []
also_type: []
applies:
- gaussian-distribution
- variational-autoencoder
- multivariate-normal-model
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- information-theory
- probability
- machine-learning
id: pkis:result:kl-divergence-gaussians
instantiates:
- kl-divergence
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch06
tags:
- KL-divergence
- Gaussian
- closed-form
- variational-inference
title: KL Divergence Between Two Gaussians
understanding: 0
---

## Definition
$$D_{\mathrm{KL}}\bigl(\mathcal{N}(\mu_1,\Sigma_1)\|\mathcal{N}(\mu_2,\Sigma_2)\bigr) = \frac{1}{2}\left[\operatorname{tr}(\Sigma_2^{-1}\Sigma_1) + (\mu_2-\mu_1)^T\Sigma_2^{-1}(\mu_2-\mu_1) - d + \ln\frac{\det\Sigma_2}{\det\Sigma_1}\right]$$

In the scalar case: $D_{\mathrm{KL}}=\ln\frac{\sigma_2}{\sigma_1}+\frac{\sigma_1^2+(\mu_1-\mu_2)^2}{2\sigma_2^2}-\frac{1}{2}$.

A closed-form formula for the KL divergence between two multivariate Gaussian distributions, depending on their means, covariances, and dimension $d$.

### Why it matters
This result is used throughout Bayesian inference, variational autoencoders (where it regularises the posterior towards a standard normal prior), Gaussian process approximations, and natural gradient methods. It is one of the few cases where KL has an exact analytic form.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[multivariate-normal-model]] — applies
- [[variational-autoencoder]] — applies
- [[gaussian-distribution]] — applies
- [[kl-divergence]] — instantiates
[To be populated during integration]