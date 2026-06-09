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
- state-space-models
id: pkis:concept:robot-localization
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch26
tags:
- robotics
- filtering
- pose-estimation
- belief-state
title: Robot Localization
understanding: 0
---

## Definition
The problem of estimating where things are—especially the robot itself—by maintaining a posterior belief over the robot's pose (e.g., (x, y, θ) for a planar mobile robot) given a stream of actions and observations. Localization is the continuous, action-conditioned form of recursive filtering: the belief is propagated through a probabilistic motion model P(X_{t+1} | X_t, a_t) and corrected by a sensor model P(z_t | X_t), with the recursive filtering equation using integration rather than summation. Sensor models include landmark models (range and bearing to known-location features) and range-scan models (a vector of beam distances to nearest obstacles). Two dominant belief representations are used: a Gaussian (Kalman/extended Kalman filter) and a particle set (Monte Carlo localization). When no map is given, localization couples with mapping into SLAM.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]