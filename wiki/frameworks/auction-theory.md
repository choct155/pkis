---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- multi-agent-systems
- economics
id: pkis:framework:auction-theory
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
specializes:
- mechanism-design
tags:
- resource-allocation
- bidding
- private-value
- common-value
- collusion
title: Auction Theory
understanding: 0
---

## Definition
The study of auction mechanisms for allocating scarce resources among bidders, a central application of mechanism design. Each bidder i has a value v_i, which may be a *private value* (idiosyncratic taste) or a *common value* (the item's true worth is the same but uncertain and estimated differently). Auction designs differ on efficiency (do goods go to the highest-valuer?), revenue, communication cost, and resistance to collusion. Major formats: ascending-bid (English) — efficient with a simple dominant strategy but high communication and vulnerable to discouraging competition; first-price sealed-bid — low communication but no simple dominant strategy and bids depend on beliefs about others; and the Vickrey (second-price sealed-bid) auction. The revenue equivalence theorem shows many formats yield the same expected revenue, so they compete on other qualities.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mechanism-design]] — specializes
[To be populated during integration]