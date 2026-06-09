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
- systems-theory
id: pkis:concept:holding-times
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- continuous-time-markov-chain
related_concepts: []
sources:
- resnick-stochastic-processes-ch05
tags:
- stochastic-processes
- exponential-distribution
- markov
title: Holding Times (Exponential Sojourn Times)
understanding: 0
uses:
- poisson-process
---

## Definition
In a continuous-time Markov chain, the holding (sojourn) time in state i is the random duration the process remains there before jumping. For a stable state it is exponentially distributed with parameter lambda(i), so the mean sojourn is 1/lambda(i); conditional on the sequence of visited states, successive holding times are independent exponentials.

## Why Exponential: the Markov Property
The exponential holding time is forced by the Markov property. Only the exponential distribution is *memoryless*: P[E > t+s | E > s] = P[E > t]. This forgetfulness means that conditioning on elapsed time in a state gives no information about the residual time, so the process can 'forget' its history and remain Markov.

## Key Exponential Facts (Resnick Prop. 5.1.1)
For independent E(a), E(b):
- Minimum: E(a) ^ E(b) ~ Exp(a+b). The first of several competing exponential clocks fires at the summed rate.
- Competition: P[E(a) > E(b)] = b/(a+b). The probability a given clock fires first is proportional to its rate.
- Summability: for independent E_n ~ Exp(lambda(n)), sum_n E_n < infinity a.s. iff sum_n 1/lambda(n) < infinity. This dichotomy is the engine behind the explosion/regularity criterion for CTMCs.

## Role
Holding times are the timing layer of the CTMC construction: the embedded discrete chain decides *where* to go, the exponential holding times decide *when*. Their rates lambda(i) sit on the diagonal of the generator matrix.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[poisson-process]] — uses: Constant-rate exponential holding times generate the jump epochs of a Poisson process (uniformization).
- [[continuous-time-markov-chain]] — prerequisite-of: Exponential holding times and their memorylessness underlie the CTMC construction and Markov property.
[To be populated during integration]