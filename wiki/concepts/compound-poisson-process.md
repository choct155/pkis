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
id: pkis:concept:compound-poisson-process
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch04
specializes:
- poisson-process
tags:
- stochastic-processes
- point-processes
- poisson-process
- levy-process
- stationary-independent-increments
- insurance-risk
title: Compound Poisson Process
understanding: 0
uses:
- marked-point-process
- laplace-functional
---

## Definition
Given a homogeneous Poisson process N on [0,∞) with rate α and an independent iid sequence of jump sizes {D_n}, the compound Poisson process is C(t) = Σ_{i=1}^{N((0,t])} D_i (with C(t)=0 when N((0,t])=0). It is the canonical elementary example of a Lévy process — a process with stationary and independent increments: C(t)−C(s) =_d C(t−s) and increments over disjoint intervals are independent. Both properties follow from marking (the D_n are real-valued marks) plus complete randomness over disjoint time regions, together with the transformation/translation invariance of the homogeneous mean measure. Its Laplace transform is E e^{−λ C(t)} = exp{α t (φ(λ) − 1)} = exp{−α t ∫_0^∞ (1 − e^{−λ x}) dG(x)}, where φ is the Laplace transform of D_1 and G its law; differentiating gives E C(t) = α t · E D_1 = E N((0,t]) · E D_1 (Wald-type identity). It models cumulative insurance claims, bulk/aggregate demand, and is the building block for the Lévy–Khintchine representation of general Lévy processes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[laplace-functional]] — uses: increment law derived via Laplace transform of the Poisson sum
- [[poisson-process]] — specializes: Poisson-driven cumulative-sum process; simplest Levy process
- [[marked-point-process]] — uses: jump sizes are real-valued marks on Poisson arrival times
[To be populated during integration]