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
id: pkis:technique:elias-omega-code
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch07
tags:
- source-coding
- integer-coding
- universal-codes
- elias-codes
- prefix-codes
title: Elias's Universal Code for Integers (C_omega)
understanding: 0
---

## Definition
**Elias's $C_\omega$** is a recursive prefix code for positive integers that 'transcends' the self-delimiting sequence $C_\alpha, C_\beta,\dots$ by effectively choosing the right depth of length-encoding automatically. It sends a chain of messages, each encoding the length of the next, using a single trailing bit to mark where the recursion stops; because every positive integer's binary form begins with '1', those leading 1s are omitted.

### Encoder
Built right-to-left: write '0'; then loop — if $\lfloor\log_2 n\rfloor=0$ halt, else prepend $c_b(n)$ and set $n:=\lfloor\log_2 n\rfloor$. Each pass prepends the binary representation of the current value, so the decoder reads successive length headers until the terminating bit.

### Universality and limits
$C_\omega$ is a *universal* code: its average length stays within a constant factor of optimal for any monotonically decreasing, finite-entropy prior over $n$. It is **not** optimal for priors that expect very large integers — one can construct a code that beats it beyond some threshold.

### Why it matters
$C_\omega$ shows you can encode integers near-optimally *without* committing to a specific prior, the central appeal of universal coding. It is the canonical example of a code that adapts its overhead to the integer's magnitude.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]