---
aliases: []
also_type: []
applies:
- mcmc
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:concept:effective-sample-size
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch11
tags:
- mcmc
- autocorrelation
- effective-sample-size
- n-eff
- simulation-efficiency
- variogram
- gelman
title: Effective Sample Size (MCMC)
understanding: 0
uses:
- monte-carlo-estimator
---

## Definition
Effective sample size n_eff quantifies how many *independent* draws a correlated MCMC sample is worth for estimating a posterior expectation. MCMC draws within a sequence are autocorrelated, so although m chains of length n give mn total draws, the variance of the estimator ψ̄_.. of E(ψ|y) behaves as if computed from fewer independent samples — the 'patchy' look of an MCMC scatterplot relative to the same number of i.i.d. draws makes this concrete.

The definition rests on the asymptotic variance of the average of a stationary correlated sequence:

  lim_{n→∞} mn · var(ψ̄_..) = (1 + 2 Σ_{t=1}^∞ ρ_t) var(ψ|y),   (11.5)

where ρ_t is the lag-t autocorrelation. Since independent draws would give var(ψ̄_..) = var(ψ|y)/(mn), the inflation factor (1 + 2Σρ_t) defines

  n_eff = mn / (1 + 2 Σ_{t=1}^∞ ρ_t).   (11.6)

Estimation (BDA3): use var̂⁺ from (11.3) as the total-variance estimate; form the variogram at each lag,

  V_t = 1/[m(n-t)] Σ_j Σ_{i=t+1}^n (ψ_{i,j} − ψ_{i-t,j})²,

then invert E(ψ_i − ψ_{i-t})² = 2(1−ρ_t)var(ψ) to get ρ̂_t = 1 − V_t/(2 var̂⁺)   (11.7). The summed autocorrelations cannot be summed to large lag (sample correlations get too noisy); instead use the Geyer initial-positive-sequence rule — take the partial sum up to the first odd T for which ρ̂_{T+1} + ρ̂_{T+2} < 0:

  n̂_eff = mn / (1 + 2 Σ_{t=1}^T ρ̂_t).   (11.8)

All computed on saved (post-warm-up) iterations only. n_eff combines with R̂ as a stopping rule: once R̂ is near 1 and n_eff exceeds a target for every estimand, collect the mn draws as a posterior sample. As few as 10 independent draws inflate the simulation standard error only by sqrt(1 + 1/10) ≈ 1.05, so Gelman's default is to run until n̂_eff ≥ 5m (i.e. ≈10 effective draws per original sequence, recalling m is twice the number of chains after splitting).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[monte-carlo-estimator]] — uses: n_eff is defined via the variance-efficiency of the Monte Carlo average as an estimate of E(ψ|y).
- [[mcmc]] — applies: n_eff measures the independent-draw worth of correlated MCMC output.
[To be populated during integration]