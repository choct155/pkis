---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- knowledge-representation
- symbolic-subsymbolic
- optimization
id: pkis:framework:classical-planning-pddl
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch11
tags:
- planning
- pddl
- factored-representation
- action-schema
- strips
title: Classical Planning and PDDL
understanding: 0
---

## Definition
Classical planning is the task of finding a sequence of actions to accomplish a goal in a discrete, deterministic, static, fully observable environment. Its defining contribution is a *factored* representation language — PDDL, the Planning Domain Definition Language (Ghallab et al., 1998), descended from STRIPS (Fikes & Nilsson, 1971) and ADL (Pednault, 1986) — that expresses states as conjunctions of ground atomic fluents and actions as *action schemas* with parameterized preconditions and effects. A single schema (e.g. Fly(p,from,to)) compactly represents an entire family of ground actions, replacing the exponentially large explicit state spaces and ad hoc per-domain heuristics required by problem-solving search (Ch. 3) and propositional logical agents (Ch. 7). This factored structure is precisely what makes domain-independent heuristics derivable.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]