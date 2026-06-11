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
- probabilistic-inference
id: pkis:technique:biased-importance-sampling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch17
tags:
- importance-sampling
- self-normalised
- unnormalized-density
- monte-carlo
title: Biased Importance Sampling (Self-Normalised)
understanding: 0
---

## Definition
$$\hat{s}_{\text{BIS}} = \frac{\sum_{i=1}^n \frac{\tilde{p}(\mathbf{x}^{(i)})}{\tilde{q}(\mathbf{x}^{(i)})}f(\mathbf{x}^{(i)})}{\sum_{i=1}^n \frac{\tilde{p}(\mathbf{x}^{(i)})}{\tilde{q}(\mathbf{x}^{(i)})}}, \quad \mathbf{x}^{(i)} \sim q$$

where $\tilde{p}, \tilde{q}$ are unnormalized versions of $p$ and $q$. The estimator is asymptotically unbiased ($E[\hat{s}_{\text{BIS}}] \to s$ as $n \to \infty$) because the denominator converges to 1, but is biased for finite $n$.

This self-normalised variant of importance sampling is the practical choice when only unnormalized densities are available, as is common for energy-based and latent variable models.

### Why it matters
Many distributions of interest in deep learning (e.g., EBMs, VAE posteriors) are known only up to a normalizing constant. Biased IS enables Monte Carlo estimation in these cases without ever computing the partition function, at the cost of introducing a finite-sample bias that vanishes asymptotically.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]