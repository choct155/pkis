---
id: "pkis:hypothesis:scaling-foil-null-hypothesis"
aliases: []
title: "Scaling Foil — Can Sufficiently Large LLMs Subsume Each Cluster's Task Without Ontological Scaffolding?"
knowledge_type: hypothesis
domain: [knowledge-representation, deep-learning, symbolic-subsymbolic]
tags: [scaling-laws, null-hypothesis, compute-efficiency, ontology]
date_created: 2026-05-30
date_updated: 2026-05-30
status: open
origin: research-program
research_program_cluster: null
research_program_role: scaling-foil
iks_link: null
cluster_membership:
  - intensional-grounding
  - learned-symbol-grounding
  - compositional-query-grounding
  - ontological-coverage-planning
  - structured-validation-truth-discovery
  - embedding-ontology-alignment
  - model-evolution
  - parsed-intent-calibration
  - retrieval-inference-tradeoff
  - composite-credibility
  - research-instrumentation
  - evaluation-infrastructure
dependent_nodes:
  - node: "[[scaling-laws]]"
    node_type: result
    rationale: "The null hypothesis is grounded in scaling law predictions"
  - node: "[[transformer-attention-mechanisms]]"
    node_type: technique
    rationale: "Understanding attention mechanisms is required to assess whether architectural limitations prevent scaling from subsuming symbolic tasks"
evidence_nodes: []
---

## Formal Statement
A sufficiently large language model, given sufficient training data, can subsume the task of each hypothesis cluster without ontological scaffolding — making ontological investment unnecessary.

## Motivation
This is the null hypothesis that must be rejected for the research program's claims to hold. It is not a straw man — scaling has subsumed many tasks previously thought to require symbolic reasoning. The burden of proof is on the research program to demonstrate cases where architectural or economic reasons prevent this.

## Current Evidence
Literature suggests the null is false for architectural reasons in cases requiring intensional grounding (category membership for novel instances) and for economic reasons in cases where retrieval dominates inference on cost × error rate. The Hamilton et al. structured review provides the most balanced empirical assessment.

## Open Questions
Per-cluster: the null hypothesis is not uniformly true or false across all clusters. Each cluster requires its own experimental refutation.

## Connections
- [[all-clusters]] — belongs-to: this hypothesis is a constituent of every cluster
