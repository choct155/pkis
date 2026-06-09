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
- statistical-learning
id: pkis:concept:first-passage-time
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch01
tags:
- probability-theory
- stochastic-processes
- random-walk
- hitting-times
- generating-functions
title: First-Passage Time
understanding: 0
---

## Definition
$$N = \inf\{n \ge 1 : S_n = a\}, \qquad \tau_B = \inf\{n \ge 0 : \xi_n \in B\}$$

The first-passage (or hitting) time is the first index at which a process reaches a target level $a$ or enters a target set $B$; by convention $\inf\emptyset = +\infty$, so a passage that never occurs has time $\infty$.

### Hitting times are stopping times
For a process adapted to $\mathcal{F}_n = \sigma(\xi_0,\ldots,\xi_n)$, the event $[\tau_B = n] = [\xi_0 \in B^c, \ldots, \xi_{n-1}\in B^c, \xi_n \in B] \in \mathcal{F}_n$, so every hitting time is a stopping time.

### Distribution via generating functions
For the simple random walk hitting $1$, conditioning on the first step and using the regeneration of i.i.d. increments yields a quadratic for $\Phi(s)=Es^N$, solved as $\Phi(s) = (1-\sqrt{1-4pqs^2})/(2qs)$. From it, $P[N<\infty] = (1-|p-q|)/2q$, which equals $1$ iff $p \ge q$, and $EN = (p-q)^{-1}$ when $p>q$ but $EN=\infty$ in the symmetric case. The first return to the origin is certain when $p=q=1/2$ yet has infinite expected time.

### Why it matters
First-passage times answer the central questions of random dynamics — Will the gambler ever get ahead? Will the population go extinct? Will the queue empty? Their distributions, recurrence versus transience, and finite-versus-infinite expectation are recurring themes, and the generating-function recursion shown here is the prototype technique.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]