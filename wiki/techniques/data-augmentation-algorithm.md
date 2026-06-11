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
- bayesian-inference
id: pkis:technique:data-augmentation-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch11
tags:
- bayesian
- latent-variables
- posterior-sampling
- mcmc
- missing-data
title: Data Augmentation Algorithm
understanding: 0
---

## Definition
The data augmentation (IP) algorithm samples from the joint posterior $p(\theta, Z | X)$ by iterating two steps:
- **I-step (Imputation):** Sample $\theta^{(l)} \sim p(\theta|X)$ (current estimate), then sample $Z^{(l)} \sim p(Z|\theta^{(l)}, X)$.
- **P-step (Posterior):** Update the estimate of the posterior via
$$p(\theta|X) \simeq \frac{1}{L}\sum_{l=1}^L p(\theta|Z^{(l)}, X).$$
This exploits the tractability of the complete-data posterior $p(\theta|Z,X)$ to sidestep the intractable marginal $p(\theta|X)$.

### Why it matters
Data augmentation is the Bayesian counterpart to the EM algorithm: the I-step mirrors the E-step and the P-step mirrors the M-step, but targets the full posterior rather than the mode. It is widely used in Bayesian analysis of missing-data and mixture models and is a precursor to the Gibbs sampler for hierarchical models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]