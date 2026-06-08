---
aliases: []
also_type: []
applies:
- binary-erasure-channel
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
id: pkis:concept:fountain-codes
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch50
tags:
- erasure-channel
- rateless-codes
- sparse-graph-codes
- luby
- broadcast
- no-feedback
title: Fountain Codes (Rateless Erasure Codes)
understanding: 0
uses:
- noisy-channel-coding-theorem
---

## Definition
A **fountain code** is a *rateless* erasure-correcting code: from a source file of $K$ packets it produces a potentially limitless stream of encoded packets ('drops'), and the original file can be reconstructed from **any** $K' \approx K$ drops collected, independent of *which* drops arrive. The metaphor is a fountain — a receiver simply holds a bucket under it until slightly more than $K$ drops accumulate, then decodes. In practice the overhead is small, $K' \approx 1.05\,K$.

Fountain codes resolve the central weakness of classical block codes (e.g. Reed–Solomon): a block code fixes its rate $R = K/N$ *before* transmission, so the sender must guess the erasure probability $f$, and there is no on-the-fly way to lower the rate if too few packets arrive. Being rateless, a fountain emits exactly as many drops as the channel demands, with **no feedback channel** required — Shannon already guarantees feedback adds no capacity, $C = (1-f)l$ bits per packet.

### Why it matters
Fountain codes are the *best known* codes for the erasure channel, and the practical payoff is largest on **broadcast** and **storage**: a single satellite stream serves thousands of receivers that each lose a *different* random subset of packets, with no redundant retransmissions; a backup can be sprayed across many unreliable disks and recovered from any-$K'$ surviving drops. Luby calls them **universal**: simultaneously near-optimal for *every* erasure rate, with encode/decode cost only $O(K \ln(K/\delta))$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[noisy-channel-coding-theorem]] — uses: Shannon's theorem justifies discarding feedback: erasure-channel capacity (1-f)l is unchanged by a feedback channel.
- [[binary-erasure-channel]] — applies: Fountain codes are erasure-correcting codes for the (q-ary) erasure channel.
[To be populated during integration]