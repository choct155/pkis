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
- reinforcement-learning
extends:
- hill-climbing
id: pkis:technique:lrta-star
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch04
specializes:
- online-search-agents
- reinforcement-learning
tags:
- LRTA-star
- real-time-search
- online-search
- optimism-under-uncertainty
- heuristic-update
- escaping-local-minima
title: Learning Real-Time A* (LRTA*)
understanding: 0
---

## Definition
An online search agent that augments hill climbing with memory rather than randomness, storing and updating a current best estimate H(s) of the cost to reach a goal from each visited state. H(s) is initialized to the heuristic estimate h(s) and refined with experience: the agent moves to the neighbor minimizing c(s,a,s') + H(s'), and when that move reveals the current estimate was too optimistic it raises H(s) accordingly, progressively 'flattening out' a flat local minimum until it escapes. A key design choice is optimism under uncertainty: untried actions in a state are assumed to lead immediately to the goal at the least possible cost h(s), which encourages exploration of new, possibly promising paths. Introduced by Korf (1990) for real-time search where the agent must act after a bounded amount of deliberation (common in two-player games), LRTA* is in fact a special case of reinforcement-learning algorithms for stochastic environments: its cost-estimate updates converge to exact values given proper exploration, after which pure hill climbing on the converged values is optimal. Its naive optimism can, in the uninformed case, yield exploration less efficient than plain depth-first search.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[reinforcement-learning]] — specializes: LRTA* is a special case of RL algorithms for stochastic environments (Barto et al. 1995).
- [[hill-climbing]] — extends: LRTA* augments hill climbing with a learned cost-to-go memory H(s) to escape local minima.
- [[online-search-agents]] — specializes: LRTA* is a specific online search agent that updates heuristic estimates from experience.
[To be populated during integration]