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
id: pkis:result:borel-cantelli-lemma
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch06
tags:
- probability-theory
- almost-sure-convergence
- infinitely-often
title: Borel-Cantelli Lemma
understanding: 0
---

## Definition
For a sequence of events $\{A_n\}$, let $[A_n \text{ i.o.}] = \bigcap_m \bigcup_{n\ge m} A_n$ be the event that infinitely many $A_n$ occur. The Borel-Cantelli lemma has two halves:
- **(Convergence half)** If $\sum_n P(A_n) < \infty$, then $P[A_n \text{ i.o.}] = 0$ — almost surely only finitely many of the events occur. (Proof: $E\sum_n \mathbf{1}_{A_n} = \sum_n P(A_n) < \infty$, so $\sum_n \mathbf{1}_{A_n} < \infty$ a.s.)
- **(Divergence half, converse)** If the $A_n$ are *independent* and $\sum_n P(A_n) = \infty$, then $P[A_n \text{ i.o.}] = 1$.

It is the standard workhorse for upgrading summable probability bounds into almost-sure statements. In Brownian-motion theory it appears throughout: controlling the dyadic-refinement errors in the Levy construction, establishing nowhere-differentiability, proving the a.s. convergence of quadratic variation, and supplying both halves of the law of the iterated logarithm.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]