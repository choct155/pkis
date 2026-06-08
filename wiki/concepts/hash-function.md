---
aliases: []
also_type: []
analogous-to:
- typical-set
- noisy-channel-coding-theorem
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
- computer-science
id: pkis:concept:hash-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- hashing-for-error-detection
related_concepts: []
sources:
- mackay-itila-ch12
tags:
- hashing
- information-retrieval
- dimensionality-reduction
- random-codes
- mackay-itila
title: Hash Function
understanding: 0
---

## Definition
A **hash function** is a deterministic map
$$h : \{0,1\}^N \to \{0,1\}^M, \qquad M < N,$$
that compresses an $N$-bit key $\mathbf{x}$ to a short $M$-bit *hash* $h(\mathbf{x})$, where the table size $T \simeq 2^M$ is chosen a little larger than the number of stored items $S$ (e.g. $T \approx 10S$). The ideal hash function should be *quick to compute* yet *indistinguishable from a fixed random code*: each key should appear to land in a uniformly random one of the $T$ slots, independently of all others.

### Why it matters
MacKay frames hashing as the synthesis of two earlier ideas. Source coding mapped $N$ symbols down to a label (a typical-set encoder); channel coding mapped $K$ bits *up* to $N$ bits using random codes. Hashing reuses the random-code idea to map *down*, projecting a high-dimensional key space ($2^N$ huge) into a small space ($2^M$) where the otherwise-impossible direct look-up table becomes feasible. This makes information retrieval cost roughly one hash evaluation plus one table look-up, beating the raw list ($\sim S+N$ comparisons) and the alphabetical list ($\lceil\log_2 S\rceil$ string comparisons).

### Simple constructions
- **Division method:** $h(x) = x \bmod T$ with $T$ a prime not near a power of 2.
- **Variable string addition:** sum the bytes of $x$ modulo $T$; weak (anagrams collide) unless a pseudo-random permutation is interleaved after each character (the XOR variant gives a 16-bit hash).

A hash function is *not* injective, so retrieval must confirm a hit by comparing $\mathbf{x}$ against the stored $\mathbf{x}^{(s)}$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[noisy-channel-coding-theorem]] — analogous-to: Hash codes reuse the random-code idea of channel coding, but mapping N bits down to M<N rather than up.
- [[typical-set]] — analogous-to: MacKay derives hashing from the unsolved typical-set compression encoder: both map N bits down to a short label.
- [[hashing-for-error-detection]] — prerequisite-of: Error detection computes and compares hashes of files.
[To be populated during integration]