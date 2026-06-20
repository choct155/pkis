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
date_updated: '2026-06-20'
domain:
- optimization
- symbolic-subsymbolic
- knowledge-representation
extends:
- belief-state-planning
id: pkis:technique:execution-monitoring-replanning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch11
- gulli-agentic-design-patterns-ch06
- gulli-agentic-design-patterns-ch11
- gulli-agentic-design-patterns-ch12
- gulli-agentic-design-patterns-ch19
tags:
- planning
- replanning
- execution-monitoring
- online-planning
- action-monitoring
- plan-monitoring
title: Execution Monitoring and Replanning
understanding: 0
uses:
- partial-order-planning
---

## Definition
Online planning interleaves planning and acting: an agent executes a plan while *monitoring* the world, and *replans* — splicing in repair sequences — when reality diverges from expectation. Replanning is needed because of nondeterministic actions, exogenous events, or incorrect models (missing preconditions, effects, or fluents). Three monitoring levels: *action monitoring* (verify each action's preconditions still hold before executing it), *plan monitoring* (verify the entire remaining plan will still succeed, cutting off doomed plans early and allowing serendipitous success), and *goal monitoring* (check whether better goals are available). On detecting divergence from expected state E to observed state O, the agent finds a recovery point P on the original plan and minimizes total cost of repair (O→P) plus continuation (P→G).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[partial-order-planning]] — uses: plan monitoring leverages partial-order causal-link structures
- [[belief-state-planning]] — extends: online complement that repairs contingent plans at execution time
[To be populated during integration]