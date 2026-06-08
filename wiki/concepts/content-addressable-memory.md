---
aliases: []
also_type: []
applies:
- neural-networks
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- hash-table
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- deep-learning
id: pkis:concept:content-addressable-memory
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch38
tags:
- neural-networks
- associative-memory
- robustness
title: Content-Addressable Memory
understanding: 0
---

## Definition
A memory system in which a stored pattern is retrieved by supplying a *part of its content* (a cue) rather than an external address. Formally, given a set of stored patterns $\{\mathbf{x}^{(n)}\}$ and a partial or corrupted query $\tilde{\mathbf{x}}$, the system returns the stored pattern most consistent with the query, $\hat{\mathbf{x}} = \arg\max_n \, \text{compat}(\tilde{\mathbf{x}}, \mathbf{x}^{(n)})$, typically by relaxation dynamics that settle into an attractor. MacKay contrasts this with conventional **address-based memory**, where the address is arbitrary and carries no relationship to the stored content.

### Three properties of address-based memory it lacks
Conventional digital memory is (1) *not associative* — you cannot recall a memory from half of its content without its address; (2) *not robust* — a one-bit error in the address retrieves a completely unrelated item, and the fault-tolerance of modern memory comes from bolted-on error-correcting codes, not from the storage scheme itself; (3) *not distributed* — only the CPU and the addressed byte participate in a recall while millions of other devices sit idle.

### Biological motivation
Biological memory exhibits exactly the converse: it is associative (a name evokes a face and vice versa), error-tolerant (the cue "intelligent politician whose father disliked broccoli" still evokes Bush despite a factual error), and parallel/distributed (many neurons participate in storing many memories). These properties motivate artificial neural network memory models such as the Hopfield network.

### Why it matters
Content-addressability reframes "memory" as an inference problem — completing or correcting a pattern — rather than a lookup. This makes graceful degradation an *intrinsic* property of the substrate and connects associative recall directly to attractor dynamics and energy-based models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hash-table]] — contrasts-with: Hash tables give fast address-based lookup keyed by an arbitrary hash of a key; content-addressable memory instead retrieves by partial content and degrades gracefully, the properties MacKay shows address-based schemes lack.
- [[neural-networks]] — applies: Associative neural network memories (e.g. Hopfield nets) are the canonical realization of content-addressable storage; MacKay introduces CAM precisely to motivate these models.
[To be populated during integration]