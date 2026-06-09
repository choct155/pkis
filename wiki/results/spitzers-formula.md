---
aliases: []
also_type: []
applies:
- random-walk
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
id: pkis:result:spitzers-formula
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch07
tags:
- random-walk
- running-maximum
- fluctuation-theory
- transforms
title: Spitzer's Formula
understanding: 0
uses:
- wiener-hopf-factorization
- ladder-epochs-and-heights
---

## Definition
Spitzer's formula gives the generating function of the characteristic functions of the running maximum M_n = max_{0<=j<=n} S_j of a random walk in terms of the step distribution alone: sum_{n>=0} q^n E exp{i zeta M_n} = exp{ sum_{n>=1} (q^n/n) E e^{i zeta S_n^+} }, for 0 < q < 1, where S_n^+ = max(S_n, 0).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[ladder-epochs-and-heights]] — uses
- [[random-walk]] — applies
- [[wiener-hopf-factorization]] — uses
[To be populated during integration]