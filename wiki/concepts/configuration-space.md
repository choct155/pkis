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
- optimization
id: pkis:concept:configuration-space
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch26
tags:
- robotics
- motion-planning
- kinematics
- degrees-of-freedom
title: Configuration Space (C-space)
understanding: 0
---

## Definition
An abstract multidimensional space in which an entire robot—every point on its body—is represented by a single point q, given the robot's fixed geometry plus its current pose. The dimensionality equals the robot's degrees of freedom (e.g., (x, y) for a non-rotating planar robot; (x, y, θ) if it rotates; (θ_shoulder, θ_elbow) for a two-link arm). Forward kinematics φ_b: C → W maps a configuration to the workspace location of a body point; inverse kinematics maps a desired workspace location to the configuration(s) achieving it. The workspace obstacle region O induces a C-space obstacle C_obs = {q : A(q) ∩ O ≠ ∅}, whose complement is the free space C_free. C-space obstacles can be highly nonlinear even when workspace obstacles are simple polygons, so planners usually probe C-space with a collision checker rather than constructing C_obs explicitly.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]