---
aliases: []
also_type: []
applies:
- curse-of-dimensionality
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
id: pkis:technique:tile-coding
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch09
specializes:
- coarse-coding
tags:
- coarse-coding
- feature-construction
- binary-features
- hashing
- cmac
title: Tile Coding
understanding: 0
uses:
- hash-function
---

## Definition
A computationally efficient form of coarse coding for multi-dimensional continuous spaces (Albus 1971; a.k.a. CMAC). The receptive fields are grouped into multiple tilings—non-overlapping partitions of the space—each offset from the others by a fraction of a tile width; a state activates exactly one tile per tiling, so the number of active (binary) features equals the number of tilings, regardless of state. This constant active-feature count makes step-size selection intuitive: α = 1/n (n tilings) gives one-trial learning, and α = 1/(10n) moves a tenth of the way to the target per update. Binary features make the inner-product value computation nearly free (sum the n active weights). Generalization is governed by how tilings are offset; asymmetric offsets (displacement vectors of the first odd integers (1,3,5,…,2k−1), with n a power of 2 ≥ 4k) avoid the diagonal artifacts of uniform offsets. Hashing—pseudo-random collapsing of a large tiling into fewer tiles—slashes memory with little performance loss and frees tile coding from the curse of dimensionality.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[curse-of-dimensionality]] — applies: hashed tile coding makes memory match task demands rather than scaling exponentially in dimension
- [[hash-function]] — uses: hashing pseudo-randomly collapses large tilings into fewer tiles to cut memory
- [[coarse-coding]] — specializes: tile coding is coarse coding with multiple offset partition tilings
[To be populated during integration]