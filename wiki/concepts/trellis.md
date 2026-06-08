---
aliases: []
also_type: []
applies:
- linear-block-code
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
- statistical-learning
id: pkis:concept:trellis
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- forward-backward-algorithm
- min-sum-algorithm
related_concepts: []
sources:
- mackay-itila-ch25
tags:
- trellis
- error-correcting-codes
- graphical-models
- decoding
- linear-codes
- state-space
title: Trellis
understanding: 0
uses:
- syndrome-decoding
---

## Definition
A **trellis** is a directed graph that represents the codewords of a code as paths. Its nodes (**states**) are grouped into vertical **times** $0,1,\dots,N$; every edge connects a node at one time to a node at the next time and is labelled with a code symbol. The leftmost and rightmost times each contain a single node. A codeword of blocklength $N$ is read off by tracing any left-to-right path and emitting the edge symbol as one moves from time $n-1$ to time $n$; thus a trellis with $N+1$ times defines a code of blocklength $N$, and the valid paths are exactly the codewords.

The **width** at a time is the number of nodes there, and the **maximal width** governs decoding cost. A trellis is **linear** if the code it defines is linear; this note treats only (binary) linear trellises.

### Minimal trellises
The **minimal trellis** of a linear code has the fewest nodes. In it each node has at most two incoming and two outgoing edges, the width is everywhere a power of two, and the width never exceeds $\min(2^{K}, 2^{M})$ where $M=N-K$. The number of binary branch points crossed equals $K$. A trellis is built from a generator matrix in *trellis-oriented form* (row spans starting and ending in distinct columns), or from the parity-check matrix by tracking the **partial syndrome** $H\mathbf{r}$ as the state.

### Why it matters
The trellis exposes the conditional-independence (chain) structure of a code, turning brute-force $O(2^{K})$ decoding into message passing whose cost scales with the number of edges. It is the graphical scaffold on which the Viterbi (min-sum) and forward-backward (sum-product) algorithms run, linking coding theory to probabilistic graphical models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[syndrome-decoding]] — uses: A trellis can be built from the parity-check matrix using the partial syndrome as the state.
- [[linear-block-code]] — applies: A linear trellis is an alternative representation of a linear block code's codeword set.
- [[min-sum-algorithm]] — prerequisite-of: Viterbi/min-sum decoding finds the minimum-cost path across a code trellis.
- [[forward-backward-algorithm]] — prerequisite-of: The trellis is the graphical structure on which forward-backward message passing is run.
[To be populated during integration]

## Decoding on the trellis (min-sum and sum-product)
For a convolutional code, the trellis edge costs encode the channel likelihoods directly. On a binary symmetric channel with received vector equal to a codeword bar one flipped bit, each edge carries a likelihood cost: zero when both of its two code bits match the received bits, one when exactly one matches, and two when neither matches. The **min–sum (Viterbi) algorithm** finds the maximum-likelihood codeword as the minimum-cost path — the path using as many exact-match edges as possible — while the **sum–product (forward–backward / BCJR) algorithm** returns the posterior marginal of each bit. A defect of an unterminated trellis is *unequal protection*: the final source bits can be distinguished by very few transmitted bits, which motivates **trellis termination** — driving the $k$ memory bits back to zero with a few extra parity bits, at a small loss in rate.