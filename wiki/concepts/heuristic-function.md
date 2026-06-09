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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- knowledge-representation
- deep-learning
id: pkis:concept:heuristic-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- a-star-search
related_concepts: []
sources:
- russell-norvig-aima-ch03
tags:
- search
- heuristic
- informed-search
- estimate
title: Heuristic Function
understanding: 0
---

## Definition
A function h(n) that gives the estimated cost of the cheapest path from the state at node n to a goal state, supplying the domain-specific 'hint' that distinguishes *informed* search from uninformed search. h(n) is required to be 0 at goal states. A classic example is the straight-line-distance heuristic h_SLD for route finding, which cannot be computed from the problem's ACTIONS and RESULT functions alone but requires extra world knowledge. Heuristic quality is measured by the **effective branching factor** b* (the branching factor a uniform tree of depth d would need to hold the N+1 nodes A* generated; a good heuristic has b* close to 1) or, following Korf and Reid, by the constant reduction k_h it produces in effective search depth, giving cost O(b^{d-k_h}). One heuristic h1 **dominates** another h2 if h1(n) >= h2(n) for all n (with both admissible), in which case h1 is never worse for A*. Heuristics can be invented by relaxing the problem, by pattern databases, by landmark precomputation, or by learning from solved instances.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[a-star-search]] — prerequisite-of: informed search presupposes the notion of a heuristic estimate
[To be populated during integration]