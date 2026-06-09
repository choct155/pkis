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
id: pkis:technique:state-aggregation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch09
specializes:
- linear-function-approximation-rl
tags:
- function-approximation
- generalization
- coarse-coding
title: State Aggregation
understanding: 0
---

## Definition
The simplest generalizing function approximator: states are partitioned into groups, with one weight component per group; a state's estimated value is its group's component, and an update changes only that component. It is a special case of SGD (and of linear function approximation) in which the feature vector is a one-hot indicator with gradient 1 for the active group and 0 elsewhere. On the 1000-state random walk, gradient MC with 10 groups of 100 states yields the characteristic 'staircase' value function near the global VE optimum; the within-group estimate is biased toward states weighted more heavily by μ (e.g. the high-value end of a left-edge group). Its limitations—coarse, axis-parallel boundaries and poor scaling—motivate richer coarse-coding schemes such as tile coding.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[linear-function-approximation-rl]] — specializes: state aggregation is linear approximation with one-hot group-indicator features
[To be populated during integration]