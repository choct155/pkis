---
aliases: []
also_type: []
applies:
- brownian-motion
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
- statistical-learning
id: pkis:concept:quadratic-variation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch06
tags:
- stochastic-processes
- brownian-motion
- stochastic-calculus
- path-properties
title: Quadratic Variation
understanding: 0
uses:
- borel-cantelli-lemma
---

## Definition
For a partition $\Pi = \{0 = t_0 < \cdots < t_n = t\}$ of $[0,t]$, the quadratic variation of a path $B$ over $\Pi$ is $Q(\Pi) = \sum_k |B(t_k) - B(t_{k-1})|^2$. For Brownian motion, as the mesh $\Delta(\Pi) \to 0$ (along refining partitions shrinking fast enough), $Q(\Pi) \to t$ almost surely — the quadratic variation of $B$ on $[0,t]$ equals the (deterministic) length $t$. The proof shows $E(Q(\Pi) - t)^2 = 2\sum_k (t_k - t_{k-1})^2 \le 2\Delta(\Pi)\,t \to 0$ (using $E N^4 = 3$ for $N(0,1)$), then upgrades $L^2$ to a.s. convergence via Chebyshev + Borel-Cantelli.

This is the path property distinguishing diffusions from smooth functions: Brownian paths have finite, nonzero quadratic variation but infinite total (first-order) variation, so they are continuous yet not rectifiable. As a function of $t$, the quadratic variation defines the *quadratic variation process* — central to stochastic integration, where it is the increasing process subtracted from a submartingale to recover a martingale, and the random time-change turning stochastic integrals into Brownian motions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[borel-cantelli-lemma]] — uses: Almost-sure convergence Q -> t is obtained from an L2 bound plus Chebyshev and Borel-Cantelli.
- [[brownian-motion]] — applies: Quadratic variation is the path functional that equals t for Brownian motion, separating it from smooth functions.
[To be populated during integration]