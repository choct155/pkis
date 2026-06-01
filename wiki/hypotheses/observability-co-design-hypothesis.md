---
aliases: []
cluster_membership:
- research-instrumentation
date_created: '2026-06-01'
date_updated: '2026-06-01'
dependent_nodes:
- node: '[[causal-analysis]]'
  node_type: concept
  rationale: valid experimental inference requires confounding and identification
    control
domain:
- knowledge-representation
- deep-learning
evidence_nodes: []
id: pkis:hypothesis:observability-co-design-hypothesis
iks_link: null
knowledge_type: hypothesis
origin: research-program
research_program_cluster: research-instrumentation
research_program_role: methodological
status: open
tags:
- observability
- instrumentation
- experimental-design
title: Co-Designing Observability With the Experimental Program Yields More Testable
  Hypotheses Than Retrofitting
uses:
- causal-analysis
---

## Formal Statement
Co-designing the platform's observability (token-level attention, entity-resolution decisions, retrieval-path choices, result-composition events) with the experimental program produces more testable hypotheses than retrofitting instrumentation after the fact.

## Motivation
Measurements that don't exist at inference time cannot be reconstructed later; the granularity of instrumentation bounds which hypotheses are testable at all.

## Current Evidence
[To be filled]

## Open Questions
What is the minimal instrumentation set that covers all clusters' measurement needs without prohibitive overhead?

## Connections
- [[causal-analysis]] — uses: instrumentation must capture what causal attribution requires
- [[research-instrumentation]] — belongs-to: constituent hypothesis of the research-instrumentation cluster