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
id: pkis:technique:local-beam-search
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch04
tags:
- beam-search
- local-search
- parallel-search
- stochastic-beam-search
- information-sharing
title: Local Beam Search
understanding: 0
---

## Definition
A local search algorithm that keeps track of k states rather than one. It begins with k randomly generated states; at each step it generates all successors of all k states, halts if any is a goal, and otherwise selects the k best successors from the combined pool and repeats. Crucially, this is not the same as k independent random restarts run in parallel: useful information passes among the parallel threads—states generating the best successors effectively pull resources toward themselves ('come over here, the grass is greener!'), so the algorithm abandons unfruitful searches and concentrates effort where progress is greatest. Its main failure mode is loss of diversity: the k states can cluster in a small region, degrading the method to a k-times-slower hill climbing. Stochastic beam search—analogous to stochastic hill climbing—mitigates this by choosing successors with probability proportional to their value rather than taking the top k, which increases diversity and is the conceptual bridge to evolutionary algorithms (which add recombination of multiple parents).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]