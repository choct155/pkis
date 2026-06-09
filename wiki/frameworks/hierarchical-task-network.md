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
extends:
- classical-planning-pddl
id: pkis:framework:hierarchical-task-network
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch11
tags:
- planning
- htn
- hierarchical-decomposition
- high-level-action
- refinement
- abstraction
title: Hierarchical Task Network (HTN) Planning
understanding: 0
---

## Definition
Hierarchical task network (HTN) planning manages complexity by planning at multiple levels of abstraction. Its key construct is the *high-level action* (HLA) — e.g. Go(Home,SFO) — which has one or more *refinements* into sequences of actions that may themselves be HLAs or primitive actions; a refinement containing only primitives is an *implementation*. A high-level plan achieves a goal if *at least one* of its implementations does (the agent chooses the implementation, unlike nondeterministic planning where nature chooses). Planning proceeds by repeatedly replacing an HLA in the current plan with one of its refinements until the plan is primitive and achieves the goal. The HLA library encodes domain knowledge about how things are done; with a regular refinement structure (each nonprimitive action has r refinements of k steps), the number of decomposition trees is r^((d-1)/(k-1)), giving exponential savings (effectively the k-th root of nonhierarchical cost) when refinements are few and long.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[classical-planning-pddl]] — extends: adds high-level actions and refinement hierarchy
[To be populated during integration]