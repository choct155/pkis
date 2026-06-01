---
aliases: []
cross_cluster_dependencies:
- evaluation-infrastructure
- research-instrumentation
date_created: 2026-05-30
date_updated: 2026-06-01
domain:
- knowledge-representation
- symbolic-subsymbolic
- deep-learning
frontier_hypotheses:
- intensional-grounding-ned-accuracy
- intensional-grounding-vs-scale
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
Node coverage assessed 2026-06-01 (de-orphaning pilot). The cluster's task and mechanism anchors are now materialized and graph-linked: `named-entity-disambiguation` (the evaluation task), `transformer-attention-mechanisms` (the claimed mechanism, sourced to Soydaner 2022), `scaling-laws` (the foil, sourced to Bayless neurosymbolic 2025), and `formal-ontology` (the intensional structure, settled coverage).

**Lead hypothesis: `intensional-grounding-ned-accuracy`.** Operationalize token-to-ontological-class distance as a predictor of NED/NER accuracy — the most directly testable claim in the program and the first experiment to instrument. Running alongside it: **`intensional-grounding-vs-scale`**, the compute-equivalence test against scaling laws, which already has indirect support (Bayless 2025).

`intensional-grounding-ood-membership` is held off the immediate frontier: it reuses the same task machinery, but its core measure — a model-independent operationalization of "out-of-distribution" — is unresolved and is best defined once the ned-accuracy distance metric exists.

**Coverage gaps blocking instrumentation:** `knowledge-representation` is a sourceless stub (needs a canonical source — see `get_sourceless_stubs`); `named-entity-disambiguation` and `transformer-attention-mechanisms` are stubs needing deeper coverage before experiments can be designed.

## Connections
- [[knowledge-representation]] — uses: The cluster draws on knowledge representation to design experiments — intensional class definitions and membership conditions are KR constructs.
- [[transformer-attention-mechanisms]] — uses: The umbrella thesis claims ontological structure operates through attention weight redistribution.