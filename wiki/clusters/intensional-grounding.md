---
aliases: []
cross_cluster_dependencies:
- evaluation-infrastructure
- research-instrumentation
date_created: 2026-05-30
date_updated: 2026-05-30
domain:
- knowledge-representation
- symbolic-subsymbolic
- deep-learning
frontier_hypotheses: []
hypotheses:
- intensional-grounding-ned-accuracy
- intensional-grounding-vs-scale
- intensional-grounding-ood-membership
id: pkis:research-cluster:intensional-grounding
knowledge_type: research-cluster
origin: research-program
status: active
tags:
- named-entity-disambiguation
- ontology
- intension-extension
- transformer-attention
title: Intensional Grounding
uses:
- knowledge-representation
- transformer-attention-mechanisms
---

## Thesis
Providing explicit intensional structure — ontological class definitions, property restrictions, necessary and sufficient conditions for concept membership — at inference time allows a model to perform entity identity and category membership tasks that it cannot perform reliably from distributional statistics alone.

## Summary
The Marcus-Lamb distinction between intension and extension is the theoretical foundation. A model trained on labeled examples learns to approximate the extension of a concept but has no guaranteed access to the intension. This explains why same-different resolution, entity disambiguation across surface variation, and category membership for novel instances all degrade systematically without structural grounding.

## Research Program Context
Primary test of the umbrella thesis at the extraction and query parsing stages. The NED/NER accuracy prediction from token-to-ontological-class distance is the most directly testable claim in the program and should be the first experiment instrumented.

## Constituent Hypotheses
- **intensional-grounding-ned-accuracy** — Token-to-ontological-class distance predicts NED/NER accuracy
- **intensional-grounding-vs-scale** — Ontological type constraints reduce entity resolution errors more than equivalent compute scaling
- **intensional-grounding-ood-membership** — Category membership for out-of-distribution instances improves with explicit intensional grounding

## Current Frontier
To be computed by Maintenance agent after PKIS node coverage is assessed.

## Connections
- [[transformer-attention-mechanisms]] — uses: The umbrella thesis claims ontological structure operates through attention weight redistribution.
- [[knowledge-representation]] — uses: The cluster draws on knowledge representation to design experiments — intensional class definitions and membership conditions are KR constructs.
- [[knowledge-representation]] — prerequisite-of: the cluster requires deep understanding of KR to design experiments
- [[transformer-attention-mechanisms]] — uses: the umbrella thesis claims ontological structure operates through attention weight redistribution