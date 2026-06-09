---
aliases: []
also_type: []
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
- statistical-learning
id: pkis:concept:stationary-renewal-process
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch03
tags:
- renewal-theory
- stochastic-processes
- stationarity
- equilibrium-distribution
title: Stationary Renewal Process
understanding: 0
---

## Definition
A stationary (equilibrium) renewal process is a delayed renewal process whose delay (first interarrival) distribution is chosen to be the equilibrium distribution F_0(x) = mu^{-1} integral_0^x (1-F(s)) ds, with {Y_n, n>=1} i.i.d. with distribution F of finite mean mu. The defining characterization is that the delayed renewal function is exactly linear, V(t) = t/mu for all t > 0, if and only if the delay distribution G equals F_0 (proved via Laplace transforms: V-hat(lambda) = F_0-hat(lambda)/(1-F-hat(lambda)) = 1/(lambda mu)). With this delay the process has a constant renewal rate and is genuinely time-stationary — the forward recurrence time has distribution F_0 for every t — justifying the adjective. The Poisson process is the special case in which F_0 = F (the exponential is its own equilibrium distribution), so the homogeneous Poisson process is the canonical stationary renewal process with linear renewal function EN(t) - 1 = at.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]