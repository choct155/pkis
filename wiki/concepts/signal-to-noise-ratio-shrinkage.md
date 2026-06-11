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
- statistics
- signal-processing
- machine-learning
id: pkis:concept:signal-to-noise-ratio-shrinkage
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch03
tags:
- bayesian-shrinkage
- gaussian
- bias-variance
- regularization
title: Signal-to-Noise Ratio (Bayesian Shrinkage)
understanding: 0
---

## Definition
In a scalar linear Gaussian model $y = z + \epsilon$ where $z \sim \mathcal{N}(\mu_0, \tau_0^2)$ and $\epsilon \sim \mathcal{N}(0, \sigma^2)$, the **signal-to-noise ratio** is:
$$\mathrm{SNR} \triangleq \frac{\mathbb{E}[Z^2]}{\mathbb{E}[\epsilon^2]} = \frac{\tau_0^2 + \mu_0^2}{\sigma^2}$$

It quantifies how much of the observed variance is attributable to the signal rather than measurement noise, and determines the degree of Bayesian shrinkage of the posterior mean toward the prior.

### Why it matters
When SNR is high (strong signal or tight prior), the posterior mean stays close to the data; when SNR is low, the posterior mean shrinks strongly toward the prior. The SNR therefore mediates the classical bias-variance tradeoff in a principled Bayesian way and connects directly to regularisation strength in ridge regression.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]