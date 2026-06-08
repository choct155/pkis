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
id: pkis:concept:runlength-limited-codes
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch17
tags:
- coding
- modulation-coding
- disk-drive
- constraints
- variable-length
- mackay
title: Runlength-Limited Codes
understanding: 0
---

## Definition
A **runlength-limited (RLL) channel** constrains the minimum and maximum number of consecutive identical symbols. Writing $(d,k)$-style bounds on runs of 0s and 1s, the unconstrained binary channel allows runs $1$ to $\infty$; channel A limits runs of 1s to length exactly 1; channel B forces every run to length $\ge2$; channel C caps every run at length $\le2$. An RLL *code* maps arbitrary source bits onto strings obeying these constraints.

Codes range from simple to optimal. The fixed rate-1/2 map $\{0\to00,\,1\to10\}$ trivially respects channel A. The variable-length $C_2=\{0\to0,\,1\to10\}$ has mean length $L=\tfrac32$, rate $2/3$. Feeding $C_2$ a *sparse* source of density $f$ gives rate
$$R(f)=\frac{H_2(f)}{1+f},$$
maximised at $f\approx0.38$ to give $\approx0.69$ bits — the capacity. So sparsification (e.g. an arithmetic decoder) plus $C_2$ approaches optimality.

### Why it matters
RLL codes are the workhorse of magnetic and optical storage: forbidding isolated domains (channel B) stabilises the medium, and bounding maximum runs (channel C) preserves clock synchronisation when the read rate is uncertain. They trade a little rate for physical robustness, and the constrained-channel capacity sets the price of that robustness.

### Fixed-length guarantees
When predictable block sizes matter (e.g. 512-byte disk blocks), one can pair two complementary codes — when one over-runs the other under-runs — and send the shorter, prefixed by one flag bit, bounding the encoded length near $N/C$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]