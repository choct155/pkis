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
extends:
- probabilistic-roadmap-prm
id: pkis:technique:rapidly-exploring-random-tree-rrt
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
- single-query
title: Rapidly-Exploring Random Tree (RRT)
understanding: 0
---

## Definition
A randomized, single-query motion planner that incrementally grows tree(s)—often one rooted at q_s and one at q_g—by repeatedly sampling a random milestone and extending the nearest tree vertex a step δ toward it, which biases growth into unexplored regions of the configuration space. A solution is found when the two trees connect. RRT solutions are typically non-optimal and non-smooth, so they are post-processed (e.g., 'short-cutting' that removes path vertices by reconnecting neighbors). RRT* is an asymptotically-optimal variant that selects parents by cost-to-come (rather than distance) and rewires the tree as cheaper routes appear, converging to the optimal path as more milestones are sampled.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[probabilistic-roadmap-prm]] — extends: RRT is described as an extension of the PRM idea for single-query planning
- [[motion-planning]] — instantiates: a randomized single-query tree method for motion planning
[To be populated during integration]