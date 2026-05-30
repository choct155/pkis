---
id: "pkis:research-cluster:compositional-query-grounding"
aliases: []
title: "Compositional Query Grounding"
knowledge_type: research-cluster
domain: [knowledge-representation, deep-learning]
tags: [query-understanding, implicit-expansion, cross-store-alignment, rag]
date_created: 2026-05-30
date_updated: 2026-05-30
status: active
origin: research-program
hypotheses:
  - implicit-entity-expansion-accuracy
  - cross-store-referential-alignment
cross_cluster_dependencies:
  - intensional-grounding
  - retrieval-inference-tradeoff
  - parsed-intent-calibration
  - evaluation-infrastructure
frontier_hypotheses: []
---

## Thesis
Ontological structure enables reliable decomposition of natural language queries into structured intent representations, implicit expansion of entity and field scope, and referential alignment across heterogeneous stores — tasks that purely statistical query understanding fails on at the margin cases that matter most.

## Summary
The implicit expansion problem: a query about Apple's performance must surface iPhone as the relevant product entity without the user naming it. The cross-store alignment problem: 'Apple', 'Apple Inc.', and 'AAPL' must resolve to the same canonical entity across relational, graph, and vector stores. Both require ontological inference that stochastic generation cannot reliably provide.

## Research Program Context
Spans the most stages of the value chain (6, 7, 8) and has the most cross-cluster dependencies. Should be addressed after Intensional Grounding and Parsed Intent Calibration have produced initial results.

## Constituent Hypotheses
- **implicit-entity-expansion-accuracy** — Ontological inference improves implicit entity expansion accuracy over stochastic generation
- **cross-store-referential-alignment** — Ontological backbone enables cross-store entity alignment that reduces referential errors

## Current Frontier
To be computed by Maintenance agent.

## Connections
- [[knowledge-graph-traversal]] — uses: cross-store alignment requires KG as the alignment backbone
- [[probabilistic-inference]] — prerequisite-of: Bayesian framing of query intent posterior requires understanding probabilistic inference
