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
- knowledge-representation
- symbolic-subsymbolic
- optimization
id: pkis:concept:angelic-semantics-hla
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch11
tags:
- planning
- htn
- angelic-semantics
- reachable-set
- downward-refinement
- abstract-plan
title: Angelic Semantics for High-Level Actions
understanding: 0
---

## Definition
Angelic semantics gives precondition–effect descriptions to high-level actions so that a high-level plan can be proven to achieve a goal *without* refining it to primitives — the holy grail of hierarchical planning. The central object is the *reachable set* REACH(s,h): the set of states reachable by any implementation of HLA h from s. Because the agent (angelically) chooses which implementation to execute, a high-level plan achieves the goal iff its reachable set *intersects* the goal (contrast the *demonic* semantics, where an adversary chooses, requiring every reachable state to be a goal). An HLA can have nine effects on a fluent (notated with +e, -e, ±e for 'possibly add/delete'), since it can control the value depending on the implementation chosen. Because reachable sets can be arbitrarily 'wiggly,' optimistic REACH+ (overstates) and pessimistic REACH- (understates) approximations are used, with REACH- ⊆ REACH ⊆ REACH+.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]