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
- deep-learning
- statistics
id: pkis:concept:logit-neural-network
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch06
tags:
- output-unit
- log-probability
- numerical-stability
- sigmoid
- softmax
title: Logit (Neural Network)
understanding: 0
---

## Definition
In the context of neural network output units, a logit is the scalar or vector $z = \mathbf{w}^\top \mathbf{h} + b$ (scalar for binary, $\mathbf{z} = \mathbf{W}^\top\mathbf{h}+\mathbf{b}$ for multiclass) representing the unnormalized log-probability before the sigmoid or softmax normalization: $$\log \tilde{P}(y) = yz \quad (\text{binary case})$$ or $$z_i = \log \tilde{P}(y=i\mid\mathbf{x}) \quad (\text{multiclass case}).$$ Logits live in $\mathbb{R}$ and are converted to probabilities by exponentiation and normalization.

Operating in log-probability space enables the negative log-likelihood loss to cancel saturation from the exponential, ensuring well-behaved gradients.

### Why it matters
Numerically stable training requires computing the cross-entropy loss directly from logits rather than from probabilities $\hat{y} = \sigma(z)$, because $\log \sigma(z)$ underflows when $\sigma(z)\approx 0$. Most deep learning frameworks expose a `cross_entropy_from_logits` function for this reason. The logit parametrization is also the foundation of the softmax overparametrization analysis (fixing one logit to zero recovers the sigmoid).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]