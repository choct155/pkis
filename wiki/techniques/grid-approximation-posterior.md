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
- bayesian-inference
- computational-statistics
id: pkis:technique:grid-approximation-posterior
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch07
tags:
- grid
- approximate-inference
- normalization
- posterior-approximation
title: Grid Approximation (Posterior)
understanding: 0
---

## Definition
$$p(\theta \in r_k | D) \approx p_k\Delta, \quad p_k = \frac{\tilde{p}_k}{\sum_{k'}\tilde{p}_{k'}}, \quad \tilde{p}_k = p(D|\theta_k)p(\theta_k)$$

The parameter space is partitioned into K equally-spaced cells of volume $\Delta$; the unnormalised density is evaluated at each grid point $\theta_k$ and then renormalised to give a discrete approximation to the posterior.

### Why it matters
Grid approximation is conceptually transparent and gives an exact numerical answer in 1–2 dimensions, making it ideal for teaching Bayesian updating (e.g., beta-Bernoulli). Its fatal flaw is the curse of dimensionality: the number of evaluations grows as $K^D$, rendering it impractical beyond a few dimensions. It is therefore primarily used as a pedagogical baseline against which all other approximate methods are measured.

### Limitations
Beyond ~3 parameters, grid approximation is replaced by MCMC, VI, or Laplace methods. It also requires knowing the prior on a bounded support or truncating the grid.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]