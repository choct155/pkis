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
- optimization
- search-and-planning
id: pkis:technique:hill-climbing
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch04
tags:
- hill-climbing
- greedy-local-search
- steepest-ascent
- random-restart
- local-maxima
- 8-queens
title: Hill Climbing
understanding: 0
---

## Definition
The simplest local search algorithm: keep one current state, and on each iteration move to the neighboring state with the highest objective value (steepest ascent), terminating at a peak where no neighbor is better. It looks ahead no further than its immediate neighbors—'like trying to find the top of Mount Everest in a thick fog while suffering from amnesia'—and is also called greedy local search because it grabs the best neighbor without planning ahead. Hill climbing makes rapid progress on easy parts of a landscape but gets stuck at local maxima, on ridges (sequences of local maxima hard for greedy moves to navigate), and on plateaus/shoulders (flat regions where it wanders). On randomly generated 8-queens instances, steepest-ascent hill climbing solves only ~14% of cases (getting stuck 86% of the time) but is fast—~4 steps to succeed, ~3 to get stuck—in a space of 8^8 ≈ 17 million states. Variants trade speed for robustness: stochastic hill climbing chooses randomly among uphill moves (weighted by steepness); first-choice hill climbing generates successors randomly until one improves (good when there are thousands of successors); allowing bounded sideways moves (e.g. up to 100) on plateaus raises the 8-queens solve rate to ~94%; and random-restart hill climbing runs repeated searches from random initial states, achieving completeness with probability 1 (expected restarts 1/p for per-run success probability p). Because it keeps only one state in memory and expands locally, hill climbing is intrinsically an online search algorithm, though pure hill climbing is poor for exploration since it strands the agent at local maxima.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]