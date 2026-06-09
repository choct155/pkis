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
id: pkis:concept:poisson-random-measure
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch04
specializes:
- point-process
tags:
- stochastic-processes
- point-processes
- poisson-process
- random-measure
- complete-randomness
title: Poisson Random Measure (PRM)
understanding: 0
uses:
- laplace-functional
---

## Definition
A Poisson random measure with mean measure μ — written PRM(μ) — is the most tractable and central point process. Let μ be a measure on the state space (E, 𝒰) that is finite on bounded sets. A point process N is PRM(μ) if: (1) for each A ∈ 𝒰, N(A) is Poisson distributed with parameter μ(A), i.e. P[N(A)=k] = e^{-μ(A)} μ(A)^k / k! when μ(A) < ∞ (and N(A)=∞ a.s. when μ(A)=∞); and (2) for disjoint A_1,...,A_k, the counts N(A_1),...,N(A_k) are independent random variables. Property (2) is called complete randomness; on E = ℝ it specializes to the independent-increments property. When μ is a multiple of Lebesgue measure, μ(A) = α|A|, the process is homogeneous with rate α (the pathwise arrival rate, since t^{-1}N((0,t]) → α a.s.); otherwise it is non-homogeneous with local intensity α(·) where μ(dx)=α(x)dx. On [0,∞) the renewal construction Σ ε_{Γ_n} with Γ_n = E_1+···+E_n (iid unit-exponential gaps) yields the unit-rate homogeneous Poisson process (Prop. 4.2.1 / 4.8.1). A general PRM(μ) is constructed by: when μ(E)<∞, drawing a Poisson(μ(E)) number of iid points with law F(dx)=μ(dx)/μ(E); when μ(E)=∞, summing independent PRMs over a partition of E into finite-measure pieces. A key consequence: conditional on N(A)=n, the n points are iid with distribution μ(dx)/μ(A).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[laplace-functional]] — uses: PRM is characterized by exp{-int(1-e^{-f})dmu}
- [[point-process]] — specializes: PRM is the Poisson special case of a general point process
[To be populated during integration]