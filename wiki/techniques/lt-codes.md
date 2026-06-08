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
id: pkis:technique:lt-codes
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch50
tags:
- fountain-codes
- luby-transform
- generator-matrix-code
- xor
- degree-distribution
- sparse-graph-codes
title: LT Codes (Luby Transform)
understanding: 0
---

## Definition
**LT codes** (Luby Transform, Luby 1998) are the first practical realization of a fountain code. Each encoded packet $t_n$ is generated independently:

$$d_n \sim \rho(d), \qquad t_n = \bigoplus_{k \in \mathcal{N}_n} s_k,$$

where a degree $d_n$ is drawn from a **degree distribution** $\rho(d)$, then $d_n$ source packets are chosen uniformly at random and XOR-ed (bitwise sum mod 2). This defines a bipartite graph between encoded ('check') nodes and source packets; when the mean degree $\bar d \ll K$ the graph is sparse, so the code is an **irregular low-density generator-matrix code** with $\mathbf{t} = G\mathbf{s}$.

The decoder must learn each packet's degree and neighbours. This is shipped cheaply: a 32-bit random **key** $\kappa_n$ in the packet header seeds a pseudo-random generator that reproduces the degree and connections, or synchronized clocks supply a shared seed — negligible overhead when $l \gg 32$.

### Performance
With probability $1-\delta$, $K$ packets are communicated at average encoding *and* decoding cost $O(K \ln(K/\delta))$, with overhead $K' - K$ of order $\sqrt{K}\,(\ln(K/\delta))^2$.

### Why it matters
LT codes turned the abstract fountain ideal into a deployable, linear-cost erasure code, founding Digital Fountain and seeding **raptor codes** (Shokrollahi 2003), an LT extension with strictly linear-time encode/decode that works at *all* blocklengths, not only large $K$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]