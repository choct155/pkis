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
id: pkis:concept:stream-codes
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch06
tags:
- data-compression
- source-coding
- arithmetic-coding
- lempel-ziv
title: Stream Codes
understanding: 0
---

## Definition
A class of lossless source codes whose distinctive property is that, unlike symbol codes, they are **not constrained to emit at least one bit per source symbol**. Many source symbols can be coded jointly into a smaller number of bits, so the per-symbol cost can drop well below one bit without the cumbersome blocking that symbol codes require.

### Contrast with symbol codes
A symbol code (e.g. Huffman) assigns each source symbol its own integer-length codeword, forcing $\ge 1$ bit/symbol and leaving up to ~1 bit/symbol of slack when one symbol is very probable. Stream codes remove this granularity: arithmetic coding maps a string to a sub-interval of $[0,1)$ of width equal to its probability; Lempel–Ziv maps repeated substrings to pointers. Both approach the Shannon information content of the entire message.

### Why it matters
Stream codes are MacKay's organizing category for the two practically important compressors — arithmetic coding and Lempel–Ziv. A caveat: because the entire stream is interdependent, a single corrupted bit destroys the rest of the decoding, so stream-compressed data needs error-correcting codes if stored or sent over noisy media.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]