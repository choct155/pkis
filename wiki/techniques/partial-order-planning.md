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
contrasts-with:
- forward-state-space-planning
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- symbolic-subsymbolic
- knowledge-representation
id: pkis:technique:partial-order-planning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch11
tags:
- planning
- partial-order
- plan-space-search
- least-commitment
- causal-link
title: Partial-Order Planning
understanding: 0
uses:
- classical-planning-pddl
---

## Definition
Partial-order planning represents a plan as a graph rather than a strictly linear sequence: each action is a node, and for each precondition there is an edge from an earlier action (or the initial state) that establishes it. The planner searches in the *space of plans*, inserting actions to satisfy open conditions and adding ordering constraints only when needed (least commitment), leaving independent actions unordered. Dominant in research from the 1980s–1990s for handling independent subproblems, it was overtaken around 2000 by forward-search planners with strong heuristics and by SATPLAN benefiting from Moore's-law memory growth, and is no longer competitive on fully automated classical planning. It remains the technology of choice for operations scheduling, for human-inspectable plans (spacecraft and Mars-rover operations), and underlies plan-monitoring bookkeeping.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[forward-state-space-planning]] — contrasts-with: plan-space vs world-state search; eclipsed on automated classical planning
- [[classical-planning-pddl]] — uses: searches plan space over PDDL actions
[To be populated during integration]