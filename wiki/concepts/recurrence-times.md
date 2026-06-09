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
id: pkis:concept:recurrence-times
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch03
tags:
- renewal-theory
- stochastic-processes
- length-biasing
- inspection-paradox
title: Recurrence Times (Age and Excess Life)
understanding: 0
---

## Definition
For a renewal process observed at time t, the *forward recurrence time* (excess / residual life) B(t) = S_{N(t)} - t is the time until the next renewal, and the *backward recurrence time* (age) A(t) = t - S_{N(t)-1} is the time since the last renewal. Their sample paths are sawtooth: B decreases at slope -1 between upward jumps, A increases at slope +1. Both distributions are obtained by deriving a renewal equation (conditioning on the first renewal Y_1, so the process 'starts from scratch') and solving: P[A(t)<=x] = U*((1-F)1_{[0,x]})(t) and P[B(t)>x] = U*(1-F(.+x))(t) = integral_0^t (1-F(x+t-y)) U(dy). Applying the key renewal theorem gives a common limiting (equilibrium) law for both, F_0(x) = mu^{-1} integral_0^x (1-F(s)) ds. This equilibrium distribution is *length-biased* — it weights interarrival intervals by their length — which is the formal content of the inspection (waiting-time) paradox: an observer arriving at a random time lands in a longer-than-typical interval. For the Poisson process the memorylessness of the exponential makes B(t) exponential for every t (and A(t) truncated exponential), one expression of Poisson stationarity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]