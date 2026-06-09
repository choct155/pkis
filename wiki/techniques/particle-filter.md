---
aliases: []
also_type: []
applies:
- dynamic-bayesian-network
contrasts-with:
- variational-inference
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-07'
domain:
- bayesian-stats
- state-space-models
- time-series
id: pkis:technique:particle-filter
knowledge_type: technique
maturity: settled
related_concepts: []
sources:
- '[[binsbergen-term-structure-dsge-2011]]'
specializes:
- filtering-prediction-smoothing
tags:
- sequential-monte-carlo
- smc
- importance-resampling
- nonlinear-filtering
- particle-filter
- likelihood-evaluation
- hidden-markov-models
- dsge
- dynamic-bayesian-networks
title: Particle Filter (Sequential Monte Carlo)
understanding: 0
uses:
- importance-resampling
---

A sequential Monte Carlo algorithm that approximates the filtering distribution p(states_t | data_{1:t}) of a nonlinear, non-Gaussian state-space model by propagating a weighted empirical distribution of particles (state draws) through time using sequential importance resampling (SIR); at each step, particles are propagated through the state transition, reweighted by the likelihood of the new observation, and resampled to prevent weight degeneracy — producing a consistent Monte Carlo estimator of the likelihood function even when the Kalman filter is inapplicable due to model nonlinearity.

## Reading Path
- [[binsbergen-term-structure-dsge-2011]] (unread) — uses the particle filter to evaluate the likelihood of a nonlinear DSGE state-space representation (third-order perturbation solution); the Kalman filter is inapplicable because the solution is nonlinear; the particle-filter likelihood is then maximized via CMA-ES to estimate structural parameters

## Distinction from Beam Search
Unlike beam search, which keeps a fixed-size set of deterministic top-k hypotheses with uniform implicit weight, a particle filter maintains a genuine distribution over hypotheses and resamples stochastically. This preserves the entropy of the approximate posterior rather than collapsing it to a constant.

Beam search: keep top-k paths by point score → implicit uniform weight over k paths → entropy term collapses to constant log k → only fit objective is active.

Particle filter: keep k weighted paths → genuine probability distribution over paths → entropy is real and computable → both fit and entropy objectives remain active.

This distinction is load-bearing for the variational-graph-traversal hypothesis: a particle filter approximation to the path distribution preserves the ELBO entropy signal that beam search discards.

## Relationship to MCMC
Particle filters are to sequential inference what MCMC is to static inference. MCMC constructs a chain whose stationary distribution is the posterior over fixed parameters. Particle filters construct a weighted population whose empirical distribution approximates the sequential posterior at each time step as new observations arrive. Both are asymptotically exact given sufficient particles or chain length.

## Connections
- [[importance-resampling]] — uses: Particle filtering is sequential importance sampling with resampling to combat weight degeneracy.
- [[filtering-prediction-smoothing]] — specializes: Particle filtering approximates the filtering task by a resampled weighted sample population.
- [[dynamic-bayesian-network]] — applies: Particle filtering is the workhorse approximate-inference method for general (nonlinear, non-Gaussian, factored) DBNs.
- [[variational-inference]] — contrasts-with: Particle filter is sampling-based sequential inference; VI is optimization-based approximation