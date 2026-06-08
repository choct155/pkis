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
id: pkis:concept:channel-capacity
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- noisy-channel-coding-theorem
related_concepts: []
sources:
- mackay-itila-ch01
tags:
- capacity
- noisy-channel
- rate
- mutual-information
- shannon
title: Channel Capacity
understanding: 0
uses:
- information-theory
---

## Definition
The **capacity** $C$ of a noisy channel is the maximum rate at which information can be communicated with arbitrarily small probability of error. Formally it is the maximum, over input distributions, of the mutual information between channel input and output:
$$C=\max_{p(x)} I(X;Y).$$
It is the point where the boundary between achievable and non-achievable $(R,p_b)$ points meets the rate axis.

The intuition: every channel, however noisy, has a hard ceiling on reliable throughput — and that ceiling is strictly positive.

### The surprise
It was widely believed the achievable boundary passed through the origin, so vanishing error would demand vanishing rate ('no pain, no gain'). Capacity says otherwise: reliable communication is possible at *every* rate $R<C$, and impossible for $R>C$.

### Why it matters
Capacity is the central quantity of information theory: it sets the fundamental limit that no encoder/decoder can beat and the target that good codes approach. It connects coding (channel side) to entropy and mutual information (the measurement side), unifying compression and communication.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[information-theory]] — uses: Capacity is defined via mutual information, a core information-theoretic quantity.
- [[noisy-channel-coding-theorem]] — prerequisite-of: Capacity is the threshold quantity whose existence and value the coding theorem establishes.
[To be populated during integration]