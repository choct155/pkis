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
- deep-learning
- optimization
- sequence-modeling
id: pkis:concept:vanishing-exploding-gradients-rnn
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch10
tags:
- gradient
- RNN
- eigenvalue
- spectral-radius
- long-term-dependencies
title: Vanishing and Exploding Gradients in RNNs
understanding: 0
---

## Definition
In a recurrent network with hidden-to-hidden weight matrix $W$, gradients propagated backward over $t$ steps scale as $(W^\top)^t$. Using the eigendecomposition $W = Q\Lambda Q^\top$:
$$h^{(t)} = Q\Lambda^t Q^\top h^{(0)},$$
eigenvalues $|\lambda_i| < 1$ cause exponential decay (**vanishing**) while $|\lambda_i| > 1$ cause exponential growth (**exploding**). Consequently, learning signals from distant time steps are either drowned out or destabilize optimization.

### Why it matters
This fundamental obstacle to training RNNs was independently identified by Hochreiter (1991) and Bengio et al. (1993, 1994). It motivates nearly every architectural and algorithmic innovation in sequence modeling: gradient clipping (exploding), LSTM/GRU cell-state highways (vanishing), echo state network spectral radius tuning, leaky units, skip connections, and the residual / highway connections used in Transformers.

### Asymmetry
Robustness to small perturbations (long-term memory storage) *requires* the network to be in a contractive regime ($|\lambda| < 1$), so vanishing gradients are in some sense unavoidable for stable RNNs — the signal about long-term dependencies is necessarily exponentially smaller than short-term signals.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]