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
- optimization
id: pkis:framework:constraint-satisfaction-problem
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch06
tags:
- csp
- factored-representation
- constraint-graph
- np-complete
- global-constraint
- alldiff
title: Constraint Satisfaction Problem (CSP)
understanding: 0
---

## Definition
A problem-solving formalism that replaces the atomic ('black-box') states of classical state-space search with a factored representation: a state is a set of variables, each assigned a value, and a solution is a complete, consistent assignment. Formally a CSP is a triple <X, D, C>: X = {X_1,...,X_n} is a set of variables; D = {D_1,...,D_n} gives each variable a domain of allowable values; and C is a set of constraints, each a pair <scope, rel> where scope is a tuple of participating variables and rel is a relation (an explicit set of legal value-tuples, or a predicate that tests membership) restricting their joint values. An assignment is consistent (legal) if it violates no constraint; complete if every variable is assigned; a solution is a consistent complete assignment. Solving a general CSP is NP-complete, though important subclasses (tree-structured, linear-programming) are tractable.

The payoff of the factored view: a CSP solver can prune large swathes of the search space at once by detecting which variable/value combinations violate constraints (e.g. fixing SA=blue in the Australia map cuts five neighbors' choices from 3^5 to 2^5), and the actions/transition model are deduced from the problem description rather than coded per-domain. CSPs are visualized as a constraint graph (nodes = variables, edges = binary constraints) or, for n-ary constraints, a constraint hypergraph.

Variables may have discrete finite domains (map coloring, scheduling with deadlines, 8-queens), discrete infinite domains (integers/strings, requiring implicit constraints; general nonlinear integer constraints are undecidable), or continuous domains (the operations-research setting; linear programming is the best-known tractable continuous-domain class). Constraints range over unary (one variable), binary (two; defines a binary CSP / constraint graph), higher-order/global (arbitrary arity, e.g. Alldiff requiring all variables distinct, or Atmost resource constraints), and preference (soft) constraints. Any finite-domain CSP can be reduced to binary constraints via auxiliary variables or the dual-graph transformation. With preference constraints encoded as costs, a CSP becomes a constrained optimization problem (COP).

Canonical example domains: map coloring (Australia's seven regions, three colors, nine inequality constraints), job-shop scheduling (tasks as integer start-time variables with precedence and disjunctive constraints), cryptarithmetic, and Sudoku (81 variables, 27 Alldiff constraints over rows/columns/boxes).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]