---
aliases: []
also_type: []
analogous-to:
- autoencoder
- elbo
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
- deep-learning
- probabilistic-graphical-models
extends:
- score-matching
id: pkis:technique:denoising-score-matching
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- diffusion-processes
related_concepts: []
sources:
- goodfellow-deeplearning-ch18
- murphy-pml2-advanced-ch24
- murphy-pml2-advanced-ch25
tags:
- score-function
- denoising
- autoencoders
- diffusion-models
- energy-based-models
title: Denoising Score Matching
understanding: 0
uses:
- regularization
- stein-score-function
- gaussian-distribution
---

## Definition
**Denoising Score Matching** (DSM) fits a model to a smoothed data distribution:
$$p_{\text{smoothed}}(x) = \int p_{\text{data}}(y)\, q(x|y)\, dy,$$
where $q(x|y)$ is a corruption process (e.g., additive Gaussian noise). The score matching objective is then applied to $p_{\text{smoothed}}$ rather than $p_{\text{data}}$. This is equivalent to training a model to predict the clean data score from corrupted inputs.

### Why it matters
DSM regularizes score matching against overfitting: without smoothing, a consistent estimator with enough capacity will collapse to Dirac deltas on training points. The smoothing adds implicit regularization at the cost of asymptotic consistency. Kingma & LeCun (2010) applied DSM with Gaussian $q$. Critically, **denoising autoencoders are equivalent to DSM** (see section 14.5.1): the autoencoder reconstruction function estimates $\nabla_x \log p_{\text{smoothed}}(x)$, connecting denoising objectives to partition-function-free density estimation and to modern diffusion/score-based generative models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gaussian-distribution]] — uses: Score of Gaussian kernel is (x - x̃)/σ², giving the closed-form target
- [[elbo]] — analogous-to: Both provide tractable surrogates for intractable objectives: DSM for the Fisher divergence, ELBO for the log-likelihood
- [[diffusion-processes]] — prerequisite-of: DSM is the direct training objective for score-based diffusion generative models
- [[stein-score-function]] — uses
- [[regularization]] — uses
- [[autoencoder]] — analogous-to
- [[score-matching]] — extends
[To be populated during integration]