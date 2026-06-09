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
- optimization
- search-and-planning
id: pkis:concept:local-search
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch04
tags:
- local-search
- optimization
- state-space-landscape
- metaheuristics
- complete-state-formulation
title: Local Search
understanding: 0
---

## Definition
A family of search methods that operate from a single current state (or a small set of states), moving to neighboring states without tracking the paths taken or the set of states reached. Because they do not retain paths, local search algorithms are not systematic—they may never explore a region of the space where a solution lies—but they have two decisive advantages: they use very little memory (typically constant in the size of the state space), and they can find reasonable solutions in very large or infinite state spaces where systematic algorithms are infeasible. Local search is naturally suited to optimization problems, where the goal is to find a state that maximizes (or minimizes) an objective function, and the path to that state is irrelevant—as in the 8-queens problem, integrated-circuit design, factory floor layout, job-shop scheduling, and portfolio management. The central conceptual device is the state-space landscape: each state is a point with an 'elevation' given by the objective function, and the task is to find the highest peak (a global maximum) or, dually, the lowest valley (a global minimum). The defining obstacles—local maxima, ridges, and plateaus—are properties of this landscape, and the differences among local search algorithms (hill climbing, simulated annealing, beam search, evolutionary methods) lie in how they trade exploitation of the current gradient against random exploration to escape these traps.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]