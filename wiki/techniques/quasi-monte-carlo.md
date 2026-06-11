---
aliases: []
also_type: []
applies:
- bayesian-optimization
- variational-inference
- mcmc
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
- numerical-methods
- statistics
- machine-learning
extends:
- monte-carlo-integration
id: pkis:technique:quasi-monte-carlo
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch11
tags:
- low-discrepancy
- Halton
- Sobol
- variance-reduction
- numerical-integration
- RQMC
title: Quasi-Monte Carlo (QMC)
understanding: 0
---

## Definition
Replaces i.i.d. random samples in Monte Carlo integration with **low-discrepancy sequences** (e.g., Halton or Sobol sequences) that fill space more uniformly:
$$\hat{f}_N = \frac{1}{N}\sum_{n=1}^N f(x_n), \quad \epsilon_N = O\!\left(\frac{(\log N)^D}{N}\right) \text{ vs. } O\!\left(\frac{1}{\sqrt{N}}\right) \text{ for MC}$$

For $N>2^D$, QMC error is smaller than standard MC error.

### Why it matters
QMC achieves nearly $O(1/N)$ convergence for smooth integrands, dramatically outperforming i.i.d. MC. Randomized QMC (RQMC) adds a uniform random shift $\mathbf{y}_{i,r}=\mathbf{x}_i+\mathbf{u}_r\pmod{1}$ to restore unbiasedness and enable variance estimation while retaining the low-discrepancy structure. Used in Bayesian optimization initialization, MCMC, and variational inference.

### Limitation
Deterministic QMC provides no built-in uncertainty estimate; RQMC resolves this by repeating with $R$ independent random shifts.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mcmc]] — applies
- [[variational-inference]] — applies
- [[bayesian-optimization]] — applies
- [[monte-carlo-integration]] — extends
[To be populated during integration]