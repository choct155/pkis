---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
- systems-theory
id: pkis:result:kolmogorov-forward-backward-equations
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch05
tags:
- stochastic-processes
- markov
- differential-equations
title: Kolmogorov Forward and Backward Equations
understanding: 0
uses:
- generator-matrix-q-matrix
---

## Definition
The Kolmogorov differential equations govern the transition function P(t) = {P_ij(t)} of a continuous-time Markov chain in terms of its generator matrix A.

## Backward Equation
Obtained by conditioning on the first jump (place and time):

P'(t) = A P(t),   i.e.   d/dt P_ij(t) = sum_k A_ik P_kj(t),

with initial condition P(0) = I. Resnick derives it first from the backward integral equation P_ij(t) = delta_ij e^{-lambda(i)t} + integral_0^t lambda(i) e^{-lambda(i)s} sum_{k!=i} Q_ik P_kj(t-s) ds (Proposition 5.4.1), then differentiates. The backward equation is considered more fundamental.

## Forward Equation
Obtained by conditioning on the last jump before t, or formally by differentiating the Chapman-Kolmogorov relation P(t+s) = P(t)P(s) in s and setting s=0:

P'(t) = P(t) A.

The forward equation is often easier to solve in practice but can fail if explosions are possible (the last jump may not exist).

## Matrix-Exponential Solution
When S is finite, both equations have the formal solution

P(t) = exp(At) = sum_{n>=0} t^n A^n / n!.

## Solution Techniques
Resnick illustrates several: direct ODE solving, eigendecomposition of A (matrix methods), Laplace transforms with hat-P(alpha) = (alpha I - A)^{-1}, and renewal-theoretic arguments. Closed-form solutions are usually attainable only in small/toy problems.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[generator-matrix-q-matrix]] — uses: Both equations are stated in terms of the generator matrix A.
[To be populated during integration]