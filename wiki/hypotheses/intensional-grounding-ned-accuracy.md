---
aliases: []
cluster_membership:
- intensional-grounding
date_created: 2026-05-30
date_updated: 2026-05-30
dependent_nodes:
- node: '[[named-entity-disambiguation]]'
  node_type: technique
  rationale: Addressing this hypothesis requires implementing and evaluating NED systems
- node: '[[transformer-attention-mechanisms]]'
  node_type: technique
  rationale: The umbrella thesis claims ontological structure operates through attention
    redistribution — testing this requires understanding attention mechanisms
- node: '[[ontology]]'
  node_type: concept
  rationale: Ontological class definitions are the independent variable in this hypothesis
domain:
- knowledge-representation
- deep-learning
evidence_nodes: []
id: pkis:hypothesis:intensional-grounding-ned-accuracy
iks_link: null
knowledge_type: hypothesis
origin: research-program
research_program_cluster: intensional-grounding
research_program_role: direct-test
status: open
tags:
- named-entity-disambiguation
- ontology
- intensional-grounding
title: Token-to-Ontological-Class Distance Predicts NED/NER Accuracy
uses:
- named-entity-disambiguation
- transformer-attention-mechanisms
- formal-ontology
---

## Formal Statement
Token-to-ontological-class distance — measured as the semantic distance between a surface token and its candidate ontological class assignments in the embedding space — predicts NED/NER accuracy: entities with closer token-to-class distance are resolved correctly at higher rates than those with greater distance.

## Motivation
If ontological structure operates through attention weight redistribution, then the degree to which a token is already semantically proximate to its correct ontological class in the model's representation should predict whether the model resolves it correctly. This is a clean, testable operationalization of the umbrella thesis.

## Current Evidence
Indirect support from Think-on-Graph (Sun et al., ICLR 2024) showing KG traversal improves multi-hop entity resolution. Direct measurement of token-to-class distance as a predictor variable has not been published.

## Open Questions
How to operationalize token-to-ontological-class distance in a way that is independent of the NED system being evaluated. What distance metric is most appropriate in the embedding space.

## Connections
- [[formal-ontology]] — uses: Ontological class definitions are the independent variable; the [[ontology]] reference resolves to the materialized formal-ontology node.
- [[transformer-attention-mechanisms]] — uses: Token-to-class distance is operationalized through the attention mechanism the hypothesis claims as the channel.
- [[named-entity-disambiguation]] — uses: NED/NER is the task whose accuracy the hypothesis predicts from token-to-class distance.
- [[intensional-grounding]] — belongs-to: this is a constituent hypothesis of the Intensional Grounding cluster