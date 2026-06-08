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
id: pkis:technique:peeling-decoder
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch50
tags:
- erasure-channel
- message-passing
- lt-codes
- sparse-graph-codes
- degree-one
- sum-product
title: Peeling Decoder for Erasure Codes
understanding: 0
---

## Definition
The **peeling decoder** recovers $\mathbf{s}$ from $\mathbf{t} = G\mathbf{s}$ on an erasure channel by repeatedly resolving any check node of degree one. It is the **sum–product algorithm** specialized to the erasure case, where every message is *either* fully certain (a packet's value is known with probability one) *or* fully uncertain — there are no soft probabilities, so the algorithm reduces to bookkeeping on the graph.

Calling encoded packets *check nodes* $\{t_n\}$:

1. Find a check $t_n$ connected to exactly one source packet $s_k$. *(If none exists, the decoder halts and fails.)*
   - (a) Set $s_k := t_n$.
   - (b) For every other check $t_{n'}$ touching $s_k$, update $t_{n'} := t_{n'} + s_k$ (mod 2).
   - (c) Remove all edges incident to $s_k$.
2. Repeat until all $s_k$ are determined.

Resolving one source packet reduces neighbouring check degrees, ideally exposing a fresh degree-one check — a chain reaction that 'peels' the graph apart.

### Suboptimality
The peeling decoder is **not** optimal: it can give up even when the received packets jointly contain enough information to solve $G\mathbf{s}=\mathbf{t}$ by Gaussian elimination. The optimal (matrix-inversion) decoder needs only $K' = K + \Delta$ packets to fail with probability $\approx 2^{-\Delta}$, but costs more. Peeling trades a small overhead for near-linear $O(K\ln K)$ time.

### Why it matters
This degree-one chain reaction is the engine that gives LT/fountain codes their linear-time decoding, and the soliton degree distribution exists precisely to keep the supply of degree-one checks alive throughout peeling.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]