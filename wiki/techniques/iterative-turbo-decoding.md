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
id: pkis:technique:iterative-turbo-decoding
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch48
tags:
- decoding
- turbo-codes
- message-passing
- sum-product
- forward-backward
title: Iterative Turbo Decoding
understanding: 0
---

## Definition
**Iterative (turbo) decoding** applies the sum–product algorithm to a turbo code's factor graph by alternating belief propagation between its two constituent trellises. On iteration one, each trellis receives the channel likelihoods and runs the **forward–backward algorithm** to compute, for every bit, the relative likelihood of $0$ versus $1$ given the other bits. These per-bit likelihoods are then **passed to the other trellis**, multiplied by the channel likelihoods on the way, and the forward–backward sweep is rerun. After roughly ten to twenty exchanges the decoder typically converges to the correct codeword.

### Stopping criterion
Rather than running a fixed number of iterations, one can halt adaptively: at each iteration, pick the locally most probable edge at every time-step in each trellis. If these edges join into two valid paths — one per trellis — that are mutually **consistent**, stop. This saves decoding time with no loss in error probability and, crucially, *detects* decoding failures: a block that never satisfies the criterion within the iteration cap can be flagged as definitely corrupted, and the distinction between detected and undetected errors exposes the low-weight codewords useful for code design.

### Why it matters
Iterative decoding is what makes turbo codes practical: exact joint decoding over the coupled trellises is intractable, but message passing between simple constituent decoders — each a tractable forward–backward pass — yields near-optimal performance at near-capacity rates. It is the prototypical example of the sum–product/belief-propagation paradigm applied to a loopy (cyclic) factor graph.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]