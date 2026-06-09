---
aliases: []
also_type: []
analogous-to:
- blackwells-renewal-theorem
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
id: pkis:result:key-renewal-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch03
tags:
- renewal-theory
- asymptotic-theory
- convolution
- direct-riemann-integrability
title: Key Renewal Theorem
understanding: 0
uses:
- renewal-equation
- renewal-function
---

## Definition
Originally formulated by Walter Smith. For the solution Z = U*z of a proper renewal equation Z = z + F*Z (F non-arithmetic, proper), if z is *directly Riemann integrable* (dRi; satisfied e.g. when z is non-negative, decreasing, and integrable) then lim_{t->infinity} Z(t) = mu^{-1} integral_0^infinity z(s) ds, where mu = E Y_1. It is the engine of the renewal method: once a quantity is written as a convolution U*z, its limit is obtained simply by integrating z. The key renewal theorem is logically equivalent to Blackwell's theorem (it is heuristically plausible because U(t-y, t-y+dy] ~ dy/mu by Blackwell). Applying it to the recurrence-time renewal equations yields the equilibrium (length-biased) limit distribution F_0(x) = mu^{-1} integral_0^x (1-F(s)) ds for both the age A(t) and excess B(t). In the arithmetic/discrete case the analogue is lim_n U*z(n) = mu^{-1} sum_{k>=0} z(k), which (with Blackwell's discrete form u_n -> 1/mu) follows directly from the aperiodic Markov chain limit theorem.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[blackwells-renewal-theorem]] — analogous-to
- [[renewal-function]] — uses
- [[renewal-equation]] — uses
[To be populated during integration]