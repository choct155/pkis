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
id: pkis:result:wiener-hopf-factorization
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch07
tags:
- random-walk
- convolution
- ladder-heights
- transforms
- queueing
title: Wiener-Hopf Factorization (Random Walk)
understanding: 0
---

## Definition
For a random walk with step distribution F, geometric killing time T with P[T >= n] = q^n, and any dual pair of stopping times tau, eta, the step law factors as delta - qF = (delta - H_{tau,q}) * (delta - H_{eta,q}), where H_{tau,q}(.) = P[S_tau in ., tau <= T] is the q-discounted ladder-height measure. Specialized to (N, Nbar) it separates the joint transform of the ascending ladder pair (N, S_N) from that of the descending pair.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]