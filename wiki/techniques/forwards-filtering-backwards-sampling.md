---
aliases: []
also_type: []
applies:
- hidden-markov-model
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- particle-filter
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probabilistic-graphical-models
- machine-learning
- Bayesian-statistics
extends:
- forwards-backwards-algorithm
id: pkis:technique:forwards-filtering-backwards-sampling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch09
tags:
- posterior-sampling
- HMM
- MCMC
- state-space-models
- smoothing
title: Forwards Filtering Backwards Sampling (FFBS)
understanding: 0
uses:
- mcmc
---

## Definition
$$p(z_{1:T} \mid y_{1:T}) = p(z_T \mid y_{1:T}) \prod_{t=T-1}^{1} p(z_t \mid z_{t+1}, y_{1:T})$$

where the backward conditional factorises as
$$p(z_t \mid z_{t+1}, y_{1:T}) \propto A(z_t, z_{t+1})\,\alpha_t(z_t).$$

The algorithm runs the standard forwards (filtering) pass to store $\alpha_t$, then samples $z^s_T \sim \alpha_T$ and iterates backward, drawing $z^s_t \sim p(z_t \mid z^s_{t+1}, y_{1:T})$.

Intuition: exact ancestral sampling from the HMM posterior by exploiting the Markov structure in the backward direction.

### Why it matters
FFBS produces exact i.i.d. samples from the joint posterior $p(z_{1:T}\mid y_{1:T})$ in $O(K^2 T)$ time. It is the standard method for the "simulation smoother" in state-space model MCMC (e.g., the Gibbs sampler for Bayesian HMMs and switching state-space models). Sampling is preferable to MAP when there are multiple posterior modes or when downstream inference requires full posterior uncertainty.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[particle-filter]] — contrasts-with
- [[mcmc]] — uses: used as simulation smoother in Gibbs sampler for Bayesian HMMs
- [[hidden-markov-model]] — applies
- [[forwards-backwards-algorithm]] — extends: replaces backward marginal computation with backward sampling
[To be populated during integration]