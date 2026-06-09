---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- probabilistic-roadmap-prm
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- robotics
- optimization
id: pkis:technique:trajectory-optimization-motion-planning
instantiates:
- motion-planning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch26
tags:
- robotics
- motion-planning
- calculus-of-variations
- signed-distance-field
title: Trajectory Optimization for Motion Planning
understanding: 0
uses:
- simulated-annealing
---

## Definition
A motion-planning approach that starts from a simple but possibly infeasible path (e.g., a straight line) and optimizes a cost functional J[τ] = J_obs + λ J_eff over the path, pushing it out of collision while keeping it efficient/smooth. Efficiency is encoded quadratically as the integral of the squared path derivative (whose unconstrained optimum is the straight line); the obstacle term uses a signed distance field to build a workspace cost field that the robot body sweeps through via a retiming-invariant path integral. Because J is a functional of a function, its gradient is obtained via the calculus of variations (Euler–Lagrange equation) and minimized by gradient descent, which finds only local optima—so exploration methods such as simulated annealing can improve the result. This complements sampling planners, which instead find a feasible path first and then optimize it.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[simulated-annealing]] — uses: annealing used for exploration to escape poor local optima of the functional gradient descent
- [[probabilistic-roadmap-prm]] — contrasts-with: optimization starts feasible-then-optimize is reversed: it starts infeasible and pushes out of collision, vs sampling planners that find a feasible path first
- [[motion-planning]] — instantiates: optimization-based path generation for motion planning
[To be populated during integration]