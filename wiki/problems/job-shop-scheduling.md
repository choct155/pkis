---
aliases: []
also_type: []
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-20'
domain:
- optimization
- symbolic-subsymbolic
extends:
- classical-planning-pddl
id: pkis:problem:job-shop-scheduling
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch11
- gulli-agentic-design-patterns-ch16
tags:
- scheduling
- resources
- makespan
- job-shop
- aggregation
- plan-first-schedule-later
title: Job-Shop Scheduling with Resource Constraints
understanding: 0
---

## Definition
Whereas classical planning says what to do and in what order, *scheduling* adds time: how long each action takes and when it occurs. A job-shop scheduling problem is a set of jobs, each a collection of actions with ordering constraints; each action has a duration and resource requirements specifying a resource type, quantity, and whether the resource is *consumable* (e.g. lug nuts) or *reusable* (e.g. an inspector, borrowed at action start and released at end). A solution assigns start times satisfying all ordering and resource constraints; cost is commonly the *makespan* (total plan duration). The standard approach is 'plan first, schedule later': select actions with ordering constraints, then add temporal information to meet resource and deadline constraints. Resources are represented by *aggregation* — numeric quantities (e.g. Inspectors(2)) rather than named individuals — which is essential for complexity (avoiding 9! futile inspector-assignment trials when 10 inspections need 9 inspectors).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[classical-planning-pddl]] — extends: adds time, durations, and resource constraints to planning
[To be populated during integration]