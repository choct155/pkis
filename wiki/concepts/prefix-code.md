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
id: pkis:concept:prefix-code
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch05
specializes:
- uniquely-decodable-codes
tags:
- symbol-codes
- prefix-free
- instantaneous-code
- self-punctuating
- binary-trees
title: Prefix Codes (Instantaneous Codes)
understanding: 0
uses:
- kraft-inequality
---

## Definition
A symbol code is a **prefix code** if no codeword is a prefix of any other codeword. For example $C_3=\{0,10,110,111\}$ is a prefix code, whereas $\{1,101\}$ is not, since $1$ is a prefix of $101$.

A prefix code is also called **instantaneous** or **self-punctuating**: an encoded stream can be decoded left to right without looking ahead, because the end of each codeword is recognizable the moment it arrives. Every prefix code is uniquely decodable (the converse is false).

### Correspondence with trees
Prefix codes correspond exactly to binary trees: each codeword is a leaf, and the prefix condition forbids any codeword from lying on the path to another. A **complete** prefix code corresponds to a tree with no unused branches.

### Why it matters
Prefix codes give instantaneous decoding yet sacrifice nothing in compression: for any source there exists an *optimal* symbol code that is also a prefix code, since any lengths satisfying the Kraft inequality can be realized by a prefix code. Thus the search for optimal symbol codes can be restricted, without loss, to prefix codes — the principle exploited by Huffman coding.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[kraft-inequality]] — uses: Lengths satisfying Kraft are realizable as a prefix code via the supermarket construction.
- [[uniquely-decodable-codes]] — specializes: Every prefix code is uniquely decodable; the converse fails (e.g. C6).
[To be populated during integration]