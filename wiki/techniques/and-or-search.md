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
- search-and-planning
id: pkis:technique:and-or-search
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- belief-state-search
related_concepts: []
sources:
- russell-norvig-aima-ch04
tags:
- and-or-search
- nondeterminism
- conditional-plan
- contingency-plan
- AND-OR-tree
- cyclic-solutions
- AO-star
title: AND-OR Search
understanding: 0
---

## Definition
A search method for nondeterministic environments where, instead of a single RESULT(s,a) outcome, actions have a RESULTS(s,a) set of possible outcomes, so a solution is no longer a sequence but a conditional plan (contingency plan / strategy) that branches on what the agent observes. The search tree alternates two kinds of nodes: OR nodes, where the agent chooses among its own actions, and AND nodes, where the environment chooses among the action's possible outcomes and every outcome must be handled—yielding an AND-OR tree. A solution is a subtree that (1) has a goal at every leaf, (2) specifies one action at each OR node, and (3) includes every outcome branch at each AND node; it corresponds to an if-then-else plan. The canonical algorithm is a recursive depth-first search alternating OR-SEARCH and AND-SEARCH; cycle handling (returning failure when the current state repeats one on the path to the root) guarantees termination in finite spaces and discards redundant cyclic incarnations. When no acyclic solution exists (e.g. a 'slippery' vacuum world where motion sometimes fails), a cyclic plan—expressed with a while/label construct, such as 'keep trying Right until it works'—can still be a solution, provided every leaf is a goal reachable from every point and the nondeterminism is genuinely random rather than a fixed unobserved fault. AND-OR graphs admit breadth-first or best-first exploration; admissibility carries over to contingent-cost heuristics, and AO* is the optimal-solution analog of A*. The same algorithm applies directly to belief-state problems to solve general partially observable problems.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[belief-state-search]] — prerequisite-of: The AND-OR contingent-plan machinery underlies belief-state conditional plans.
[To be populated during integration]