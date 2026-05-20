---
title: "Particle Filter (Sequential Monte Carlo)"
knowledge_type: technique
also_type: []
domain: [bayesian-stats, state-space-models, time-series]
tags: [sequential-monte-carlo, smc, importance-resampling, nonlinear-filtering, particle-filter, likelihood-evaluation, hidden-markov-models, dsge, dynamic-bayesian-networks]
related_concepts: []
sources:
  - "[[binsbergen-term-structure-dsge-2011]]"
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

A sequential Monte Carlo algorithm that approximates the filtering distribution p(states_t | data_{1:t}) of a nonlinear, non-Gaussian state-space model by propagating a weighted empirical distribution of particles (state draws) through time using sequential importance resampling (SIR); at each step, particles are propagated through the state transition, reweighted by the likelihood of the new observation, and resampled to prevent weight degeneracy — producing a consistent Monte Carlo estimator of the likelihood function even when the Kalman filter is inapplicable due to model nonlinearity.

## Reading Path
- [[binsbergen-term-structure-dsge-2011]] (unread) — uses the particle filter to evaluate the likelihood of a nonlinear DSGE state-space representation (third-order perturbation solution); the Kalman filter is inapplicable because the solution is nonlinear; the particle-filter likelihood is then maximized via CMA-ES to estimate structural parameters
