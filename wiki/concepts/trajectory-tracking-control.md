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
- robotics
- systems-theory
id: pkis:concept:trajectory-tracking-control
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch26
tags:
- robotics
- control
- dynamics
- feedback
title: Trajectory Tracking Control
understanding: 0
---

## Definition
The task of executing a planned reference path/trajectory by computing the actuator commands (torques) that drive the robot to follow it. A path is a sequence of geometric points; a trajectory ξ(t) is a path with a time assigned to each point (obtained by 'retiming' a path under velocity/acceleration limits). Open-loop tracking uses inverse dynamics u = f^{-1}(ξ, ξ̇, ξ̈) to compute feedforward torques, but accumulates error because the dynamics model f is imperfect; closed-loop control feeds the current tracking error back to correct it. Control laws are policies (they prescribe an action from any reached state), not plans, and turn an otherwise-open-loop motion plan into a robust policy that returns to the reference when perturbed.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]