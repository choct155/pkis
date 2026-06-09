---
aliases: []
also_type: []
applies:
- bayesian-model-averaging
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
extends:
- metropolis-algorithm
id: pkis:technique:reversible-jump-mcmc
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch12
specializes:
- mcmc
tags:
- mcmc
- trans-dimensional
- model-averaging
- metropolis-hastings
- dimension-matching
- model-selection
- mixture-models
title: Reversible Jump MCMC
understanding: 0
uses:
- mixture-models
---

## Definition
Reversible jump MCMC (Green 1995) is a Metropolis-Hastings method for trans-dimensional simulation, in which the dimension of the parameter space can change from one iteration to the next. It is used when a single Markov chain must move among models with different numbers of parameters — e.g. Bayesian model averaging over regression models with different predictor sets, or finite mixture models with an unknown number of components. The chain's state includes both the ordinary parameters and an indicator of the current model, so the sampler yields posterior model probabilities alongside within-model parameter inference.

## Dimension Matching
The key device is the introduction of auxiliary random variables to match dimensions across models. To propose a move from model k (parameters ω_k, dimension d_k) to model k*, one draws an auxiliary variable u from a proposal J(u | k, k*, ω_k) and applies a one-to-one deterministic map (ω_{k*}, u*) = g_{k,k*}(ω_k, u) with d_k + dim(u) = d_{k*} + dim(u*). This dimension-matching is what preserves the balance condition needed to prove convergence of the underlying Metropolis-Hastings algorithm in the enlarged space.

## Acceptance Ratio
A proposed model is accepted with probability min(r, 1), where r multiplies the usual likelihood×prior×model-prior ratio by the proposal ratio J_{k*,k}J(u*|...)/(J_{k,k*}J(u|...)) and by the Jacobian |∇g_{k,k*}(ω_k, u)| of the dimension-matching transformation. The Jacobian term is the distinctive trans-dimensional ingredient; in special cases (e.g. simply setting τ² = u with no rescaling) the Jacobian is 1 and priors that are common to both models cancel.

## Use and Caveats
A canonical illustration is testing whether a variance component τ is needed in a hierarchical (e.g. probit/logistic) regression by letting the chain jump between the model with τ = 0 and the model with τ > 0. Gelman et al. note that they generally prefer fitting the full model and examining the posterior of τ rather than treating τ = 0 as a discrete possibility, but reversible jump is the right tool when discrete model uncertainty must be sampled directly.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mixture-models]] — uses: a canonical use is finite mixture models with an unknown, varying number of components
- [[bayesian-model-averaging]] — applies: RJMCMC samples across candidate models, yielding posterior model probabilities for model averaging
- [[mcmc]] — specializes: RJMCMC is a trans-dimensional MCMC sampler
- [[metropolis-algorithm]] — extends: RJMCMC generalizes Metropolis-Hastings to moves between spaces of differing dimension via dimension-matching
[To be populated during integration]