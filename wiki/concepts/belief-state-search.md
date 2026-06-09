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
- search-and-planning
id: pkis:concept:belief-state-search
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- markov-decision-processes
related_concepts: []
sources:
- russell-norvig-aima-ch04
tags:
- belief-state
- partial-observability
- sensorless-problem
- conformant-planning
- state-estimation
- prediction-update
- localization
title: Belief-State Search
understanding: 0
uses:
- and-or-search
---

## Definition
When an environment is partially observable, the agent does not know its exact physical state, so it reasons over a belief state: the set of physical states it believes are possible. Search then takes place in belief-state space rather than physical-state space—a space that is itself fully observable (the agent always knows its own belief state) but exponentially larger (up to 2^N belief states for N physical states). For a sensorless (conformant) problem, where percepts give no information, the solution is an ordinary action sequence (no contingencies, since percepts are always empty), so one transforms the physical problem into a belief-state problem—initial belief state = all states; ACTIONS(b) = union (or intersection, if illegal actions are dangerous) over states in b; deterministic transitions map each state forward (belief state shrinks or stays equal), while nondeterministic transitions take the union of RESULTS (belief state may grow); the goal is necessarily achieved when every state in b is a goal—and applies any Chapter-3 search algorithm. With actual sensing, the belief-state transition has three stages: PREDICT (apply the action, b̂=RESULT(b,a)), POSSIBLE-PERCEPTS (the percepts that could be observed in b̂), and UPDATE (for each percept o, b_o = states in b̂ consistent with o); deterministic sensing partitions b̂ into disjoint b_o, and observation can only shrink uncertainty. Feeding this RESULTS function to AND-OR search yields a conditional plan that branches on the belief state. Maintaining the belief state during execution—b' = UPDATE(PREDICT(b,a),o)—is a recursive state estimator and goes by the names monitoring, filtering, and state estimation; robot localization (recovering position from a map plus a percept/action sequence) is the canonical example.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[markov-decision-processes]] — prerequisite-of: Belief states generalize to POMDPs / probabilistic state estimation (AIMA Ch. 17).
- [[and-or-search]] — uses: General partially observable problems are solved by running AND-OR search over belief states.
[To be populated during integration]