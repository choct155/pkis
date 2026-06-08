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
id: pkis:technique:concatenated-codes
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch11
tags:
- coding-theory
- concatenation
- interleaving
- burst-errors
- reed-solomon
- mackay
title: Concatenated Codes and Interleaving
understanding: 0
uses:
- linear-block-code
---

## Definition
**Concatenation** builds a practically-decodable code from two simpler ones. An encoder–channel–decoder triple $C\to Q\to D$ defines a **super-channel** $Q'$ with lower error rate (but correlated errors); an outer code $C'$/$D'$ is then designed for $Q'$. The composite (outer $C'$ then inner $C$) is the concatenated code, decoded conveniently — though sub-optimally — by running each constituent decoder in sequence, lowest-rate code first.

### Interleaving
**Interleaving** reorders bits so that nearby bits of one code are separated before entering the next code. This spreads any burst the inner code produces across many outer codewords, letting the decoder treat the errors as independent. A rectangular **product code** ($K_2\times K_1$ block encoded horizontally then vertically) is the simplest interleaver.

### Why it matters
Concatenation + interleaving is how real systems beat **burst-error** channels: concatenated Reed–Solomon codes on compact discs correct bursts up to 4000 bits, and a convolutional inner / Reed–Solomon outer concatenation flew on Voyager. The construction also presaged turbo codes, whose iterative decoding is a message-passing (sum–product) algorithm. (MacKay notes interleaving is theoretically wasteful in redundancy, since it discards the useful correlation structure of bursts.)

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[linear-block-code]] — uses: concatenation composes linear inner and outer codes into a practically-decodable code
[To be populated during integration]