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
id: pkis:concept:code-goodness-taxonomy
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch11
tags:
- coding-theory
- shannon-limit
- very-good-codes
- practical-codes
- mackay
title: Code Goodness Taxonomy
understanding: 0
---

## Definition
MacKay classifies families of error-correcting codes along two independent axes — *how close to capacity* they can get, and *whether they are computationally feasible*:

- **Very good codes** achieve arbitrarily small error at *any* rate up to the channel capacity $C$.
- **Good codes** achieve arbitrarily small error at some non-zero rate, but only up to a maximum that may be below $C$.
- **Bad codes** cannot achieve arbitrarily small error except by driving the rate to zero — e.g. repetition codes.
- **Practical codes** can be encoded *and* decoded in time/space polynomial (ideally linear) in the blocklength $N$.

### The constructive gap
Shannon's proof shows nearly all block codes are very good, but it is non-constructive and requires exponential look-up tables. Writing an explicit code that is both very good *and* practical was long open: "the Shannon limit is not achieved in practice." The best modern answers — turbo codes and Gallager's LDPC codes — use large blocklengths, semi-random constructions, and probability-based (message-passing) decoders.

### Why it matters
This taxonomy frames the central engineering problem of coding theory: existence (Shannon) versus constructibility. It sets the benchmark — distance from the Shannon limit — against which every practical code is judged.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]