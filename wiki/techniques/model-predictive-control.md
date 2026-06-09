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
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- robotics
- optimization
- systems-theory
id: pkis:technique:model-predictive-control
instantiates:
- trajectory-tracking-control
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch26
tags:
- robotics
- control
- online-replanning
- receding-horizon
title: Model Predictive Control (MPC)
understanding: 0
uses:
- value-of-information
---

## Definition
A control strategy for acting under uncertainty in which, at every time step, the robot plans over a short (receding) horizon, executes only the first action of the resulting plan, and then replans from the new observed state. This effectively produces a policy from a planner: deviations and new information are handled implicitly because the robot will replan anyway. MPC is the robotics analogue of real-time search and game-playing algorithms and is the standard way robots cope with imperfect dynamics models, changing most-likely-state hypotheses, and humans who deviate from a precomputed joint plan.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[trajectory-tracking-control]] — instantiates: MPC turns repeated short-horizon planning into a tracking policy
- [[value-of-information]] — uses: MPC handles uncertainty by online replanning, complementary to explicit information-gathering
[To be populated during integration]