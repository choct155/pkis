---
aliases: []
also_type: []
applies:
- bayesian-inference
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- likelihood-tempering-smc
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
id: pkis:technique:data-tempering-ibis
instantiates:
- smc-sampler
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch13
tags:
- smc-sampler
- sequential-bayesian-inference
- online-learning
- marginal-likelihood
title: Data Tempering / IBIS
understanding: 0
---

## Definition
**Data tempering** builds a sequence of posterior targets by including one observation at a time:
$$\tilde{\gamma}_t(\theta) = p(\theta)\,p(y_{1:t}|\theta)$$
so the incremental weight reduces to the one-step predictive likelihood: $\alpha_t(\theta) = p(y_t|y_{1:t-1}, \theta)$.

**IBIS** (Iterated Batch Importance Sampling, Chopin 2002) is a practical implementation that triggers MCMC rejuvenation moves only when the ESS drops below a threshold, reducing total cost from $O(T^2)$ to near-linear in typical cases.

### Why it matters
Data tempering / IBIS is the online Bayesian equivalent of sequential updating: each new observation naturally refines the posterior. It provides a tractable alternative to full MCMC for sequential data streams, and yields unbiased marginal-likelihood estimates useful for model comparison.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-inference]] — applies
- [[likelihood-tempering-smc]] — contrasts-with
- [[smc-sampler]] — instantiates
[To be populated during integration]