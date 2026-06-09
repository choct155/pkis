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
- statistical-learning
id: pkis:technique:locality-sensitive-hashing
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- k-nearest-neighbors
related_concepts: []
sources:
- russell-norvig-aima-ch19
tags: []
title: Locality-Sensitive Hashing (LSH)
understanding: 0
---

## Definition
A randomized-algorithm technique for solving the approximate near-neighbors problem in high dimensions far faster than exhaustive or tree-based search. Ordinary hashing scatters values randomly across bins; LSH instead wants a locality-sensitive hash whose collision probability is high for nearby points and low for distant ones. Formally: given a query x_q, if some point lies within radius r, then with high probability LSH returns a point within distance cr; if no point lies within r it may report failure. The constant c and the probability are hyperparameters.

The construction relies on the intuition that points close in n-dimensional space project close on a random one-dimensional line; discretizing that line into bins makes near points usually collide. A single projection is unreliable, so LSH builds l independent random projections (each a random subset of the bit-string representation), creating l hash tables. All examples are inserted into every table. For a query, the points in x_q's bin in each of the l tables are unioned into a small candidate set C; exact distances are then computed only for points in C and the k closest returned. With high probability every true near neighbor appears in at least one bin, while the few spurious far points are filtered by the exact-distance check. On a 13-million-image, 512-dimensional dataset, LSH examined only a few thousand images -- a thousand-fold speedup over exhaustive or k-d-tree search.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[k-nearest-neighbors]] — prerequisite-of
[To be populated during integration]