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
- statistics
- probabilistic-models
id: pkis:technique:expectation-maximization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch19
tags:
- latent-variables
- coordinate-ascent
- maximum-likelihood
- ELBO
- generative-models
title: Expectation Maximization (EM) Algorithm
understanding: 0
---

## Definition
$$\mathcal{L}(v, \theta, q) = \mathbb{E}_{h \sim q}[\log p(h, v)] + H(q)$$

The EM algorithm maximizes this ELBO via coordinate ascent, alternating between:
- **E-step**: Set $q(h^{(i)} | v) = p(h^{(i)} | v^{(i)}; \theta^{(0)})$ — the exact posterior under current parameters.
- **M-step**: Maximize $\sum_i \mathcal{L}(v^{(i)}, \theta, q)$ with respect to $\theta$.

Convergence is guaranteed because each step increases (or maintains) the ELBO, and the E-step restores the bound to equality.

### Why it matters
EM is the canonical algorithm for maximum likelihood learning in latent variable models, including GMMs, HMMs, and probabilistic PCA. The view of EM as coordinate ascent on $\mathcal{L}$ (Neal & Hinton, 1999) unifies it with variational inference: the E-step optimizes $q$, the M-step optimizes $\theta$. In deep learning, where closed-form M-steps are unavailable, the M-step is replaced by gradient steps, yielding stochastic gradient EM.

### Limitations
EM holds $q$ fixed at $p(h|v; \theta^{(0)})$ throughout the M-step, introducing a gap between $\mathcal{L}$ and $\log p(v)$ as $\theta$ moves away from $\theta^{(0)}$. This gap is closed when the E-step runs again at the new $\theta$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]