---
title: "SKOS (Simple Knowledge Organization System)"
knowledge_type: framework
also_type: [concept]
domain: [knowledge-representation]
tags: [semantic-web, controlled-vocabulary, thesaurus, taxonomy, rdfs, w3c-standard, knowledge-organization]
related_concepts: ["[[rdf]]", "[[rdfs]]", "[[owl]]", "[[linked-open-data]]", "[[ontology-reasoning]]"]
sources: ["[[allemang-semantic-web]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

W3C standard for representing controlled vocabularies, thesauri, and classification schemes in RDF without the heavyweight machinery of OWL class-instance modeling. Core constructs: `skos:Concept` (a unit of meaning), `skos:ConceptScheme` (a collection of concepts), hierarchical relations (`skos:broader`, `skos:narrower`), associative relation (`skos:related`), labeling properties (`skos:prefLabel`, `skos:altLabel`, `skos:hiddenLabel`), and documentation properties (`skos:scopeNote`, `skos:definition`, `skos:example`). SKOS treats concepts as individuals (not classes), making it complementary to rather than competing with OWL. High-profile deployments include the Library of Congress Subject Headings, Europeana, and DBpedia categories.

Classification note: assigned as framework because SKOS is a coherent system for organizing vocabulary knowledge; also_type concept because it is itself a defined W3C vocabulary with a formal specification.

## Connections
- [[rdf]] — uses: SKOS is built entirely on RDF triples; concepts are RDF resources identified by URIs
- [[rdfs]] — uses: SKOS uses RDFS vocabulary for its own specification; rdfs:label bridges SKOS labels to RDFS
- [[owl]] — contrasts-with: SKOS manages vocabularies without OWL's class-instance hierarchy; concepts are individuals, not classes
- [[linked-open-data]] — uses: SKOS is a primary format for publishing controlled vocabularies as Linked Open Data
- [[ontology-reasoning]] — uses: SKOS mapping properties (skos:exactMatch, skos:broadMatch) enable cross-vocabulary alignment and limited inference

## Reading Path
- [[allemang-semantic-web-ch10]] (unread) — primary treatment: SKOS vocabulary, ConceptScheme, hierarchical/associative relations, labeling
- [[allemang-semantic-web-ch09]] (unread) — context from RDFS-Plus in the wild that motivates SKOS's design
