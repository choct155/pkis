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
id: pkis:concept:birth-death-process
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch05
tags:
- stochastic-processes
- markov
- queueing
- population-dynamics
title: Birth-Death Process
understanding: 0
---

## Definition
A birth-death process is a continuous-time Markov chain on {0,1,2,...} whose embedded discrete-time chain is a simple random walk: from state i it moves only to i+1 (a birth) or i-1 (a death). It is the canonical nearest-neighbor CTMC.

## Rates
Given holding-rate parameters lambda(i) and walk probabilities p_i = P[i -> i+1], q_i = 1 - p_i, one defines the *birth rate* lambda_i = p_i lambda(i) and *death rate* mu_i = q_i lambda(i) (with mu_0 = 0). Then lambda(i) = lambda_i + mu_i and p_i = lambda_i/(lambda_i + mu_i). Equivalently, in state i imagine independent exponential clocks B(i) ~ Exp(lambda_i) (next birth) and D(i) ~ Exp(mu_i) (next death); the holding time is B(i) ^ D(i) ~ Exp(lambda_i + mu_i) and a birth occurs iff B(i) <= D(i), with probability lambda_i/(lambda_i+mu_i). For small delta, P_{i,i+1}(delta) = lambda_i delta + o(delta) and P_{i,i-1}(delta) = mu_i delta + o(delta), justifying the names.

## Special Cases
The *linear birth-death process* takes lambda_i = lambda i, mu_i = mu i. The *Yule (linear birth) process* has only births (mu_i = 0, lambda_i = lambda i); its holding time in state n is Exp(lambda n), the minimum of n iid lifetimes. The M/M/1 queue is a birth-death process with constant rates lambda_i = a (arrival), mu_i = b (service).

## Stationary Distribution
Solving eta'A = 0 (a tridiagonal generator) gives the product form

eta_n = (prod_{i=0}^{n-1} lambda_i) / (prod_{i=1}^{n} mu_i),  n >= 1,

so a stationary distribution exists iff sum_n eta_n < infinity. This is the discrete analogue of detailed balance: mu_n eta_n = lambda_{n-1} eta_{n-1}.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]