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
id: pkis:concept:weight-enumerator-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch13
tags:
- coding-theory
- linear-codes
- distance-distribution
- random-codes
- union-bound
title: Weight Enumerator Function
understanding: 0
---

## Definition
The **weight enumerator** $A(w)$ of a code is the number of codewords of Hamming weight $w$:
$$A(w) = \#\{\mathbf{x}\in C : |\mathbf{x}| = w\}.$$
For a linear code this also captures the *distance distribution*, since the multiset of distances from any codeword equals the multiset of codeword weights. The minimum distance is the smallest $w>0$ with $A(w)>0$.

### Expected enumerator of a random linear code
Averaging over linear codes defined by a random $M\times N$ parity-check matrix, the probability that a given weight-$w$ word satisfies $\mathbf{Hx}=\mathbf{0}$ is $2^{-M}$ (each of $M$ syndrome bits is an independent fair coin), so
$$\langle A(w)\rangle = \binom{N}{w} 2^{-M}, \qquad w>0.$$
This crosses $1$ near $H_2(w/N) = 1-R$, locating the typical minimum distance (the Gilbert--Varshamov distance).

### Bounding error probability
Via a **union bound**, the block-error probability on a binary symmetric channel is bounded by the enumerator weighted by the Bhattacharyya parameter $\beta(f)=2\sqrt{f(1-f)}$:
$$P(\text{block error}) \le \sum_{w>0} A(w)\,[\beta(f)]^{w}.$$

### Why it matters
The *whole* weight enumerator -- not just $d_{\min}$ -- governs whether a code is good. MacKay's "blind bat" picture explains why: at higher noise, errors are dominated by the many medium-weight codewords, not the rare minimum-weight ones.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]