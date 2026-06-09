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
id: pkis:result:blackwells-renewal-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch03
tags:
- renewal-theory
- asymptotic-theory
- arithmetic-vs-non-arithmetic
title: Blackwell's Renewal Theorem
understanding: 0
---

## Definition
Blackwell's theorem describes the asymptotically constant rate of accumulation of expected renewals: for a renewal process with proper delay distribution and mean interarrival mu, the expected number of renewals in a window of fixed width a far from the origin converges, V(t, t+a] -> a/mu as t -> infinity (non-arithmetic case). In the arithmetic case with span 1 the statement becomes u_n = p_00^{(n)} -> 1/mu and U(n, n+h] -> h/mu, which is exactly the aperiodic-state limit theorem for the embedded success-run Markov chain. Blackwell's theorem is finer than the elementary renewal theorem — it bears the same relation to it that ordinary sequence convergence bears to Cesaro convergence (averaging V(n-1,n] -> 1/mu recovers V(0,n]/n -> 1/mu). It is equivalent to the key renewal theorem, and supplies the local interpretation U(dx) ~ dx/mu used throughout asymptotic renewal analysis.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]