---
aliases: []
also_type: []
analogous-to:
- contrastive-divergence
- fisher-information
applies:
- energy-based-model
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- maximum-likelihood-estimation
- partition-function
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
- generative-models
generalizes:
- denoising-score-matching
id: pkis:technique:score-matching
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch14
- goodfellow-deeplearning-ch18
- murphy-pml2-advanced-ch24
tags:
- score
- unnormalised-model
- partition-function
- denoising
- energy-based-model
title: Score Matching
understanding: 0
uses:
- score-function
- information-theory
- fisher-information
- stein-score-function
- fisher-divergence
---

## Definition
Score matching (Hyvärinen, 2005) is a parameter estimation method for unnormalised probabilistic models $p_\theta(x) = \tilde{p}_\theta(x)/Z(\theta)$ that avoids computing $Z(\theta)$ by minimising the expected squared difference of score functions:
$$J(\theta) = \frac{1}{2}\mathbb{E}_{p_{\text{data}}}\left[\left\|\nabla_x \log p_\theta(x) - \nabla_x \log p_{\text{data}}(x)\right\|^2\right]$$
Using integration by parts this simplifies to a tractable objective involving only $\nabla_x^2 \log p_\theta(x)$ and $\nabla_x \log p_\theta(x)$.

### Why it matters
Score matching is a consistent estimator for a broad class of models where MLE is intractable due to an unknown partition function. **Denoising score matching** (Kingma & LeCun, 2010) shows that DAE training with Gaussian noise implicitly performs score matching, connecting autoencoders to energy-based model training and forming the conceptual foundation for diffusion-based generative models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[fisher-divergence]] — uses: SM minimizes the Fisher divergence between data and model
- [[fisher-information]] — analogous-to: Fisher divergence uses first-order score differences; Fisher information uses the squared score of the model
- [[stein-score-function]] — uses
- [[energy-based-model]] — applies: SM trains EBMs by matching score functions, avoiding the partition function
- [[denoising-score-matching]] — generalizes
- [[contrastive-divergence]] — analogous-to
- [[fisher-information]] — uses
- [[partition-function]] — contrasts-with
- [[information-theory]] — uses
- [[maximum-likelihood-estimation]] — contrasts-with
- [[score-function]] — uses
[To be populated during integration]