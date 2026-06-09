---
aliases: []
also_type: []
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- robotics
- state-space-models
extends:
- robot-localization
id: pkis:problem:simultaneous-localization-and-mapping-slam
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch26
tags:
- robotics
- mapping
- localization
- estimation
title: Simultaneous Localization and Mapping (SLAM)
understanding: 0
uses:
- kalman-filter
---

## Definition
The chicken-and-egg problem a robot faces when it must build a map of an unknown environment while simultaneously localizing itself within that partially-built map: it cannot localize without a map, yet it cannot build an accurate map without knowing where it is. SLAM is solved with probabilistic techniques—notably the extended Kalman filter (augmenting the state vector with landmark locations, with quadratic update cost), graph-relaxation/nonlinear-optimization methods that exploit the sparseness of the problem, and EM for data association. Map representations range from feature/landmark maps to occupancy grids and topological maps.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[kalman-filter]] — uses: EKF-SLAM augments the state with landmark positions
- [[robot-localization]] — extends: SLAM is localization without a given map—the map must be built concurrently
[To be populated during integration]