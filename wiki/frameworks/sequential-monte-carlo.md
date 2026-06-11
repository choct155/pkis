---
aliases: []
also_type: []
applies:
- state-space-models
- markov-decision-processes
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
contrasts-with:
- mcmc
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- bayesian-computation
- sequential-inference
- monte-carlo-methods
generalizes:
- particle-filter
- smc-sampler
id: pkis:framework:sequential-monte-carlo
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch07
- murphy-pml2-advanced-ch13
tags:
- SMC
- particle-filter
- sequential-inference
- importance-weights
- resampling
title: Sequential Monte Carlo (SMC)
understanding: 0
uses:
- importance-sampling
- marginal-likelihood
- bayesian-model-comparison
- filtering-prediction-smoothing
---

## Definition
$$\{\theta_t^{(s)}, w_t^{(s)}\}_{s=1}^S \approx p(\theta|D_{1:t}), \quad w_t^{(s)} \propto \frac{p(D_{1:t}|\theta_t^{(s)})p(\theta_t^{(s)})}{q(\theta_t^{(s)}|D_{1:t})}$$

SMC maintains a weighted particle population that is propagated, reweighted, and resampled as the target distribution evolves from a simple prior toward the full posterior, bridging successive distributions via importance weights.

### Why it matters
Unlike MCMC's local Markov moves, SMC performs inference via a sequence of intermediate distributions, making it more robust to multimodality and naturally suited to streaming/online data. Particle filtering is its specialisation to state-space models. SMC also yields an unbiased estimate of the marginal likelihood $p(D)$, which is valuable for model comparison. Recent "SMC samplers" apply it to static models as an alternative to MCMC.

### Relationship to particle filtering
Particle filtering applies SMC to the temporal filtering problem $p(\theta_t|D_{1:t})$, where observations arrive sequentially and the target distribution changes at each step.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[smc-sampler]] — generalizes
- [[markov-decision-processes]] — applies: SMC applied to SSM filtering, a special case of planning/inference in sequential models
- [[filtering-prediction-smoothing]] — uses
- [[bayesian-model-comparison]] — uses
- [[state-space-models]] — applies
- [[marginal-likelihood]] — uses: SMC yields an unbiased estimate of p(D)
- [[importance-sampling]] — uses
- [[particle-filter]] — generalizes
- [[mcmc]] — contrasts-with
[To be populated during integration]