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
id: pkis:concept:minimum-distance
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- perfect-codes
related_concepts: []
sources:
- mackay-itila-ch13
tags:
- coding-theory
- error-correction
- hamming-distance
- linear-codes
- binary-codes
title: Minimum Distance of a Code
understanding: 0
uses:
- weight-enumerator-function
---

## Definition
The **minimum distance** $d_{\min}$ (often just $d$) of a code is the smallest Hamming distance between any two of its codewords:
$$d_{\min} = \min_{\mathbf{x}\neq\mathbf{y}\in C} d_H(\mathbf{x},\mathbf{y}).$$
For a **linear** code this equals the minimum weight of any non-zero codeword, since distances are translation-invariant and $\mathbf{0}\in C$. The Hamming distance counts coordinates in which two binary vectors differ.

### Error-correcting power
A code with minimum distance $d$ can guarantee to correct any error pattern of weight up to
$$t = \left\lfloor \frac{d-1}{2} \right\rfloor,$$
because placing $t$-spheres around each codeword leaves them disjoint. The (7,4) Hamming code has $d=3$, hence $t=1$. A bounded-distance decoder returns the unique codeword within distance $t$, or fails.

### Asymptotic distance categories
For a family of codes of growing blocklength $N$ at fixed rate $R$: the distance is **good** if $d/N\to$ const $>0$, **bad** if $d/N\to 0$, and **very bad** if $d\to$ const.

### Why it matters
Distance is the classical figure of merit in coding theory, but MacKay's central caution is that *distance isn't everything*: bounded-distance decoders that only exploit $d_{\min}$ tolerate at most half the noise Shannon allows. Good codes (e.g. concatenated Hamming, LDPC) decode far beyond $t$. Under low noise, though, $d_{\min}$ still dominates the (tiny) error probability.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[weight-enumerator-function]] — uses: for a linear code d_min is the smallest weight w>0 with A(w)>0.
- [[perfect-codes]] — prerequisite-of: the t-error-correcting radius defining perfection is t=floor((d-1)/2).
[To be populated during integration]