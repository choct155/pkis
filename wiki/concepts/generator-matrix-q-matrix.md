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
date_updated: '2026-06-20'
domain:
- bayesian-stats
- statistical-learning
- systems-theory
id: pkis:concept:generator-matrix-q-matrix
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- kolmogorov-forward-backward-equations
related_concepts: []
sources:
- resnick-stochastic-processes-ch05
- lange-applied-probability-ch08
tags:
- stochastic-processes
- markov
- linear-algebra
title: Generator Matrix (Q-Matrix)
understanding: 0
---

## Definition
The generator matrix A (often called Q in other texts) of a continuous-time Markov chain encodes the infinitesimal transition rates of the process. It is built from the holding-rate function lambda(i) and the embedded transition matrix Q by

A_ij = -lambda(i)        if i = j,
A_ij = lambda(i) * Q_ij   if i != j.

## Structure
Off-diagonal entries are non-negative (rates of probability flow from i toward j), diagonal entries are non-positive, and every row sums to zero: sum_j A_ij = -lambda(i) + sum_{j!=i} lambda(i)Q_ij = 0. The zero-row-sum property saves work: only m-1 entries of an m-state generator need be computed.

## Probabilistic Interpretation
A = P'(0), the derivative of the transition function at 0. For small t, 1 - P_ii(t) = lambda(i)t + o(t), so lambda(i) is the total flow rate of probability out of state i; and P_ij(t) = lambda(i)Q_ij t + o(t), so A_ij = lambda(i)Q_ij is the flow rate of probability from i toward j. In a birth-death process A_{i,i+1} = lambda_i (birth rate) and A_{i,i-1} = mu_i (death rate).

## Recovering Ingredients
A and the pair (Q, lambda) carry identical information: lambda(i) = -A_ii and Q_ij = -A_ij/A_ii for i != j. Likewise {P(t), t>0} carries the same analytic information as A, via A = P'(0).

## Role
The generator is the analytic engine of the CTMC: the transition function solves P'(t)=AP(t) (backward) and P'(t)=P(t)A (forward); for finite S, P(t) = exp(At). Stationary measures solve eta'A = 0.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[kolmogorov-forward-backward-equations]] — prerequisite-of: The generator must be understood before the Kolmogorov equations that use it.
[To be populated during integration]