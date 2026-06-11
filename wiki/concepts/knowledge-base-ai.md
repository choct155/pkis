---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- data-driven-ai
- machine-consciousness-and-qualia
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- artificial-intelligence
- knowledge-representation
id: pkis:concept:knowledge-base-ai
instantiates:
- cyc-knowledge-base
- knowledge-based-agent
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch01
tags:
- cyc
- formal-knowledge
- expert-systems
- symbolic-ai
title: Knowledge Base Approach to AI
understanding: 0
---

## Definition
The knowledge base approach to AI attempts to encode world knowledge as **explicit formal statements** in a logical language, then use automated inference to derive new facts and support decision-making — without any learning from data.

Exemplified by the Cyc project (Lenat & Guha, 1989): a large hand-curated ontology of common-sense facts expressed in CycL, combined with an inference engine.

### Why it matters
Despite enormous engineering effort, purely knowledge-base systems struggle with the **brittleness problem**: the world is too complex and varied for exhaustive formal specification. Failures on mundane situations (e.g., Cyc's confusion about a person holding an electric razor) motivated the shift toward machine learning approaches that acquire knowledge from data.

### Contrast with machine learning
Where the knowledge base approach requires human operators to specify all knowledge, machine learning discovers knowledge automatically from examples, trading engineering effort for labeled data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[machine-consciousness-and-qualia]] — contrasts-with
- [[knowledge-based-agent]] — instantiates
- [[data-driven-ai]] — contrasts-with
- [[cyc-knowledge-base]] — instantiates: Cyc is the flagship example of the knowledge base approach.
[To be populated during integration]