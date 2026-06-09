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
id: pkis:concept:absorbing-markov-chain
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch02
tags:
- stochastic-processes
- markov-property
- absorption
- fundamental-matrix
- gamblers-ruin
- first-step-analysis
title: Absorbing Markov Chain and the Fundamental Matrix
understanding: 0
---

## Definition
An absorbing Markov chain is one analyzed via the canonical decomposition S = T \cup C_1 \cup C_2 \cup ... of the state space into a transient set T and closed recurrent classes C_i. A state j is absorbing if p_{jj}=1 (a singleton closed set). Reordering states puts the transition matrix in block form P = [[Q, R],[0, P_2]], where Q = (p_{ij}, i,j \in T) governs transitions among transient states and R = (p_{kl}, k\in T, l\in T^c) governs absorption.

Absorption probabilities u_{ik} = P_i[X_\tau = k] (probability of being absorbed at k starting from transient i) satisfy the first-step recursion u_{ij} = \sum_{k\in T} Q_{ik} u_{kj} + p_{ij}, i.e. U = QU + R, with matrix solution U = (I-Q)^{-1} R. The fundamental matrix N = (I-Q)^{-1} = \sum_{n>=0} Q^n exists whenever T is finite; its (i,j) entry is the expected number of visits to transient state j starting from i, E_i \sum_n 1_{[X_n=j]}. Expected absorption times follow as (I-Q)^{-1} 1. When S is infinite the system can have multiple solutions and U^\wedge = \sum_n Q^n R is the minimal one; uniqueness holds iff P_i[the chain stays forever in T] = 0. The gambler's ruin chain on {0,...,m} is the paradigm: with \rho = q/p, the ruin probability is u_j = (\rho^j - \rho^m)/(1 - \rho^m).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]