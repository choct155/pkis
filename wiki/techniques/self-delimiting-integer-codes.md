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
- huffman-coding
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:technique:self-delimiting-integer-codes
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- universal-codes
related_concepts: []
sources:
- mackay-itila-ch07
tags:
- source-coding
- prefix-codes
- integer-coding
- elias-codes
- kraft-inequality
title: Self-Delimiting Codes for Integers
understanding: 0
uses:
- kraft-inequality
---

## Definition
A **self-delimiting** (prefix) code for a positive integer $n$ first communicates the *length* of $n$'s binary representation and then the integer itself, so a decoder knows when the codeword ends without external length information. The standard binary code $c_b(n)$ alone is *not* uniquely decodeable (e.g. $c_b(5)c_b(5)=101101=c_b(45)$); the fix is to prepend self-describing length information.

Writing $l_b(n)$ for the standard binary length and $c_B(n)$ for the *headless* representation (binary with the leading 1 stripped), MacKay's family is built by recursion:
$$c_\alpha(n)=c_U[l_b(n)]\,c_B(n),\qquad c_\beta(n)=c_\alpha[l_b(n)]\,c_B(n),\dots$$
where $c_U$ is the unary code. $c_\alpha$ has length $2l_b(n)-1$; each successive code encodes the length more compactly.

### Implicit prior
Every complete code implies a prior. For $c_\alpha$ the prior factors into $P(l)=2^{-l}$ over lengths and a uniform $P(n\mid l)$ over integers of that length. The $c_\alpha$ header costs as many bits as the body, doubling file size — motivating $c_\beta,c_\gamma,\dots$.

### Why it matters
Self-delimiting codes solve lossless coding when the integer's magnitude is unknown a priori — file sizes, run lengths, symbol indices. They are the constructive route from 'a length profile satisfying Kraft' to an actually decodeable stream, and the stepping stone to genuinely universal integer codes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[huffman-coding]] — contrasts-with: Huffman builds an optimal code from a known finite distribution; self-delimiting integer codes target an unbounded distribution over the positive integers.
- [[universal-codes]] — prerequisite-of: Universal integer codes are constructed from and compared against the self-delimiting family.
- [[kraft-inequality]] — uses: Self-delimiting codes are prefix codes; their length profiles must satisfy Kraft.
[To be populated during integration]