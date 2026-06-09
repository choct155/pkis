---
aliases: []
also_type: []
applies:
- admissible-and-consistent-heuristics
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
- optimization
- knowledge-representation
id: pkis:technique:relaxed-problem-heuristics
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch03
tags:
- search
- heuristic-generation
- relaxation
- pattern-database
- landmarks
title: Heuristics from Relaxed Problems, Pattern Databases, and Landmarks
understanding: 0
---

## Definition
The principal methods for *inventing* admissible heuristics rather than hand-specifying them. (1) **Relaxed problem**: remove restrictions on the actions so the state-space graph becomes a supergraph of the original; the exact optimal cost of the relaxed problem is an admissible (and, being an exact cost, consistent) heuristic for the original. For the 8-puzzle, relaxing 'a tile can move from X to Y if X adjacent to Y and Y blank' yields Manhattan distance h2 (drop the blank condition) or misplaced-tiles h1 (drop both). Programs such as ABSOLVER generate such heuristics automatically from a formal problem definition. (2) **Subproblem / pattern databases**: store the exact solution cost of every configuration of a subset of components (e.g. tiles 1-4 plus blank); look-up gives an admissible h_DB. **Disjoint pattern databases** count only moves of the tiles in each subset so several databases can be *added* and still remain admissible, yielding speedups of 1000x-1,000,000x on sliding-tile puzzles. (3) **Landmarks**: precompute exact optimal costs C*(v,L) from every vertex to a few landmark vertices; the differential heuristic h_DH(n) = max_L |C*(n,L) - C*(goal,L)| is efficient and admissible, exploited by online route-finding services together with shortcuts and precomputed path costs. Heuristics can also be **learned** from solved instances via features and (e.g.) a linear combination, at the risk of inadmissibility.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[admissible-and-consistent-heuristics]] — applies: relaxation, pattern databases, and landmarks are methods for constructing admissible heuristics
[To be populated during integration]