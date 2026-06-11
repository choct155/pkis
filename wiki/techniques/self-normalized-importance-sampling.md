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
- statistics
- machine-learning
- Bayesian-inference
id: pkis:technique:self-normalized-importance-sampling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch11
tags:
- importance-weights
- unnormalized
- particle-approximation
- SMC
- ratio-estimator
title: Self-Normalized Importance Sampling (SNIS)
understanding: 0
---

## Definition
$$E[\varphi(x)] \approx \sum_{n=1}^{N_s} W_n\,\varphi(x_n), \quad W_n = \frac{\tilde{w}_n}{\sum_{n'}\tilde{w}_{n'}}, \quad \tilde{w}_n = \frac{\tilde{\gamma}(x_n)}{q(x_n)}, \quad x_n\sim q$$

Estimates expectations under an unnormalized target $\tilde{\gamma}(x)=Z\pi(x)$ by also approximating the normalization constant $Z\approx\frac{1}{N_s}\sum_n\tilde{w}_n$, yielding a biased but consistent estimator.

### Why it matters
Most practically useful form of importance sampling because real posteriors are known only up to a normalizing constant. Unlike direct IS, no evaluation of the normalized target is needed. The estimator is biased (ratio of two expectations) but bias $\to 0$ as $N_s\to\infty$. Also yields a particle approximation $\hat{\pi}(x)=\sum_n W_n\delta(x-x_n)$ used as the foundation for sequential Monte Carlo.

### Connections
Direct importance sampling is the special case where $\tilde{\gamma}=\pi$ (normalized), giving unbiased weights $\tilde{w}_n=\pi(x_n)/q(x_n)$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]