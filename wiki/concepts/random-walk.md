---
aliases: []
also_type: []
analogous-to:
- diffusion-processes
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
id: pkis:concept:random-walk
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch07
tags:
- stochastic-processes
- iid-sums
- fluctuation-theory
- queueing
title: Random Walk
understanding: 0
uses:
- martingales
---

## Definition
A random walk is the sequence of partial sums {S_n, n >= 0} formed from iid real-valued steps {X_n, n >= 1}: S_0 = 0, S_n = X_1 + ... + X_n. The common step distribution F(x) = P[X_1 <= x] determines all global behavior. It is the discrete-time prototype of Brownian motion and the structural skeleton embedded in queueing, storage, and time-series models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[martingales]] — uses
- [[diffusion-processes]] — analogous-to: random walk is the discrete-time prototype of Brownian motion
[To be populated during integration]