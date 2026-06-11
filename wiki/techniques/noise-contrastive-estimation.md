---
aliases: []
also_type: []
applies:
- neural-language-model
- word-embeddings
- language-model
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
- hierarchical-softmax
- partition-function
- score-matching
- pseudolikelihood
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- deep-learning
- NLP
extends:
- maximum-likelihood-estimation
generalizes:
- score-matching
id: pkis:technique:noise-contrastive-estimation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch12
- goodfellow-deeplearning-ch18
- murphy-pml2-advanced-ch24
tags:
- language-model
- unnormalised-model
- partition-function
- word-embedding
- contrastive
title: Noise-Contrastive Estimation (NCE)
understanding: 0
uses:
- importance-sampling
- maximum-likelihood-estimation
- logistic-regression
- kl-divergence
---

## Definition
Noise-contrastive estimation (Gutmann & Hyvärinen, 2010) trains an unnormalised model $p_\theta(x) = \tilde{p}_\theta(x)/Z$ by recasting density estimation as binary classification: given a data sample $x$ and $k$ noise samples $\tilde{x}_1,\ldots,\tilde{x}_k \sim q(x)$, the model is trained to distinguish data from noise via the logistic objective
$$\mathcal{L}_{\text{NCE}} = \mathbb{E}_{x \sim p_d}\log\sigma(s_\theta(x) - \log kq(x)) + k\,\mathbb{E}_{\tilde{x}\sim q}\log(1 - \sigma(s_\theta(\tilde{x}) - \log kq(\tilde{x}))),$$
where $s_\theta = \log\tilde{p}_\theta$. This avoids computing the partition function $Z$ during training.

### Why it matters
Provides an asymptotically consistent estimator that avoids the $O(|\mathcal{V}|)$ softmax normalisation cost; widely used to train word embeddings (word2vec negative sampling is a special case) and energy-based models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[kl-divergence]] — uses: NCE minimizes KL between the noise/data classifier and the noise/model classifier
- [[score-matching]] — generalizes: With perturbation noise distribution and appropriate parameterization, NCE recovers score matching
- [[maximum-likelihood-estimation]] — extends: NCE provides an alternative to MLE that avoids MCMC and estimates Z_θ
- [[energy-based-model]] — applies: NCE trains EBMs by binary classification between data and noise
- [[language-model]] — applies
- [[pseudolikelihood]] — contrasts-with
- [[score-matching]] — contrasts-with
- [[logistic-regression]] — uses
- [[maximum-likelihood-estimation]] — uses
- [[partition-function]] — contrasts-with
- [[word-embeddings]] — applies
- [[hierarchical-softmax]] — contrasts-with
- [[neural-language-model]] — applies
- [[importance-sampling]] — uses
[To be populated during integration]