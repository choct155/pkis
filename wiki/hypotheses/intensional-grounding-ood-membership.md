---
id: "pkis:hypothesis:intensional-grounding-ood-membership"
aliases: []
title: "Category Membership for Out-of-Distribution Instances Improves With Explicit Intensional Grounding"
knowledge_type: hypothesis
domain: [knowledge-representation, deep-learning]
tags: [named-entity-disambiguation, ontology, intensional-grounding, out-of-distribution, category-membership]
date_created: 2026-06-01
date_updated: 2026-06-01
status: open
origin: research-program
research_program_cluster: intensional-grounding
research_program_role: generalization-test
iks_link: null
cluster_membership:
  - intensional-grounding
dependent_nodes:
  - node: "[[named-entity-disambiguation]]"
    node_type: technique
    rationale: "Category membership for novel instances is evaluated through the same entity identity / classification machinery as NED"
  - node: "[[ontology]]"
    node_type: concept
    rationale: "Explicit intensional grounding is supplied as ontological class definitions with necessary and sufficient membership conditions — the independent variable"
  - node: "[[transformer-attention-mechanisms]]"
    node_type: technique
    rationale: "The claimed mechanism for membership generalization is attention over intensional structure rather than distributional proximity"
evidence_nodes: []
---

## Formal Statement
For instances that fall outside the training distribution — novel entities, rare surface forms, or categories sparsely represented in the pretraining corpus — providing explicit intensional structure (ontological class definitions with necessary and sufficient membership conditions) at inference time improves category-membership accuracy by a greater margin than it does for in-distribution instances. The benefit of intensional grounding scales with distributional novelty.

## Motivation
A model that has only learned the extension of a concept approximates membership by similarity to seen examples, so it degrades exactly where the distribution thins out. If membership is instead decided by checking an instance against explicit intensional conditions, performance should be far less sensitive to whether the instance was well represented in training. This is the cleanest test of the intension-vs-extension distinction at the generalization frontier: the prediction is not just that grounding helps, but that it helps *differentially* on out-of-distribution instances.

## Current Evidence
Indirect. Think-on-Graph (Sun et al., ICLR 2024; Wu et al. 2025) shows that grounding reasoning in an explicit knowledge-graph structure improves multi-hop resolution on entities a purely parametric model handles poorly — consistent with structural grounding helping most where parametric coverage is thin. No study has directly measured the interaction between distributional novelty and intensional-grounding benefit for category membership.

## Open Questions
How to operationalize "out-of-distribution" for category membership in a way that is independent of the model under test (corpus frequency? embedding density? held-out novel classes?). Whether the differential benefit holds for fine-grained categories where intensional conditions are themselves hard to specify. How to separate the contribution of the ontology's class definitions from the contribution of the retrieval step that surfaces them.

## Connections
- [[intensional-grounding]] — belongs-to: this is a constituent hypothesis of the Intensional Grounding cluster, testing it at the out-of-distribution generalization frontier
