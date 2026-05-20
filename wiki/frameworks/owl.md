---
title: "OWL (Web Ontology Language)"
knowledge_type: framework
also_type: [concept]
domain: [knowledge-representation]
tags: [semantic-web, ontology, description-logic, owl2, rdfs, w3c-standard, reasoning, expressivity]
related_concepts: ["[[rdfs]]", "[[rdf]]", "[[description-logic]]", "[[ontology-reasoning]]", "[[sparql]]", "[[skos]]"]
sources: ["[[allemang-semantic-web]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

W3C standard ontology language extending RDFS with richer expressiveness grounded in Description Logic. OWL provides: property characteristics (owl:inverseOf, owl:SymmetricProperty, owl:TransitiveProperty, owl:FunctionalProperty), class expressions (owl:intersectionOf, owl:unionOf, owl:complementOf, owl:oneOf), property restrictions (owl:allValuesFrom, owl:someValuesFrom), cardinality constraints, and individual identity (owl:sameAs, owl:differentFrom). OWL 2 introduced profiles (EL, QL, RL) that trade expressivity for tractable reasoning. The tradeoff between expressivity and computational complexity is the central design tension: OWL Full is undecidable; OWL DL is decidable but EXPTIME-complete; OWL 2 RL is polynomial and implementable via SPARQL rules.

Classification note: assigned as framework because OWL is a coherent system that organizes concepts (class expressions), techniques (inference regimes), and principles (OWA) into an interoperable standard; but also_type concept because it can be studied as "what is OWL?" — a defined language with a specification.

## Connections
- [[rdfs]] — extends: OWL builds on RDFS, adding expressivity beyond subclass/subproperty hierarchies
- [[description-logic]] — grounds: OWL DL corresponds to the SHOIN(D) description logic; OWL 2 to SROIQ(D)
- [[ontology-reasoning]] — uses: OWL's formal semantics defines what a reasoner must infer from OWL axioms
- [[sparql]] — uses: OWL 2 RL can be implemented entirely as SPARQL CONSTRUCT rules over RDF data
- [[skos]] — contrasts-with: SKOS provides lightweight vocabulary management without OWL class-instance modeling
- [[open-world-assumption]] — uses: OWL operates under the OWA, which shapes all modeling decisions

## Reading Path
- [[allemang-semantic-web-ch08]] (unread) — RDFS-Plus: the practical OWL sweet spot (inverseOf, symmetry, transitivity, equivalence)
- [[allemang-semantic-web-ch11]] (unread) — Basic OWL: property restrictions, individual identity
- [[allemang-semantic-web-ch12]] (unread) — Counting and sets in OWL: cardinality, set operations
- [[allemang-semantic-web-ch15]] (unread) — Expert modeling: OWL 2 profiles, QUDT and OBO case studies
