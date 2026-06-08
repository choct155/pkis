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
id: pkis:concept:multiple-access-channel
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
- shared-medium
title: Multiple-Access Channel
understanding: 0
---

## Definition
A channel with **two (or more) independent senders** and a **single receiver**, defined by $Q(y\mid x^{(A)}, x^{(B)})$, where the senders cannot coordinate. Performance is described not by a scalar capacity but by a **capacity region**: the set of simultaneously achievable rate pairs $(R_A, R_B)$.

### Adder example
With binary inputs and ternary output $y = x^{(A)} + x^{(B)} \in \{0,1,2\}$ (noiseless), output $0$ and $2$ are unambiguous but $1$ hides whether the inputs were $(0,1)$ or $(1,0)$. Naive time-sharing gives total rate $1$, but coordinated coding achieves $R_A + R_B > 1$: the boundary of the region is reached by codes where each user transmits at a rate that, combined with the structure of the sum, lets the decoder resolve both messages.

### Capacity region (general)
Reliable $(R_A, R_B)$ are bounded by
$$R_A \le I(X^{(A)};Y\mid X^{(B)}),\; R_B \le I(X^{(B)};Y\mid X^{(A)}),\; R_A+R_B \le I(X^{(A)},X^{(B)};Y),$$
maximized over independent input distributions.

### Why it matters
It models any shared medium—cellular uplinks, Ethernet, ship VHF—and shows that uncoordinated users can still collectively exceed simple time-division rates. It is the channel-coding dual of the Slepian–Wolf source-coding result.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]