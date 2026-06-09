---
aliases: []
also_type: []
applies:
- adaptive-mcmc
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- optimization
extends:
- hmc
id: pkis:technique:no-u-turn-sampler
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch12
specializes:
- mcmc
tags:
- MCMC
- HMC
- adaptive
- leapfrog
- self-tuning
- stan
- u-turn
- dual-averaging
title: No-U-Turn Sampler (NUTS)
understanding: 0
uses:
- detailed-balance
---

## Definition
The No-U-Turn Sampler (Hoffman & Gelman 2014) is an extension of Hamiltonian Monte Carlo that eliminates the need to hand-tune the number of leapfrog steps L. Instead of running a fixed number of steps, each NUTS trajectory continues until it begins to double back on itself — detected when the dot product between the momentum variable φ and the displacement (position minus the trajectory's starting position) turns negative. This U-turn criterion sends the trajectory as far as it usefully can go before it would start retracing its path, automatically adapting the trajectory length to the local geometry of the posterior.

## Why a Naive U-Turn Rule Fails
Simply stopping the leapfrog integration at the first U-turn does NOT preserve detailed balance, so the chain would not converge to the target distribution. The full NUTS algorithm restores correctness by building the trajectory in both directions — going backward and forward along the leapfrog path (recursively doubling the trajectory) and then sampling a point from the resulting balanced set of states in a way that satisfies detailed balance.

## Adapting the Remaining Tuning Parameters
NUTS removes only the step-count L. The mass matrix M and step size ε must still be set; NUTS pairs the U-turn rule with stochastic-optimization-based adaptation (dual averaging) of M and ε during a warm-up phase. Crucially, these parameters are tuned only during warm-up and then held fixed for the inference iterations — because adapting tuning parameters using information from previous iterations during the kept iterations would break detailed balance (see adaptive-mcmc). Warm-up iterations are discarded for inference.

## Role in Stan
NUTS is the default sampler in Stan (and PyMC). Stan preprocesses by transforming bounded variables to an unconstrained scale, runs NUTS with warm-up-phase adaptation of M and ε, and then computes R-hat and effective sample size on the post-warm-up draws. NUTS is what makes HMC usable as a black-box inference engine, since the most fragile manual tuning step (choosing L) is automated.

## Relation to HMC
NUTS is HMC with an adaptive, geometry-driven stopping rule for the trajectory length. It inherits HMC's gradient-based, typical-set-following dynamics and its symplectic leapfrog integrator; it changes only how far each trajectory runs and how the residual tuning parameters are set.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[adaptive-mcmc]] — applies: NUTS adapts M and epsilon by dual averaging during warm-up, the safe two-phase adaptation pattern
- [[mcmc]] — specializes: NUTS is a specific MCMC sampler
- [[detailed-balance]] — uses: the recursive forward/backward trajectory construction is designed so the U-turn stopping rule still satisfies detailed balance
- [[hmc]] — extends: NUTS is HMC with an adaptive, geometry-driven trajectory-length stopping rule replacing fixed L
[To be populated during integration]