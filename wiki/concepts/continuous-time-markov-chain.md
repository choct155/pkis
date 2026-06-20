---
aliases: []
also_type: []
applies:
- queueing-theory
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
date_updated: '2026-06-20'
domain:
- bayesian-stats
- statistical-learning
- systems-theory
id: pkis:concept:continuous-time-markov-chain
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch05
- resnick-stochastic-processes
- cassandras-des-intro-ch06
- cassandras-des-intro-ch07
- cassandras-des-intro-ch08
- lange-applied-probability-ch08
specializes:
- markov-chains
tags:
- stochastic-processes
- markov
- queueing
title: Continuous Time Markov Chain
understanding: 0
uses:
- generator-matrix-q-matrix
- kolmogorov-forward-backward-equations
- poisson-process
---

## Definition
A continuous-time Markov chain (CTMC) is a stochastic process {X(t), t >= 0} on a discrete state space S whose future is conditionally independent of its past given the present state, with stationary transition probabilities P_ij(s) = P[X(t+s)=j | X(t)=i] depending only on the elapsed time s.

## Construction
Resnick builds a CTMC from two ingredients: (1) an embedded discrete-time Markov chain {X_n} with transition matrix Q (where Q_ii = 0, so jumps are always to a new state), governing *which* states are visited, and (2) a supply of iid unit-mean exponential random variables {E_n} together with a holding-rate function lambda(i) > 0, governing *how long* the process stays in each state. Given the visited state X_n = i, the sojourn time is T_{n+1} - T_n = E_n / lambda(i), exponential with parameter lambda(i). The process is X(t) = sum_n X_n * 1_{[T_n, T_{n+1})}(t).

## Markov Property and Memorylessness
The Markov property of {X(t)} hinges on the forgetfulness (memoryless) property of the exponential holding times: conditioning on the past reduces to knowing the current state and the elapsed time since the last transition, but the exponential distribution makes elapsed time irrelevant, so one may pretend a transition has just occurred. This is why the holding times must be exponential.

## Explosion and Regularity
The construction defines X(t) only up to T_infinity = lim_n T_n. If T_infinity < infinity an *explosion* occurs (infinitely many jumps in finite time). The chain is *regular* if P_i[T_infinity = infinity] = 1 for all i; by Proposition 5.2.1 this holds iff sum_n 1/lambda(X_n) = infinity a.s. Sufficient conditions: lambda bounded above, or S finite. States with 0 < lambda(i) < infinity are *stable*; lambda(i)=0 gives absorbing states and lambda(i)=infinity gives instantaneous states.

## Regenerative Structure
A CTMC decomposes into iid cycles (excursions between successive visits to a fixed recurrent reference state i), making it a regenerative process to which renewal theory applies.

## Applications
Queueing models (M/M/1, M/M/s, finite-capacity queues), population growth, reliability of mechanical systems, epidemics, and material-transfer models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[poisson-process]] — uses: Uniformizable CTMCs are subordinated to a Poisson clock: X(t)=X_{N(0,t]}.
- [[queueing-theory]] — applies: Markovian queues are analyzed as CTMCs.
- [[kolmogorov-forward-backward-equations]] — uses: Global transition probabilities are obtained by solving the Kolmogorov equations.
- [[generator-matrix-q-matrix]] — uses: The generator A encodes the infinitesimal rates governing P(t).
- [[markov-chains]] — specializes: A CTMC is the continuous-time instance of a Markov chain.
[To be populated during integration]