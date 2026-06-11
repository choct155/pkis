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
- machine-learning
- deep-learning
- optimization
- regularization
id: pkis:result:early-stopping-l2-equivalence
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch07
tags:
- early-stopping
- L2-regularization
- weight-decay
- equivalence
- quadratic-approximation
title: Early Stopping Equivalence to L2 Regularization
understanding: 0
---

## Definition
$$\mathbf{Q}^\top \mathbf{w}^{(\tau)} = [\mathbf{I} - (\mathbf{I} - \epsilon\boldsymbol{\Lambda})^\tau]\mathbf{Q}^\top \mathbf{w}^*$$

For a quadratic loss and gradient descent initialized at $\mathbf{w}^{(0)}=\mathbf{0}$, after $\tau$ steps with learning rate $\epsilon$, the trajectory matches the $L^2$-regularized optimum $\tilde{\mathbf{w}} = (\mathbf{H}+\alpha\mathbf{I})^{-1}\mathbf{H}\mathbf{w}^*$ when $(\mathbf{I}-\epsilon\boldsymbol{\Lambda})^\tau = (\boldsymbol{\Lambda}+\alpha\mathbf{I})^{-1}\alpha$. Under the small-eigenvalue approximation this gives $\tau \approx \frac{1}{\epsilon\alpha}$, so the number of training steps plays the role of the inverse weight-decay coefficient.

Early stopping implicitly regularizes by constraining the parameter trajectory to a ball around initialization, equivalent to $L^2$ regularization in the quadratic case.

### Why it matters
This result justifies early stopping as a principled regularizer with automatic hyperparameter selection: the optimal stopping step $\tau$ determined from a validation set corresponds to choosing the best $\alpha$ for weight decay, without a separate hyperparameter sweep.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]