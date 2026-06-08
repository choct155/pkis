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
id: pkis:concept:uniquely-decodable-codes
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch05
tags:
- symbol-codes
- source-coding
- lossless-compression
- unique-decodeability
- kraft-mcmillan
title: Uniquely Decodable Codes
understanding: 0
---

## Definition
A symbol code $C$ maps each symbol $a_i\in A_X$ to a binary codeword of length $l_i$, and the extended code encodes a string by concatenation without punctuation. The code is **uniquely decodable** if no two distinct source strings share an encoding:
$$\forall x,y\in A_X^+,\quad x\neq y \;\Rightarrow\; c^+(x)\neq c^+(y).$$
This is the minimal requirement for losslessness.

### A property of lengths, not patterns
Unique decodeability is a property of the codeword *lengths*: by the Kraft–McMillan theorem, lengths $\{l_i\}$ admit a uniquely decodable code iff $\sum_i 2^{-l_i}\le 1$. This decouples existence from construction and underlies every optimality result for symbol codes.

### Decodeability vs ease of decoding
Unique decodeability does not imply easy decoding. The code $C_6=\{0,01,011,111\}$ is uniquely decodable but requires unbounded look-ahead. Codes that decode left-to-right with no look-ahead are the special subclass of prefix codes.

### Why it matters
Unique decodeability is what makes a variable-length code usable at all. A code can have small expected length yet be useless: $C_5=\{0,1,00,11\}$ has $L=1.25$ but decodes ambiguously.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]