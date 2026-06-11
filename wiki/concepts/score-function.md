---
aliases: []
also_type: []
analogous-to:
- kl-divergence
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
- information-theory
- generative-models
id: pkis:concept:score-function
instantiates:
- fisher-information
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch14
- murphy-pml2-advanced-ch03
tags:
- score-matching
- gradient-log-density
- unnormalised-model
- diffusion-models
title: Score Function of a Distribution
understanding: 0
uses:
- fisher-information
- entropy
- maximum-likelihood-estimation
- exponential-family
- gradient-and-jacobian
- hessian-matrix
---

## Definition
The score function (or score) of a probability distribution $p(x)$ is the gradient of its log-density with respect to the data:
$$s(x) = \nabla_x \log p(x)$$
The score is a vector field pointing in the direction of increasing log-probability and is independent of the normalisation constant.

### Why it matters
Because the score does not require computing or differentiating the partition function $Z$, it enables tractable estimation for unnormalised models. **Score matching** (Hyvärinen, 2005) fits a model by minimising $\mathbb{E}[\|\nabla_x \log p_\theta(x) - \nabla_x \log p_{\text{data}}(x)\|^2]$, avoiding maximum likelihood's intractable normalisation. The score is also the key quantity estimated by denoising autoencoders and, via Stein's identity, underpins modern diffusion and score-based generative models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hessian-matrix]] — uses
- [[gradient-and-jacobian]] — uses
- [[exponential-family]] — uses
- [[maximum-likelihood-estimation]] — uses
- [[fisher-information]] — instantiates: Fisher information is the covariance of the score
- [[entropy]] — uses
- [[fisher-information]] — uses: Fisher information is the variance of the score under the model
- [[kl-divergence]] — analogous-to: Minimising KL and matching scores are related ways to fit distributions; score is gradient of log-density
[To be populated during integration]