---
aliases: []
also_type: []
analogous-to:
- collider-bias
applies:
- causal-discovery
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
- probabilistic-graphical-models
- causal-inference
id: pkis:concept:immorality-v-structure
instantiates:
- explaining-away
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch16
tags:
- v-structure
- collider
- d-separation
- bayesian-network
- causal-discovery
title: Immorality (V-Structure in DAGs)
understanding: 0
uses:
- d-separation
---

## Definition
An **immorality** (also called a *v-structure* or *collider*) in a directed acyclic graph is a configuration $a \rightarrow c \leftarrow b$ where $a$ and $b$ are both parents of $c$ but there is no direct edge between $a$ and $b$.

### Why it matters
Immoralities are the substructures that make directed graphical models strictly more expressive than undirected ones for encoding conditional independence. In an immorality, $a$ and $b$ are marginally independent but become dependent when $c$ (or any of its descendants) is observed—the *explaining-away* phenomenon. Because undirected graphs cannot represent this pattern without adding an edge between $a$ and $b$ (which would falsely imply unconditional dependence), moralization must connect $a$ and $b$, losing the independence information. Immoralities are central to causal discovery algorithms that orient edges by searching for these structures.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[causal-discovery]] — applies
- [[collider-bias]] — analogous-to
- [[explaining-away]] — instantiates
- [[d-separation]] — uses
[To be populated during integration]