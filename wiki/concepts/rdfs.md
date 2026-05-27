---
id: "pkis:concept:rdfs"
aliases: ["RDFS"]
title: "RDF Schema (RDFS)"
knowledge_type: concept
also_type: []
domain: [knowledge-representation]
tags: [semantic-web, rdf, schema, subclass, subproperty, domain-range, w3c-standard, ontology]
related_concepts: ["[[rdf]]", "[[owl]]", "[[ontology-reasoning]]", "[[sparql]]"]
sources: ["[[allemang-semantic-web]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

W3C standard schema layer built on top of RDF that adds class and property hierarchies: `rdfs:subClassOf` (inheritance between classes), `rdfs:subPropertyOf` (inheritance between properties), `rdfs:domain` (constraining the type of a property's subject), and `rdfs:range` (constraining the type of a property's object). RDFS inference rules propagate type information through these hierarchies, enabling a reasoner to infer that an individual is a member of a superclass given membership in a subclass.

## Connections
- [[rdf]] — extends: RDFS adds schema-level vocabulary on top of the basic RDF triple model
- [[owl]] — prerequisite-of: OWL extends RDFS with richer ontological constructs; RDFS is the minimal schema layer
- [[ontology-reasoning]] — uses: RDFS inference rules (subClassOf, subPropertyOf, domain, range) are the simplest entailment regime
- [[sparql]] — uses: SPARQL CONSTRUCT queries can precisely express each RDFS inference rule, making RDFS semantics executable

## Reading Path
- [[allemang-semantic-web-ch07]] (unread) — primary treatment: full RDFS language, inference rules, modeling patterns
- [[allemang-semantic-web-ch08]] (unread) — RDFS-Plus: OWL additions that extend RDFS to the practical sweet spot
