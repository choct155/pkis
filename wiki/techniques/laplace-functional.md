---
aliases: []
also_type: []
applies:
- point-process
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:technique:laplace-functional
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch04
tags:
- stochastic-processes
- point-processes
- transform-methods
- poisson-process
- laplace-transform
title: Laplace Functional
understanding: 0
---

## Definition
The Laplace functional is the transform that characterizes the distribution of a point process, generalizing the moment/Laplace transform of a random vector. For a point measure m = Σ_i ε_{x_i} and a non-negative bounded test function f ∈ B_+, write m(f) = ∫_E f dm = Σ_i f(x_i). The Laplace functional of a point process N is Ψ_N(f) = E exp{−N(f)} = E exp{−Σ_i f(X_i)}, viewed as a function on B_+. Because integrating against arbitrary test functions encodes as much information as evaluating the measure on arbitrary sets (take f = λ·1_A), the Laplace functional uniquely determines the law of N (Prop. 4.7.2): substituting simple functions f = Σ λ_i 1_{I_i} recovers all finite-dimensional joint Laplace transforms. Its signature use is the clean characterization of the Poisson process: N is PRM(μ) if and only if Ψ_N(f) = exp{−∫_E (1 − e^{−f(x)}) μ(dx)} for all f ∈ B_+ (Theorem 4.8.2). This identity reduces many proofs — marking, thinning, superposition, the renewal construction, and existence of PRM(μ) — to algebra on exponentials, since superposition of independent processes multiplies Laplace functionals.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[point-process]] — applies: the Laplace functional is the characterizing transform of a point process
[To be populated during integration]