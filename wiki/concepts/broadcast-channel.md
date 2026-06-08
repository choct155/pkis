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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:concept:broadcast-channel
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch15
tags:
- network-information-theory
- channel-capacity
- multi-user
- capacity-region
- degraded-channel
- superposition-coding
title: Broadcast Channel
understanding: 0
---

## Definition
A channel with **one transmitter and two (or more) receivers**, defined by $Q(y^{(A)}, y^{(B)}\mid x)$. The encoder must convey a common message at rate $R_0$ to all receivers plus private messages at rates $R_A, R_B$; performance is a **capacity region** (the convex hull of achievable triplets $(R_0, R_A, R_B)$).

### Beating time-sharing
The time-division benchmark achieves $(0, \phi_A C^{(A)}, \phi_B C^{(B)})$. One can do strictly better: an encoder fluent in both “languages” can layer a private stream on top of a common stream so each receiver decodes more than its time-share. This is **superposition coding**.

### Degraded broadcast channel
When the receivers form a Markov chain $x \to y^{(A)} \to y^{(B)}$ (so $B$ sees a further-degraded version of $A$'s output), anything reaching $B$ also reaches $A$. The problem collapses to finding the region for $(R_0, R_A)$: $R_0$ reaches both, $R_A$ is extra information reaching the better receiver $A$.

### Why it matters
It models one-to-many communication (TV, downlink, multicast) and is mathematically **equivalent to variable-rate coding for a channel of unknown noise level**: $R_0$ = high-priority bits guaranteed at the worst noise, $R_A$ = bonus low-priority bits delivered when noise is low.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]