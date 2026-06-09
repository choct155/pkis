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
- optimization
id: pkis:problem:motion-planning
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch26
tags:
- robotics
- path-planning
- configuration-space
- search
title: Motion Planning (Piano Mover's Problem)
understanding: 0
---

## Definition
The problem of finding a collision-free path that takes a robot from a start configuration q_s to a goal configuration q_g through the free space C_free, given a workspace, an obstacle region, and the robot's configuration space. A path is a parameterized curve τ(t) with τ(0)=q_s, τ(1)=q_g, and τ(t) ∈ C_free for all t. Motion planning is a quintessentially continuous-state search problem (PSPACE-hard in general) that is commonly reduced to discrete graph search by discretizing C-space—via visibility graphs, Voronoi diagrams, cell decomposition, randomized roadmaps/trees, or trajectory optimization. It is the geometric building block that, combined with trajectory tracking control, generates robot motion.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]