---
aliases: []
also_type: []
applies:
- named-entity-disambiguation
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
- computer-science
id: pkis:technique:hash-table
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch12
tags:
- hashing
- information-retrieval
- data-structures
- collision-resolution
- mackay-itila
title: Hash Table for Information Retrieval
understanding: 0
uses:
- hash-function
---

## Definition
A **hash table** solves the information-retrieval problem — invert the map $s \mapsto \mathbf{x}^{(s)}$ so that, given a key $\mathbf{x}$, we return its record number $s$ or report absence — using a hash function $h$ instead of a full $2^N$ look-up table.

### Encoding and decoding
**Encoding:** allocate a table of $2^M$ slots (each holding an integer in $[0,S]$), initialised to zero. For each record, write $s$ into slot $h(\mathbf{x}^{(s)})$.
**Decoding:** compute $h(\mathbf{x})$; a zero slot proves $\mathbf{x}$ is absent (cost: one hash + one look-up). A non-zero $s$ is only a *candidate* — it may be a collision — so look up the stored $\mathbf{x}^{(s)}$ and compare bit by bit. A successful retrieval costs one hash, one table look-up, one forward-database look-up, and $\le N$ binary comparisons.

### Resolving collisions
- **Appending in table (open addressing):** on collision, walk to the next zero slot (wrapping around); decoding walks the same chain until a match or a zero. Requires $2^M$ comfortably larger than $S$, else encoding gets stuck.
- **Storing elsewhere (chaining):** each slot points to a *bucket* holding all keys with that hash, kept as a short sorted list; permits a small table where almost every key collides but each bucket is tiny.

### Why it matters
The hash table is the canonical near-$O(1)$ retrieval structure and a concrete instance of trading a probabilistically-tolerated error (collisions) for a huge memory-and-time saving — the engineering counterpart to MacKay's information-theoretic compression arguments.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[named-entity-disambiguation]] — applies: Surface-collision handling in NED mirrors hash-table collision resolution: distinct entities sharing a key.
- [[hash-function]] — uses: A hash table is built on a hash function that maps keys to slots.
[To be populated during integration]