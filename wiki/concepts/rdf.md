---
aliases:
- RDF
also_type:
- framework
coverage: 3
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- knowledge-representation
id: pkis:concept:rdf
knowledge_type: concept
maturity: settled
related_concepts: []
sources:
- '[[papadaki-rdf-analytics-survey]]'
- '[[allemang-semantic-web]]'
- '[[cimiano-ontology-nlp]]'
- allemang-semantic-web-ch02
- allemang-semantic-web-ch03
- allemang-semantic-web-ch04
- allemang-semantic-web-ch06
- allemang-semantic-web-ch07
- allemang-semantic-web-ch08
- allemang-semantic-web-ch09
- allemang-semantic-web-ch10
- allemang-semantic-web-ch11
- allemang-semantic-web-ch13
- allemang-semantic-web-ch16
- cimiano-ontology-nlp-ch10
tags:
- semantic-web
- linked-data
- graph-model
- triples
- w3c-standard
title: Resource Description Framework (RDF)
understanding: 0
---

W3C standard graph-based data model for the Semantic Web: data is expressed as triples of the form (subject, predicate, object), where subjects and predicates are URIs, objects are URIs or literals, and any finite set of triples constitutes an RDF graph. RDF Schema (RDFS) adds class and property hierarchies; OWL adds richer ontological expressiveness. The open-world assumption distinguishes RDF from relational databases.

## Reading Path
- [[papadaki-rdf-analytics-survey]] (unread) — RDF as the data model for KG analytics; SPARQL query patterns
- [[allemang-semantic-web-ch03]] (unread) — primary treatment: triple model, URI/namespace identity, blank nodes, serialization formats (Turtle, N-Triples, RDF/XML, RDFa)
- [[allemang-semantic-web-ch06]] (unread) — RDF and inferencing: asserted vs. inferred triples, SPARQL-based rule specification
- [[cimiano-ontology-nlp-ch01]] (unread) — RDF as shared data model for ontologies, lemon lexica, and domain KB in the QA application