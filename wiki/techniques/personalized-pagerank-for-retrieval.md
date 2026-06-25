---
aliases:
- spreading activation
- PPR
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- dense-passage-retrieval
coverage: 0
date_created: '2026-06-25'
date_updated: '2026-06-25'
domain:
- knowledge-representation
- machine-learning
id: pkis:technique:personalized-pagerank-for-retrieval
instantiates:
- coverage-driven-graph-traversal
knowledge_type: technique
maturity: evolving
needs_canonical_source: true
related_concepts: []
sources: []
tags:
- retrieval
- graph
- pagerank
- spreading-activation
- reranking
title: Personalized PageRank for Retrieval
understanding: 0
---

## Definition
Graph-based ranking that scores nodes by the stationary distribution of a random walk which, at each step, teleports back to a set of seed nodes with probability alpha. Seeded on the candidates returned by a first-stage retriever and run over a typed knowledge graph, it propagates relevance along edges: a node well-connected to many strong hits is boosted even if its own text matched the query weakly (spreading activation). It is a concrete instance of a pluggable graph-traversal ranking function, and only computable when a structured graph exists.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[dense-passage-retrieval]] — contrasts-with: structural relevance propagated over typed edges vs independent surface-embedding similarity
- [[coverage-driven-graph-traversal]] — instantiates: PPR is a concrete pluggable ranking function R over the typed knowledge graph
[To be populated during integration]

## Needs Canonical Source
This stub was created without a source. Suggested references:

**Already in corpus:**
[none in corpus]

**External candidates (Semantic Scholar):**
[none found]