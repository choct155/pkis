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
- computer-science
id: pkis:concept:one-way-hash-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch12
specializes:
- hash-function
tags:
- cryptography
- digital-signature
- tamper-detection
- collision-resistance
- mackay-itila
title: One-Way Hash Function
understanding: 0
uses:
- hash-collision-bound
---

## Definition
A **one-way hash function** is *easy to compute* but *hard to invert*: given a hash value, no feasible procedure finds a key (or a tampering) that produces it. This property upgrades a hash from noise-detection to defence against a deliberate **adversary**.

### Why linear hashes fail
Against a forger (Fiona) who modifies Alice's file, a *linear* hash such as a CRC is useless: she edits the file freely, then solves a small linear system to flip $\sim 32$ further bits that restore the original hash. Security demands a non-linear, hard-to-invert hash — e.g. **MD5** (128-bit). Finding good one-way hashes is an active cryptography research area.

### Two attack costs (and the birthday gap)
- **Second-preimage attack:** to match a *given* hash of $M$ bits, Fiona must try about $2^M$ files. So $M=32$ is far too small ($2^{32}$ trials are cheap).
- **Collision attack:** Alice, who authors *both* files (e.g. placing two bets for the price of one), need only find *any* pair with equal hashes. By the birthday bound, $N_1 N_2 2^{-M}$ expected collisions means she succeeds after hashing only $\sim 2^{M/2}$ files — the square root of Fiona's effort.

For a system to resist a cheater with $C=10^6$ computers over $T=10$ years at $t=1\,$ns per hash, one needs $M \gg 2\log_2(CT/t) \approx 160$ bits.

### Why it matters
The gulf between $2^M$ and $2^{M/2}$ shows why hash sizes for digital signatures and commitment schemes (secret publication, as used by Newton and Hooke) must be sized against the *collision* attack, not the preimage attack.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hash-collision-bound]] — uses: Collision-attack cost 2^{M/2} comes directly from the birthday-problem collision bound.
- [[hash-function]] — specializes: A one-way hash is a hash function with the added cryptographic property of being hard to invert.
[To be populated during integration]