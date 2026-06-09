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
- optimization
- knowledge-representation
- deep-learning
id: pkis:framework:state-space-search
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch03
tags:
- search
- problem-solving
- planning
- classical-ai
title: State-Space Search
understanding: 0
---

## Definition
The foundational framework for goal-directed problem solving in which a problem-solving agent finds a sequence of actions (a solution) leading from an initial state to a goal state. A search problem is defined formally by five parts: (1) a set of possible **states** (the *state space*); (2) an **initial state**; (3) a set of one or more **goal states** (tested by IS-GOAL); (4) the **actions** ACTIONS(s) applicable in each state; (5) a **transition model** RESULT(s,a) and an additive, positive **action-cost function** c(s,a,s'). A *path* is a sequence of actions; a *solution* is a path from the initial state to a goal; an *optimal solution* has lowest path cost. The state space is a directed **graph** (states = vertices, actions = edges). Search algorithms superimpose a **search tree** over this graph, each node storing STATE, PARENT, ACTION, and PATH-COST (written g(n)); the set of unexpanded leaf nodes is the **frontier**, which separates explored from unreached states. **Expanding** a node generates its successor (child) nodes. A *graph search* records reached states to prune **redundant paths** and cycles; a *tree-like search* does not. Problem formulation requires choosing an appropriate level of **abstraction**: removing detail while preserving validity (every abstract solution maps to a real one) and usefulness. Search assumes atomic state representations and the simplest environments (deterministic, fully observable, static, discrete, known), in which a solution is a fixed action sequence executed open-loop.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]