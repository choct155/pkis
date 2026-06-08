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
id: pkis:technique:hamming-7-4-code
instantiates:
- linear-block-code
- perfect-codes
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch01
tags:
- linear-block-code
- error-correcting-codes
- parity-check
- generator-matrix
- channel-coding
title: (7,4) Hamming Code
understanding: 0
uses:
- syndrome-decoding
- binary-symmetric-channel
---

## Definition
A **linear block code** mapping $K=4$ source bits to $N=7$ transmitted bits at rate $R=4/7$. The first four bits equal the source bits; three **parity-check bits** make the parity within each of three intersecting circles even. As a linear operation $\mathbf{t}=\mathbf{G}^{\mathsf T}\mathbf{s}$ (mod 2) with generator matrix
$$\mathbf{G}^{\mathsf T}=\begin{pmatrix}\mathbf{I}_4\\ \mathbf{P}\end{pmatrix}.$$
Any two of the sixteen codewords differ in at least three bits (minimum distance $d=3$), so the code corrects **any single-bit error**.

The one-line intuition: spread four bits over seven so that every single flip leaves a unique fingerprint.

### Performance
A decoding error needs $\ge 2$ flips in a block, so block error $p_B\approx\binom{7}{2}f^2=21f^2$ and bit error $p_b\approx\tfrac{3}{7}p_B\approx 9f^2$ — same $O(f^2)$ scaling as $R_3$ but at rate $4/7$ instead of $1/3$.

### Why it matters
It is the archetypal linear block code: it shows redundancy can be added to *blocks* rather than single bits, beating repetition codes on the rate–error frontier, and it introduces generator/parity-check matrices that underpin all of coding theory.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[perfect-codes]] — instantiates: the (7,4) Hamming code is the smallest non-trivial perfect binary code.
- [[linear-block-code]] — instantiates: the (7,4) Hamming code is the canonical small linear block code with generator and parity-check matrices
- [[binary-symmetric-channel]] — uses: Hamming block/bit error rates are derived assuming a binary symmetric channel.
- [[syndrome-decoding]] — uses: The (7,4) Hamming code is optimally decoded by mapping each of seven non-zero syndromes to a single-bit flip.
[To be populated during integration]