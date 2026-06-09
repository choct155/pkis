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
id: pkis:technique:probabilistic-roadmap-prm
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
- sampling
- multi-query
title: Probabilistic Roadmap (PRM)
understanding: 0
---

## Definition
A randomized motion-planning method that builds a graph (roadmap) over the configuration space by sampling M collision-free milestones in C_free (via rejection sampling using a collision checker γ) and connecting nearby pairs (the k nearest neighbors, or all within radius r) with edges whenever a fast simple planner B(q1, q2) finds a collision-free local path. The motion-planning query is then a discrete graph search on this roadmap; if no path is found, more milestones are added. PRMs are not complete but are probabilistically complete (they find a path eventually if one exists) and work well in high-dimensional C-spaces. They are especially suited to multi-query planning, amortizing the up-front roadmap construction over many start/goal queries in the same workspace.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[motion-planning]] — instantiates: a randomized roadmap method for motion planning
[To be populated during integration]