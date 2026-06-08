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
id: pkis:concept:turbo-code
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch48
tags:
- error-correcting-codes
- turbo-codes
- interleaver
- factor-graph
- near-capacity-codes
title: Turbo Code
understanding: 0
---

## Definition
A **turbo code** is an $(N,K)$ code defined by several **constituent convolutional encoders** (usually two) together with an equal number of **interleavers** — $K\times K$ permutation matrices that scramble the order in which source bits enter each encoder (the first interleaver is taken to be the identity). A string of $K$ source bits is fed into each encoder in its interleaved order; the transmitted codeword is the $K$ source bits followed by the parity bits from each constituent code. With a systematic first encoder and a rate-1 parity-only second encoder, the result is a rate-$1/3$ code; **puncturing** (deleting) parity bits raises the rate, e.g. to $1/2$.

### Factor-graph view
A turbo code is represented by a factor graph with one large rectangular node per trellis. The $K$ source bits and the first $M_1$ parity bits sit in trellis 1; the $K$ source bits and the last $M_2$ parity bits sit in trellis 2. Each source bit participates in *both* trellises (coupling them via the interleaver); each parity bit in only one. This representation yields the standard turbo sum–product decoder.

### Performance and error floor
Turbo codes achieve excellent performance down to error probabilities around $10^{-5}$, but random constructions exhibit an **error floor** there, caused by low-weight codewords. Eliminating these requires sacrificing the code's near-capacity performance — a notorious black art.

### Why it matters
Turbo codes were among the first practical codes to approach Shannon capacity. Because their parity constraints come from sparse constituent trellises, turbo codes are themselves special cases of low-density parity-check codes (a punctured turbo code instead has a sparse *generalized* parity-check matrix).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]