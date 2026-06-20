---
aliases: []
also_type: []
applies:
- poisson-process
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-20'
domain:
- bayesian-stats
id: pkis:result:poisson-order-statistic-property
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch04
- lange-applied-probability-ch06
tags:
- stochastic-processes
- point-processes
- poisson-process
- order-statistics
- uniform-distribution
title: Order Statistic Property of the Poisson Process
understanding: 0
uses:
- probability-theory
---

## Definition
For a homogeneous Poisson process N on [0,∞) with rate α, conditional on the event [N((0,t]) = n], the n points in (0,t] taken in increasing order are distributed exactly as the order statistics U_{(1)} < ··· < U_{(n)} of n iid Uniform(0,t) random variables (Theorem 4.5.2): (Γ_1,...,Γ_n | N(0,t]=n) =_d (U_{(1)},...,U_{(n)}), with conditional density n!/t^n on 0<u_1<···<u_n<t. Equivalently, conditional on n points the locations are 'thrown uniformly at random.' This is the [0,∞) special case of the general PRM fact that, given N(A)=n, the points are iid with law μ(·)/μ(A). For symmetric functions g — e.g. additive functionals Σ h(X_i) — one may replace order statistics by iid uniforms, the key device for computing transforms of functionals such as shot-noise processes. Because it follows from order statistics alone, this property does NOT characterize the Poisson process (mixed Poisson processes also possess it). It motivates using the homogeneous Poisson process as the statistical null hypothesis of 'no interaction' / complete spatial randomness.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[probability-theory]] — uses: relies on order statistics of the uniform distribution
- [[poisson-process]] — applies: conditional uniformity of homogeneous Poisson points
[To be populated during integration]