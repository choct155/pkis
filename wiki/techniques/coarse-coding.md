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
- reinforcement-learning
id: pkis:technique:coarse-coding
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch09
tags:
- feature-construction
- binary-features
- receptive-fields
- generalization
title: Coarse Coding
understanding: 0
---

## Definition
A feature-construction scheme representing a state by overlapping receptive fields (e.g. circles in a continuous space): a binary feature is 1 (present) if the state lies inside its field and 0 otherwise, so the set of active features coarsely codes the state's location. With linear approximation, training at one state updates the weight of every field containing it, generalizing to all states sharing fields—more strongly the more fields they share. The size and shape of the fields control the breadth and direction of initial generalization, but the acuity (finest achievable discrimination) is controlled chiefly by the total number of features, not their width. Thus broad fields give fast early generalization without limiting asymptotic resolution (Example 9.3, the square-wave learning task).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]