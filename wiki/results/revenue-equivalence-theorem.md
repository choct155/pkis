---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- multi-agent-systems
- economics
id: pkis:result:revenue-equivalence-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
tags:
- auction-theory
- expected-revenue
- private-values
title: Revenue Equivalence Theorem
understanding: 0
---

## Definition
A central result of auction theory (Myerson 1981; Riley and Samuelson 1981): under mild conditions, any auction mechanism in which bidders have private values v_i known only to themselves (but drawn from a commonly known distribution) yields the *same expected revenue* to the seller. The practical implication is that auction formats — English, first-price sealed-bid, Vickrey, etc. — do not compete on expected revenue but on other qualities such as communication cost, simplicity, resistance to collusion, and incentives for entry. For instance, the Vickrey auction's expected revenue equals that of the English auction as the bid increment approaches zero.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]