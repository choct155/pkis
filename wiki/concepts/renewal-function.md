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
id: pkis:concept:renewal-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch03
tags:
- renewal-theory
- stochastic-processes
- convolution
- laplace-transform
title: Renewal Function
understanding: 0
uses:
- renewal-process
---

## Definition
The renewal function is the expected number of renewals by time t, U(t) = E N(t). For a pure renewal process it equals the sum of convolution powers of the interarrival distribution, U(t) = sum_{n>=0} F^{n*}(t); for a delayed process with delay distribution G it is V(t) = G * U(t). Although U(t) is always finite (N(t) has an exponentially bounded tail and hence a finite moment generating function), it is rarely computable in closed form — exceptions include the exponential case where U(t) = 1 + at and the Gamma(2,1) case where U(t) = 3/4 + t/2 + (1/4)e^{-2t}. The renewal function is the central analytic object of the theory: it satisfies its own renewal equation U = F^{0*} + F*U, it is the convolution kernel U*z that solves general renewal equations, its Laplace transform is U-hat(lambda) = 1/(1 - F-hat(lambda)) (the discrete-time analogue U(s) = 1/(1-F(s))), and its asymptotics U(t)/t -> 1/mu (elementary renewal theorem) and U(t,t+a] -> a/mu (Blackwell) drive nearly every limit result. The differential U(dx) admits the interpretation 'probability that some renewal occurs in (x, x+dx]'.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[renewal-process]] — uses
[To be populated during integration]