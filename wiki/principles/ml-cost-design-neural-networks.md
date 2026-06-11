---
aliases: []
also_type: []
applies:
- deep-feedforward-network
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
- deep-learning
- statistics
id: pkis:principle:ml-cost-design-neural-networks
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch06
tags:
- cost-function
- output-unit
- maximum-likelihood
- gradient-saturation
- cross-entropy
title: Maximum-Likelihood Cost Design for Neural Networks
understanding: 0
uses:
- maximum-likelihood-estimation
- cross-entropy-loss
---

## Definition
The principle states: given a parametric model $p(\mathbf{y}\mid\mathbf{x};\theta)$ defined by a neural network, use the negative log-likelihood $$J(\theta) = -\mathbb{E}_{\mathbf{x},\mathbf{y}\sim\hat{p}_{\text{data}}}\log p_{\text{model}}(\mathbf{y}\mid\mathbf{x};\theta)$$ as the cost function. This automatically determines the cost from the choice of output distribution: Gaussian output → MSE; Bernoulli output → binary cross-entropy (sigmoid + log-loss); categorical output → cross-entropy (softmax + log-loss).

Pairing the output nonlinearity with the log-likelihood algebraically cancels the exp, preventing gradient saturation at the output layer.

### Why it matters
The log in the NLL undoes the exp present in sigmoid and softmax outputs, preserving large gradients even when the model is confidently wrong. By contrast, MSE applied to sigmoid or softmax outputs saturates and produces vanishing gradients. This principle also extends to heteroscedastic models (learning variance as a function of input) and mixture density networks, making it a unifying design rule for all output-unit/cost-function pairings.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[deep-feedforward-network]] — applies
- [[cross-entropy-loss]] — uses
- [[maximum-likelihood-estimation]] — uses
[To be populated during integration]