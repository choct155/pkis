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
- search-and-planning
- reinforcement-learning
id: pkis:concept:online-search-agents
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch04
tags:
- online-search
- exploration
- unknown-environment
- competitive-ratio
- interleaved-planning-acting
- dead-ends
- safely-explorable
title: Online Search Agents
understanding: 0
---

## Definition
Search agents that interleave computation, sensing, and acting—taking an action, observing the result, then computing the next action—rather than computing a complete solution offline before acting. Online search is essential in unknown environments, where the agent does not know what states exist or what its actions do and must use actions as experiments to learn the transition model (it cannot compute RESULT(s,a) except by being in s and doing a). It is also advantageous in dynamic or semi-dynamic domains (where deliberation has a cost) and in nondeterministic domains (it can focus effort on contingencies that actually arise). The canonical instance is the mapping problem (a robot exploring an unknown building) and escaping labyrinths. Performance is measured by the competitive ratio: the agent's total path cost relative to the optimal cost if the space were known in advance; this can be made small only under conditions—no bounded ratio is achievable for general graphs, and none at all if paths can have unbounded cost. Online agents are vulnerable to dead ends (states from which no goal is reachable, especially with irreversible actions like cliffs or one-way streets); by an adversary argument, no algorithm can avoid all dead ends, so guarantees require safely explorable spaces (a goal reachable from every reachable state, as in mazes and 8-puzzles with reversible actions). Because they can expand only successors of the physically occupied state, online algorithms favor depth-first ordering (ONLINE-DFS-AGENT backtracks in the physical world and works only with reversible actions); a random walk eventually succeeds in finite safely-explorable spaces but can take exponentially many steps.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]