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
id: pkis:concept:recurrence-and-transience
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch02
tags:
- stochastic-processes
- markov-property
- first-passage
- generating-functions
- random-walk
title: Recurrence and Transience
understanding: 0
---

## Definition
A classification of the states of a Markov chain by how often the chain returns to them. Let f_{ij} = P_j[\tau_k(1)<\infty] denote the probability of ever hitting k starting from j (with f_{ij}^{(n)} = P_j[\tau_k(1)=n] the first-passage distribution). State i is recurrent if f_{ii}=1 (return is certain) and transient if f_{ii}<1 (positive probability of never returning). A recurrent state is positive recurrent if the mean return time m_i = E_i[\tau_i(1)] = \sum_n n f_{ii}^{(n)} < \infty, and null recurrent if the return is certain but m_i = \infty.

The central analytic criterion (Resnick Prop. 2.6.2): i is recurrent iff \sum_n p_{ii}^{(n)} = \infty, equivalently iff the expected number of visits E_i N_i is infinite; i is transient iff \sum_n p_{ii}^{(n)} < \infty. This follows from the generating-function identity P_{ii}(s) = 1/(1-F_{ii}(s)). For a transient j, the number of visits N_j is geometric and E_i N_j = f_{ij}/(1-f_{jj}) < \infty; for a recurrent j, P_j[N_j=\infty]=1, so the chain visits j infinitely often. Interpretively, recurrence is a stability property (the chain returns to the center of the state space) while transience signals escape toward the extremes (queues build without bound, random walks drift off, branching processes explode).

Classic results: the simple symmetric random walk on Z^d is recurrent for d=1,2 and transient for d>=3 (via Stirling, p_{00}^{(2n)} ~ (\pi n)^{-d/2}); a biased 1-D walk is transient by the SLLN. The success-run chain at 0 is recurrent iff \sum_i(1-p_i)=\infty.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]