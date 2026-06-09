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
id: pkis:concept:transition-matrix
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch02
tags:
- stochastic-processes
- markov-property
- linear-algebra
- chapman-kolmogorov
title: Transition Matrix (Stochastic Matrix)
understanding: 0
---

## Definition
For a discrete-state Markov chain {X_n}, the transition matrix P = (p_{ij}) records the one-step transition probabilities p_{ij} = P[X_{n+1}=j | X_n=i]. It is a stochastic matrix: entries are non-negative and every row sums to 1 (\sum_j p_{ij} = 1). Together with an initial distribution {a_k}, P fully determines the chain's finite-dimensional distributions via P[X_0=i_0,\dots,X_k=i_k] = a_{i_0} p_{i_0 i_1}\cdots p_{i_{k-1}i_k}.

The analytic power of Markov chains rests on the fact that probabilistic questions reduce to matrix algebra. The n-step transition probabilities are the entries of the matrix power: p_{ij}^{(n)} = P[X_n=j | X_0=i] = (P^n)_{ij}, with P^0 = I. The marginal law evolves by left-multiplication, (a^{(n)})' = a' P^n. The semigroup identity P^{n+m} = P^n P^m, written componentwise as p_{ij}^{(n+m)} = \sum_k p_{ik}^{(n)} p_{kj}^{(m)}, is the Chapman-Kolmogorov equation: a path from i to j in n+m steps decomposes by summing over the intermediate state k visited at time n. Stationary (homogeneous) transition probabilities mean p_{ij} does not depend on n. Computing P^n in practice requires either numerical methods or eigenvalue/Jordan expansions; the 2x2 case admits a closed form revealing geometric convergence to a limiting matrix with constant columns.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]