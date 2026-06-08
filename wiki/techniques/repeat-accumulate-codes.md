---
aliases: []
also_type: []
analogous-to:
- concatenated-codes
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
id: pkis:technique:repeat-accumulate-codes
instantiates:
- linear-block-code
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch49
tags:
- sparse-graph-codes
- error-correction
- factor-graph
- turbo-like-codes
- accumulator
- channel-coding
title: Repeat-Accumulate Codes
understanding: 0
uses:
- factor-graph
- sum-product-algorithm
- trellis
- forward-backward-algorithm
- repetition-codes
---

## Definition
A **repeat-accumulate (RA) code** is an extremely simple sparse-graph code whose encoder is built from three trivial operations. Starting from $K$ source bits $s_1\ldots s_K$:

1. **Repeat** each source bit $q$ times (e.g. $q=3$), giving $N=qK$ bits.
2. **Permute** the repeated bits with a fixed random permutation, yielding $\mathbf{u}=u_1\ldots u_N$.
3. **Accumulate** (run a mod-2 running sum) to produce the transmitted stream:
$$t_1 = u_1,\qquad t_n = t_{n-1} + u_n \pmod 2.$$

That is the entire encoder. Introduced by Divsalar, Jin, and McEliece (1998) as turbo-like codes simple enough to analyze, RA codes turned out to perform as well as messier turbo and Gallager codes in practice.

### The factor graph
The code's prior over codewords is a factor graph with two factor types: **equality constraints** $\mathbb{1}[x_1=x_2=x_3]$ enforcing the repetition, and **parity constraints** $\mathbb{1}[\sum x = 0 \bmod 2]$ enforcing the accumulation. The accumulator is naturally represented as a **trellis**.

### Decoding
RA codes are decoded with the **sum-product algorithm** on this graph. Each iteration has two halves: the accumulator trellis runs the **forward-backward algorithm** to produce per-variable likelihoods, then the equality nodes multiply incoming messages and pass new likelihoods back to the trellis. The *stop-when-it's-done* rule distinguishes detected failures (decoder stuck) from undetected errors (low-weight codewords).

### Why it matters
RA codes demonstrate that near-Shannon-limit performance does not require elaborate constructions: a repetition, a random permutation, and a running sum suffice. They are pedagogically central as the simplest member of the sparse-graph code family and are equivalent to staircase codes.

### Power-law decoding times
The number of sum-product iterations $\tau$ needed to decode is random, with a heavy-tailed distribution $P(\tau)\propto\tau^{-p}$; the exponent $p$ shrinks (heavier tail) as SNR decreases.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[concatenated-codes]] — analogous-to: RA codes are turbo-like, serial-concatenation-style constructions of a repeater and an accumulator
- [[repetition-codes]] — uses: the first encoding step repeats each source bit q times, the repetition-code building block
- [[linear-block-code]] — instantiates: an RA code is a linear code; its valid words satisfy a (generalized) linear parity-check system
- [[forward-backward-algorithm]] — uses: the accumulator trellis runs forward-backward to produce per-variable likelihoods each iteration
- [[trellis]] — uses: the accumulator is represented as a trellis for the forward-backward sub-routine
- [[sum-product-algorithm]] — uses: RA codes are decoded by sum-product message passing on the factor graph
- [[factor-graph]] — uses: the RA code's prior over codewords is a factor graph with equality and parity factor nodes
[To be populated during integration]