---
aliases: []
also_type: []
analogous-to:
- markov-decision-processes
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
- knowledge-representation
- symbolic-subsymbolic
- optimization
extends:
- classical-planning-pddl
id: pkis:technique:belief-state-planning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch11
tags:
- planning
- belief-state
- sensorless
- conformant
- contingent
- partial-observability
- percept-schema
title: Belief-State Planning (Sensorless, Conformant, and Contingent)
understanding: 0
uses:
- planning-heuristics-relaxation
---

## Definition
Belief-state planning extends classical planning to partially observable, nondeterministic, and unknown environments by searching in the space of *belief states* — sets of physical states the agent might be in — represented compactly as logical formulas rather than enumerated sets. Three regimes: *sensorless (conformant)* planning, which finds a plan that works with no observations (e.g. coercing a chair and table to match color by painting both from one can without knowing the color); *contingent* planning, which generates branching plans conditioned on percepts, modeled via PDDL *percept schemas*; and *online planning with replanning* for unknown environments. Sensorless planning uses the open-world assumption and a belief-state update b' = (b - DEL(a)) ∪ ADD(a) that keeps belief states in 1-CNF — but only for unconditional schemas; conditional effects induce inter-fluent dependencies that take belief states outside 1-CNF, potentially to exponential size.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[markov-decision-processes]] — analogous-to: belief-state machinery parallels POMDPs
- [[planning-heuristics-relaxation]] — uses: admissible-on-subset heuristics guide belief-state search
- [[classical-planning-pddl]] — extends: extends planning to partial observability and nondeterminism
[To be populated during integration]