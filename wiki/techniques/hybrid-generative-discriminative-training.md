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
- supervised-learning
- semi-supervised-learning
id: pkis:technique:hybrid-generative-discriminative-training
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch28
tags:
- generative-classifier
- discriminative-model
- semi-supervised
- mixture-model
- objective-function
title: Hybrid Generative–Discriminative Training
understanding: 0
---

## Definition
$$\mathcal{L}(\theta) = -\lambda \sum_n \log p(x_n, y_n \mid \theta) - (1-\lambda) \sum_n \log p(y_n \mid x_n, \theta), \quad \lambda \in [0,1]$$

Hybrid training interpolates between a purely generative joint-likelihood objective ($\lambda=1$) and a purely discriminative conditional-likelihood objective ($\lambda=0$) via a scalar trade-off parameter $\lambda$. Unlabelled data can also be incorporated by modifying the generative term with a second weight $\kappa$ that balances labelled and unlabelled contributions.

### Why it matters
Generative classifiers can handle missing features and enable semi-supervised learning, but pure generative training often underperforms discriminative models on classification accuracy. Hybrid training closes this gap while preserving the generative model's benefits. It is particularly effective when combined with mixture-model class conditionals (e.g., GMM or MFA per class).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]