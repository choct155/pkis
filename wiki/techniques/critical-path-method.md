---
aliases: []
also_type: []
analogous-to:
- backward-regression-planning
applies:
- job-shop-scheduling
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
id: pkis:technique:critical-path-method
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch11
tags:
- scheduling
- critical-path
- makespan
- slack
- dynamic-programming
- earliest-latest-start
title: Critical Path Method (CPM)
understanding: 0
---

## Definition
The critical path method computes a minimum-makespan schedule for a partially ordered set of timed actions *ignoring resource constraints*. Viewing the partial-order plan as a directed graph from Start to Finish, the *critical path* is the path of longest total duration: it determines the whole plan's duration, and delaying any action on it delays the entire plan, whereas off-critical actions have a *slack* window. For each action CPM computes an earliest start ES and latest start LS (slack = LS - ES) via a forward/backward dynamic program: ES(Start)=0, ES(B)=max over predecessors A of ES(A)+Duration(A); LS(Finish)=ES(Finish), LS(A)=min over successors B of LS(B)-Duration(A). The algorithm runs in O(Nb) for N actions and branching factor b.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[backward-regression-planning]] — analogous-to: shares a forward/backward dynamic-programming propagation structure
- [[job-shop-scheduling]] — applies: solves the temporal (resource-free) core of scheduling
[To be populated during integration]