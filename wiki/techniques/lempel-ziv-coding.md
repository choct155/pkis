---
aliases: []
also_type: []
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
id: pkis:technique:lempel-ziv-coding
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch06
tags:
- stream-codes
- data-compression
- dictionary-coding
- universal-coding
- adaptive
title: Lempel–Ziv Coding
understanding: 0
---

## Definition
A family of dictionary-based stream codes that compress by replacing a substring with a pointer to an earlier occurrence of the same substring. In the basic algorithm the input is parsed left-to-right into an ordered dictionary of substrings not seen before; each new substring is one bit longer than an existing entry, so it is transmitted as a pointer to that prefix (in $\lceil \log_2 s(n) \rceil$ bits, where $s(n)$ is the dictionary size so far) plus the one differing bit.

### How it differs from arithmetic coding
Unlike arithmetic coding, there is **no separation between modelling and coding** and no explicit probabilistic model. The dictionary *is* the model, built adaptively from the data alone. The decoder reconstructs the identical dictionary as it reads, so no model needs to be transmitted. Practical variants (LZ77 → gzip, LZW → compress) differ mainly in dictionary management.

### Universality
For any ergodic source, Lempel–Ziv provably compresses asymptotically down to the source entropy — hence 'universal'. The catch is that this limit may need infeasibly large data, so sources with long-range correlations are handled poorly.

### Why it matters
It is the workhorse of everyday lossless compression (gzip, compress, zip). It embodies the opposite philosophy to arithmetic coding: rather than model-then-code, assume nothing and let repetition reveal redundancy.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]