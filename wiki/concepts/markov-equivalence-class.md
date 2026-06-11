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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- causal-inference
- statistics
id: pkis:concept:markov-equivalence-class
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch30
tags:
- CPDAG
- identifiability
- DAG
- causal-discovery
- v-structure
title: Markov Equivalence Class (CPDAG)
understanding: 0
uses:
- directed-graphical-models
- identifiability-of-causal-effects
- structural-causal-model
---

## Definition
Two DAGs $G_1$ and $G_2$ are **Markov equivalent** if and only if they encode the same set of conditional independence relations, i.e., they have the same skeleton and the same v-structures (immoralities). The set of all DAGs Markov equivalent to a given DAG is called its **Markov equivalence class** and is represented compactly by the **completed partially directed acyclic graph (CPDAG)**, which has directed edges where all members of the class agree on direction and undirected edges where they disagree.

### Why it matters
From purely observational data, one can identify the SCM only up to its Markov equivalence class — different members make the same observational predictions but may imply different interventional distributions. This fundamental identifiability limit motivates the use of interventional data, temporal ordering assumptions, or non-Gaussianity to further orient edges (e.g., LiNGAM).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[structural-causal-model]] — uses
- [[identifiability-of-causal-effects]] — uses
- [[directed-graphical-models]] — uses
[To be populated during integration]