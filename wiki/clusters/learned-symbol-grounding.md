---
id: "pkis:research-cluster:learned-symbol-grounding"
aliases: []
title: "Learned Symbol Grounding"
knowledge_type: research-cluster
domain: [knowledge-representation, deep-learning, symbolic-subsymbolic]
tags: [vector-quantization, concept-bottleneck, neurosymbolic, discrete-representation]
date_created: 2026-05-30
date_updated: 2026-05-30
status: active
origin: research-program
hypotheses:
  - concept-bottleneck-auditability
  - learned-symbol-ontology-alignment
cross_cluster_dependencies:
  - intensional-grounding
  - embedding-ontology-alignment
  - evaluation-infrastructure
frontier_hypotheses: []
---

## Thesis
Learning systems can be designed to discover discrete, human-interpretable symbolic abstractions from data rather than opaque continuous embeddings — and these learned symbols can be aligned to formal ontological concepts to create a closed loop between statistical learning and symbolic knowledge maintenance.

## Summary
The near-term production-relevant subset is concept bottleneck architectures, which are deployable today. Full neurosymbolic abstraction learning (DreamCoder-style) remains frontier research. This cluster is partially a watch-and-learn thread with concept bottleneck models as the production-ready bridgehead.

## Research Program Context
Straddles Theme 1 (science of complementarity) and Theme 2 (operational implications). The auditability use case is immediately deployable; the closed-loop symbol learning endpoint is a 2027-2030 horizon item.

## Constituent Hypotheses
- **concept-bottleneck-auditability** — Concept bottleneck architectures provide sufficient audit trail for production QA workflows
- **learned-symbol-ontology-alignment** — Learned discrete symbols from VQ-VAE style approaches can be reliably aligned to formal ontological concepts

## Current Frontier
To be computed by Maintenance agent.

## Connections
- [[vector-quantization]] — uses: VQ-VAE is the foundational technique for discrete representation learning
- [[concept-bottleneck-models]] — uses: near-term production instantiation of the cluster
