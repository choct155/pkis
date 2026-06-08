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
- deep-learning
- statistical-learning
id: pkis:concept:associative-memory
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch42
tags:
- associative-memory
- content-addressable-memory
- pattern-completion
- hebbian-learning
- error-correction
- attractor
title: Associative (Content-Addressable) Memory
understanding: 0
---

## Definition
An **associative**, or **content-addressable**, memory retrieves a stored item from a *partial or corrupted version of its content* rather than from an explicit address. Presenting a fragment or noisy cue causes the system to relax to the nearest complete stored pattern — **pattern completion** and **error correction**.

The foundational mechanism is **Hebbian learning** (Hebb, 1949): the weight between two neurons grows with the correlation of their activities,
$$\frac{dw_{ij}}{dt} \sim \mathrm{Correlation}(x_i,x_j).$$
If the smell of a banana ($x_m$) and the sight of yellow ($x_n$) repeatedly co-occur, $w_{mn}$ grows, so later the sight alone reactivates the smell. The rule is **unsupervised and local**: no teacher and no global error signal are required.

### Memory as a communication channel
A list of memories is encoded into weights $\mathbf{W}$; a receiver seeing only $\mathbf{W}$ recovers them as the network's stable states. This channel can fail by bit corruption, missing memories, spurious memories, or *mixture/inverse* states — the last of which can be read as crude **generalization** (e.g. accepting 'John loves cake' after learning 'John loves Mary').

### Why it matters
Associative memory is the striking computational property distinguishing biological from digital memory, and it is exactly what a Hopfield network's attractor dynamics realize. Its robustness — working even when many weights are deleted — models graceful degradation absent from conventional addressed memory.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]