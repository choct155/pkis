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
contrasts-with:
- arithmetic-coding
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:technique:huffman-coding
instantiates:
- source-coding-theorem
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch05
tags:
- symbol-codes
- prefix-code
- optimal-code
- data-compression
- greedy
title: Huffman Coding
understanding: 0
---

## Definition
The optimal symbol code: a prefix code assigning each source symbol an integer-length binary codeword, minimizing expected length. Built bottom-up by a greedy merge — repeatedly combine the two least-probable symbols into a node whose probability is their sum, until one tree remains; codeword = path of left/right (0/1) choices.

### Guarantee and limits
Huffman achieves expected length within one bit of entropy: $H(X) \le \mathbb{E}[l] < H(X)+1$, and is optimal among symbol codes (one integer-length codeword per symbol). Its weakness is exactly that integer constraint: when one symbol is very probable ($p\to1$), it must still spend a whole bit, so it wastes up to ~1 bit/symbol. It also adapts poorly to changing/contextual statistics. **Arithmetic coding** removes the integer-length limit by coding whole streams.

### Why it matters
The canonical instance of the source coding theorem made constructive — it shows entropy is not just a bound but nearly attainable with a simple algorithm. Its slack motivates stream codes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[arithmetic-coding]] — contrasts-with: Integer bits/symbol (Huffman) vs whole-stream coding escaping that limit (arithmetic)
- [[source-coding-theorem]] — instantiates: Optimal symbol code; achieves within 1 bit of H
[To be populated during integration]