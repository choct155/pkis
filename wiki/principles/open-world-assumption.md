---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- knowledge-representation
id: pkis:principle:open-world-assumption
knowledge_type: principle
maturity: settled
related_concepts:
- '[[rdf]]'
- '[[owl]]'
- '[[rdfs]]'
- '[[ontology-reasoning]]'
- '[[description-logic]]'
sources:
- '[[allemang-semantic-web]]'
- allemang-semantic-web-ch01
- allemang-semantic-web-ch11
- allemang-semantic-web-ch14
tags:
- semantic-web
- epistemology
- owl
- rdf
- open-world
- closed-world
- logic
- database-theory
title: Open World Assumption
understanding: 0
---

The epistemic stance that absence of information does not constitute evidence of falsity: if a fact is not asserted in the knowledge base, it may still be true — it is simply unknown. Contrasts with the Closed World Assumption (CWA) of relational databases and Prolog, where everything not known to be true is assumed false. In the Semantic Web / RDF / OWL context, the OWA reflects the open nature of the Web: at any time, new triples about any URI may be published by anyone. This fundamentally shapes ontology modeling — a query returning no results does not mean the answer is "no," but rather "not known." The OWA forces modelers to be explicit about what they assert, rather than relying on absence as a substitute for negation.

## Connections
- [[rdf]] — grounds: OWA is a foundational commitment of the RDF data model; merging new triples can only add knowledge, never contradict existing conclusions (in RDF)
- [[owl]] — grounds: OWL operates under the OWA, which makes owl:differentFrom and owl:AllDifferent necessary (the Unique Name Assumption must be explicitly stated)
- [[ontology-reasoning]] — grounds: OWA shapes the semantics of RDFS/OWL inference; reasoning under OWA vs. CWA yields different entailments
- [[directed-graphical-models]] — contrasts-with: Bayesian networks typically assume a closed probability model; OWA and probabilistic reasoning represent different epistemic stances

## Reading Path
- [[allemang-semantic-web-ch01]] (unread) — introductory treatment: OWA as one of the four defining features of the Semantic Web
- [[allemang-semantic-web-ch14]] (unread) — good/bad modeling practices: how OWA shapes concrete modeling decisions and common pitfalls