---
aliases: []
also_type: []
applies:
- constraint-satisfaction-problem
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- backtracking-search
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- knowledge-representation
- optimization
id: pkis:technique:min-conflicts-local-search-csp
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch06
tags:
- csp
- local-search
- complete-state-formulation
- min-conflicts
- plateau-search
- tabu-search
- online-search
title: Min-Conflicts Local Search for CSPs
understanding: 0
uses:
- simulated-annealing
---

## Definition
An incomplete but often highly effective approach to solving CSPs using local search over complete assignments (the complete-state formulation of Section 4.1): every variable always has a value, and each step changes one variable. The MIN-CONFLICTS heuristic selects a randomly chosen conflicted variable and reassigns it to the value minimizing the number of violated constraints (counted by a CONFLICTS function over the current assignment). The initial complete assignment may be random or built greedily.

Min-conflicts is strikingly effective: on n-queens its run time is roughly independent of problem size (solving the million-queens problem in ~50 steps on average), because solutions are densely distributed in the state space; this 1990s result spurred research on the easy/hard problem distinction. It scaled to schedule Hubble Space Telescope observations, cutting weekly scheduling from three weeks to ~10 minutes. The min-conflicts landscape is dominated by plateaus (millions of states one conflict from a solution), so plateau-escaping methods help: PLATEAU SEARCH (allowing sideways moves), TABU SEARCH (forbidding recently visited states), and SIMULATED ANNEALING. CONSTRAINT WEIGHTING gives each constraint a weight (initially 1), choosing the variable/value change that minimizes total violated weight and incrementing weights of currently violated constraints -- adding topography to plateaus and learning which constraints are hard.

A further advantage is ONLINE repair: when a solved problem changes (e.g. weather disrupts an airline schedule), local search starting from the current assignment can repair it with few changes, whereas re-running backtracking from scratch is slower and may yield a very different solution.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[backtracking-search]] — contrasts-with: incomplete local search over complete assignments vs. complete DFS over partial assignments
- [[simulated-annealing]] — uses: simulated annealing is one method to escape min-conflicts plateaus
- [[constraint-satisfaction-problem]] — applies: local search over complete CSP assignments
[To be populated during integration]