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
id: pkis:concept:softmax-output-unit
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch06
tags:
- output-unit
- classification
- multinoulli
- logits
- cross-entropy
title: Softmax Output Unit
understanding: 0
---

## Definition
Given a vector of unnormalized log-probabilities (logits) $\mathbf{z} = \mathbf{W}^\top \mathbf{h} + \mathbf{b}$, the softmax function produces a valid probability distribution over $n$ classes: $$\text{softmax}(\mathbf{z})_i = \frac{\exp(z_i)}{\sum_j \exp(z_j)}.$$ The numerically stable form subtracts $\max_j z_j$ before exponentiation. The log-softmax simplifies to $z_i - \log \sum_j \exp(z_j)$, exposing a non-saturating linear term $z_i$ that ensures gradients survive during maximum-likelihood training.

Softmax is a smooth, differentiable relaxation of the argmax operation, implementing winner-take-all competition analogous to lateral inhibition.

### Why it matters
Paired with the cross-entropy loss, softmax avoids the gradient-vanishing caused by using squared error on bounded outputs. The function is invariant to adding a constant to all logits, so it is technically overparametrized; one logit can be fixed to zero (recovering the sigmoid for $n=2$). Saturated softmax (extreme logit differences) can cause training failure with non-log-likelihood losses.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]