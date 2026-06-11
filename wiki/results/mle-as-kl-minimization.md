---
aliases: []
also_type: []
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
- statistics
- information-theory
- machine-learning
extends:
- maximum-likelihood-estimation
id: pkis:result:mle-as-kl-minimization
instantiates:
- empirical-risk-minimization
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch05
tags:
- MLE
- KL-divergence
- cross-entropy
- empirical-distribution
- log-likelihood
title: MLE as KL-Divergence Minimization
understanding: 0
uses:
- kl-divergence
- cross-entropy-loss
- data-generating-distribution
- entropy
---

## Definition
Maximizing the log-likelihood over an i.i.d. sample is equivalent to minimizing the KL divergence from the empirical distribution $\hat{p}_{\text{data}}$ to the model distribution $p_{\text{model}}(\cdot;\boldsymbol{\theta})$:

$$\boldsymbol{\theta}_{\text{ML}} = \arg\max_{\boldsymbol{\theta}}\mathbb{E}_{x\sim\hat{p}_{\text{data}}}\log p_{\text{model}}(x;\boldsymbol{\theta}) = \arg\min_{\boldsymbol{\theta}} D_{\text{KL}}(\hat{p}_{\text{data}}\|p_{\text{model}}).$$

Minimizing $D_{\text{KL}}$ is equivalent to minimizing cross-entropy $H(\hat{p}_{\text{data}}, p_{\text{model}})$ since the entropy of $\hat{p}_{\text{data}}$ is constant with respect to $\boldsymbol{\theta}$.

### Why it matters
This equivalence unifies MLE with information-theoretic objectives and reveals that MSE loss corresponds to Gaussian likelihood, cross-entropy loss to categorical likelihood, etc. It frames all negative-log-likelihood training as an attempt to match the model distribution to the empirical data distribution.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[empirical-risk-minimization]] — instantiates
- [[entropy]] — uses
- [[data-generating-distribution]] — uses
- [[cross-entropy-loss]] — uses
- [[kl-divergence]] — uses
- [[maximum-likelihood-estimation]] — extends
[To be populated during integration]