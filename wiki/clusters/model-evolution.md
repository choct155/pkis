---
id: "pkis:research-cluster:model-evolution"
aliases: []
title: "Model Evolution"
knowledge_type: research-cluster
domain: [knowledge-representation]
tags: [ontology-maintenance, concept-drift, shadow-fragmentation, llm-assisted-authoring]
date_created: 2026-05-30
date_updated: 2026-05-30
status: active
origin: research-program
hypotheses:
  - llm-assisted-ontology-authoring-cost
  - concept-drift-detection
  - shadow-fragmentation-detection
cross_cluster_dependencies:
  - learned-symbol-grounding
  - ontological-coverage-planning
  - evaluation-infrastructure
frontier_hypotheses: []
---

## Thesis
The marginal cost of ontology maintenance can be materially reduced by using LLMs as ontology authoring assistants — proposing concept definitions, property structures, and class hierarchies from domain text with human review as the gate rather than human authorship as the source — while preserving consistency and referential integrity.

## Summary
The concept drift sub-problem: existing ontological concepts shift in meaning over time in source data. The shadow fragmentation problem: independent teams creating semantically equivalent but formally distinct concepts is the primary source of ontological debt. Automated detection of near-duplicate concept creation enables governance intervention before fragmentation compounds.

## Research Program Context
Stage 5 (Model Maintenance) primary cluster. A largely Theme 2 (operational implications) cluster. The cost reduction claim is testable; the drift and fragmentation detection claims require the Research Instrumentation infrastructure.

## Constituent Hypotheses
- **llm-assisted-ontology-authoring-cost** — LLM-assisted ontology authoring with human review gates reduces maintenance cost relative to human-authored ontologies
- **concept-drift-detection** — Distributional monitoring of ontological concept usage detects semantic drift before it produces downstream errors
- **shadow-fragmentation-detection** — Embedding similarity plus structural comparison detects near-duplicate concept creation before fragmentation compounds

## Current Frontier
To be computed by Maintenance agent.

## Connections
- [[distribution-shift]] — uses: concept drift detection is a special case of distribution shift monitoring
- [[ontology]] — uses: the cluster is about ontology maintenance specifically
