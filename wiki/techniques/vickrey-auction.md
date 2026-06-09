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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- multi-agent-systems
- economics
id: pkis:technique:vickrey-auction
instantiates:
- auction-theory
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
tags:
- second-price
- sealed-bid
- truthful
- dominant-strategy
title: Vickrey Auction
understanding: 0
---

## Definition
A sealed-bid auction in which the highest bidder wins but pays the *second-highest* bid b_o rather than their own. This single change makes truthful bidding (b_i = v_i) a dominant strategy: when v_i − b_o > 0 any winning bid is optimal and bidding v_i wins; when v_i − b_o < 0 any losing bid is optimal and bidding v_i loses — so v_i is optimal (and uniquely so) regardless of others. Because it requires minimal computation and communication and is incentive-compatible, the Vickrey auction is widely used in distributed AI and underlies variants powering trillions of online ad auctions per year. Its expected seller revenue equals the limit of the English auction as the increment goes to zero (a revenue-equivalence instance). Caveat: auctioning n goods via an (n+1)-price scheme is *not* truth-revealing.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[auction-theory]] — instantiates
[To be populated during integration]