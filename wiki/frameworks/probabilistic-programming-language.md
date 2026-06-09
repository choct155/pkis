---
aliases: []
also_type: []
applies:
- statistical-relational-learning
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- knowledge-representation
id: pkis:framework:probabilistic-programming-language
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch15
tags:
- probabilistic-programming
- generative-models
- first-order-probability
- universal-models
- inference-engine
title: Probabilistic Programming Language
understanding: 0
---

## Definition
A universal formal language for specifying probability models, in the sense that Turing machines are universal: a PPL can represent any computable probability distribution and ships with general-purpose inference algorithms (analogous to sound-and-complete logical inference). PPLs arise via two routes. The first, declarative route extends probability theory through logic, defining distributions over first-order possible worlds rather than the propositional possible worlds of Bayes nets (yielding relational and open-universe probability models). The second route injects random choices into a conventional programming language, so that programs define distributions over their own execution traces, inheriting the host language's recursion, data structures, and higher-order functions. Concrete systems include BUGS, STAN, BLOG, Church, Figaro, Gen, Pyro, and Edward. Inference is generally approximate (rejection/likelihood-weighting, MCMC, sequential Monte Carlo, HMC) because exact inference does not scale; with infinite-precision continuous variables inference can even encode the halting problem, though it remains decidable for finite-precision smooth distributions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[statistical-relational-learning]] — applies: PPLs operationalize the SRL goal of unifying first-order logic with probabilistic inference
[To be populated during integration]