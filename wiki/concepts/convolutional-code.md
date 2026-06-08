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
id: pkis:concept:convolutional-code
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch48
tags:
- error-correcting-codes
- shift-register
- trellis
- linear-codes
- convolutional-codes
title: Convolutional Code
understanding: 0
---

## Definition
A **convolutional code** generates a transmission $\mathbf{t}$ from a source stream $\mathbf{s}$ by passing the source through a *linear filter* built from a shift register, linear output taps, and possibly linear feedback. With a register of $k$ memory bits (the **constraint length**), each clock cycle ingests one source bit and emits, say, two output bits, giving rate $1/2$. An output bit is a mod-2 dot product between the state vector $\mathbf{z}=(z_k,\dots,z_0)$ and a binary **tap vector** $\mathbf{g}$ (compactly written in octal), $t^{(b)}=\sum_\kappa g^{(b)}_\kappa z_\kappa \bmod 2$.

### Three flavours
- **Systematic nonrecursive**: no feedback, and one output equals the source bit ($t^{(a)}=s$).
- **Nonsystematic nonrecursive**: no feedback, both outputs are tap functions; can have superior error-correction at fixed constraint length.
- **Systematic recursive**: feedback feeds a linear combination of taps back into the register; denoted by an octal ratio such as $(247/371)_8$.

### Recursive vs nonrecursive
A nonrecursive encoder has a **finite impulse response** (a lone source $1$ produces finitely many output $1$s), whereas a recursive encoder has an **infinite, periodic impulse response** of period up to $2^k-1$. A systematic recursive code and a nonsystematic nonrecursive code with the same taps are **code-equivalent** — they define identical codeword sets — yet the encoders behave differently, a distinction that matters for turbo codes.

### Why it matters
Convolutional codes admit an efficient trellis description, so optimal decoding reduces to the min–sum (Viterbi) and sum–product (forward–backward/BCJR) algorithms. They are the constituent building blocks of turbo codes and, viewed as block codes, have low-density parity-check matrices.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]