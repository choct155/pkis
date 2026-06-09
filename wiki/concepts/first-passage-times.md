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
id: pkis:concept:first-passage-times
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch02
tags:
- stochastic-processes
- markov-property
- hitting-time
- first-step-analysis
- generating-functions
title: First-Passage and Hitting Times
understanding: 0
---

## Definition
For a Markov chain and a target set B (or single state j), the hitting time is \tau_B = inf{n>=0 : X_n \in B}; the first-passage / first-return time to a state i is \tau_i(1) = inf{m>=1 : X_m=i}. The first-passage distribution is f_{jk}^{(n)} = P_j[\tau_k(1)=n] with total mass f_{jk} = \sum_n f_{jk}^{(n)} = P_j[\tau_k(1)<\infty], the probability of ever reaching k from j.

First-passage quantities are computed by first-step (first-jump) analysis, conditioning on the first transition. The recursion f_{ij}^{(n)} = p_{ij} for n=1 and f_{ij}^{(n)} = \sum_{k\neq j} p_{ik} f_{kj}^{(n-1)} for n>1 has the clean matrix form f^{(n)} = (^{(j)}P)^{n-1} f^{(1)}, where ^{(j)}P is P with its j-th column zeroed. Generating functions give the dual identities P_{ii}(s) = 1/(1-F_{ii}(s)) and P_{ij}(s) = F_{ij}(s) P_{jj}(s), linking n-step transition probabilities to first-passage probabilities. Expected hitting/absorption times w_i = E_i\tau satisfy the linear system w_i = g(i) + \sum_{j} p_{ij} w_j (with reward g=1), solved in the finite case via the fundamental matrix as w = (I-Q)^{-1} 1. Applications: expected number of generations to reach the top occupational class, expected time to ruin, expected number of acts before a riot.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]