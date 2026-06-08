---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:result:kraft-inequality
knowledge_type: result
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- huffman-coding
related_concepts: []
sources:
- mackay-itila-ch05
tags:
- prefix-code
- symbol-codes
- unique-decodability
- codeword-lengths
title: Kraft Inequality
understanding: 0
---

## Definition
A set of codeword lengths $\{l_i\}$ for a uniquely decodable (in particular, prefix) binary code over $I$ symbols can exist **if and only if**
$$\sum_{i=1}^{I} 2^{-l_i} \le 1.$$
The "budget" $2^{-l_i}$ each codeword spends must not exceed 1. It both constrains what length profiles are achievable and, conversely, guarantees a prefix code exists for any lengths satisfying it.

## Why it matters
Combined with Gibbs' inequality, Kraft yields the lower bound on expected codeword length: $\mathbb{E}[l] \ge H(X)$ — no uniquely decodable code beats entropy. Setting $l_i = \lceil \log_2 1/p_i \rceil$ (Shannon information content, rounded up) satisfies Kraft and gets within 1 bit of $H$. It is the structural prerequisite behind Huffman coding's optimality.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[huffman-coding]] — prerequisite-of: Kraft guarantees prefix codes exist for valid length sets; underlies optimality
[To be populated during integration]