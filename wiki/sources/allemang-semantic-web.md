---
abbrev: "SWWO"
id: "pkis:source:allemang-semantic-web"
aliases: ["Semantic Web for the Working Ontologist"]
title: "[SWWO Allemang & Hendler] Semantic Web for the Working Ontologist, 2nd Ed."
authors: "Dean Allemang, Jim Hendler"
year: 2011
type: book
domain: [knowledge-representation]
tags: [semantic-web, rdf, rdfs, owl, skos, ontology, linked-data, sparql, w3c-standard]
source_url: ""
drive_id: "1w9NmGv55cBYLxVG4L32t5uWYXZY3KTTV"
drive_path: "PKIS/sources/books/Semantic Web for the Working Ontologist 2nd Ed"
isbn: "978-0-12-385965-5"
toc_source: "openlibrary"
status: unread
date_added: 2026-05-20
concepts:
  - "[[rdf]]"
  - "[[rdfs]]"
  - "[[owl]]"
  - "[[skos]]"
  - "[[sparql]]"
  - "[[linked-open-data]]"
  - "[[ontology-reasoning]]"
  - "[[knowledge-graph]]"
  - "[[open-world-assumption]]"
  - "[[description-logic]]"
  - "[[linked-data-principles]]"
  - "[[semantic-web]]"
---

## Summary

*Semantic Web for the Working Ontologist* (2nd ed., 2011) is the primary practical reference for building ontologies and knowledge models on the Semantic Web using RDF, RDFS, OWL, and SKOS. Authored by Dean Allemang (TopQuadrant) and Jim Hendler (RPI), the book targets practitioners—not logicians—who need to model real-world domains in a distributed, open-world setting.

The book opens with a conceptual introduction to the Semantic Web: why a distributed web of data (not documents) requires a different data model, and what the "AAA slogan" (Anyone can say Anything about Any topic) and the Open World Assumption imply for modeling. RDF is introduced as the foundational triple-based data model; SPARQL as the query/inference language; RDFS as the basic schema layer (class and property hierarchies, domain/range constraints); and OWL as the richer ontological layer (inverse, symmetric, transitive, functional properties; class set operations; cardinality restrictions; description logic entailment).

The 2nd edition adds a dedicated chapter on SKOS (managing controlled vocabularies), expands SPARQL coverage substantially (SPARQL 1.1 features, CONSTRUCT rules, federated queries), and includes four "in the wild" chapters examining real-world ontologies: FOAF, Good Relations, QUDT, and the Open Biological and Biomedical Ontologies. Modeling best practices, common pitfalls, and advanced OWL patterns round out the treatment.

The central organizing metaphor is the "working ontologist" who must navigate the tension between expressivity and tractable inference in a world where data is decentralized and schema is emergent. SPARQL is used throughout as the primary expository vehicle for explaining inference rules, making the book notably approachable for practitioners comfortable with query languages.

## Key Knowledge Objects

- [[rdf]] (concept, high) — W3C triple-based graph data model; primary coverage with serialization formats (Turtle, N-Triples, RDF/XML, RDFa)
- [[rdfs]] (concept, high) — RDF Schema: class/property hierarchy and domain/range constraints
- [[owl]] (framework, high) — Web Ontology Language: full OWL treatment including OWL 2 extensions
- [[skos]] (framework, high) — Simple Knowledge Organization System for controlled vocabularies and thesauri
- [[sparql]] (technique, high) — Deepened treatment: SPARQL 1.1, CONSTRUCT rules, federation, inference patterns
- [[linked-open-data]] (concept, high) — Linked Data principles and the LOD cloud; URI dereferencing
- [[ontology-reasoning]] (technique, high) — Inference engines, entailment regimes, RDFS and OWL inferencing
- [[knowledge-graph]] (concept, high) — Distributed RDF as a knowledge graph; merging data from multiple sources
- [[open-world-assumption]] (principle, high) — OWA as the defining epistemic stance of the Semantic Web vs. closed-world databases
- [[description-logic]] (concept, high) — Theoretical foundation of OWL; decidable fragment of first-order logic
- [[linked-data-principles]] (principle, high) — Berners-Lee's four rules for publishing Linked Data on the Web
- [[semantic-web]] (framework, moderate — could be concept) — The overarching distributed data vision and W3C standards stack

## Key Extractions

1. **The AAA Slogan and the Open World Assumption**: "The Semantic Web isn't about getting everyone to agree, but rather about coping in a world where not everyone will agree, and achieving some degree of interoperability nevertheless." The OWA means that absence of information implies nothing — distinguishing RDF from SQL databases where closed-world reasoning is standard.

2. **RDF as data merging infrastructure**: The core value proposition of RDF is that triples from different publishers can be merged without coordination, because subjects and predicates are URIs. Unlike relational schemas, there is no "alter table" step — any agent can publish triples about any URI.

3. **SPARQL as an inference expository language**: The 2nd edition uses SPARQL CONSTRUCT queries to describe inference rules precisely and practically. The pattern `CONSTRUCT {?x rdf:type :B} WHERE {?x rdf:type :A}` encodes `rdfs:subClassOf` inference — making the semantics of schema languages checkable by practitioners.

4. **RDFS-Plus as the practical OWL sweet spot**: The book introduces "RDFS-Plus" as the subset of OWL most useful in practice: `owl:inverseOf`, `owl:SymmetricProperty`, `owl:TransitiveProperty`, `owl:equivalentClass`, `owl:equivalentProperty`, `owl:sameAs`, `owl:FunctionalProperty`. These cover the majority of real-world ontological relationships without requiring full OWL reasoning.

5. **Description Logic completeness and decidability**: OWL Full is undecidable; OWL DL (and OWL 2's profiles EL, QL, RL) correspond to decidable DL fragments. The working ontologist needs to choose a profile based on reasoning requirements. OWL 2 RL is particularly attractive because it can be implemented with SPARQL rules.

6. **SKOS for vocabulary management**: SKOS provides `skos:Concept`, `skos:broader`, `skos:narrower`, `skos:related`, `skos:prefLabel`, `skos:altLabel`, `skos:scopeNote` — a lightweight graph-based alternative to heavyweight OWL ontologies for thesauri and classification schemes. SKOS does not use OWL class-instance modeling; concepts are individuals.

7. **Named graphs for provenance**: RDF datasets consist of named graphs (URI-identified sets of triples) enabling provenance tracking, versioning, and access control. SPARQL 1.1 GRAPH keyword enables graph-level queries.

## Connection Candidates

- [[rdf]] — extends: this book is the primary treatment of RDF's design philosophy and serialization formats; papadaki-rdf-analytics-survey covers analytics atop RDF
- [[sparql]] — extends: deepens existing SPARQL node with CONSTRUCT rules, federation, SPARQL 1.1 aggregate features from the ontologist's perspective
- [[ontology-reasoning]] — uses: ontology-reasoning is the key technique explained throughout Chs. 6–15; RDFS and OWL inference rules are the substance
- [[knowledge-graph]] — grounds: RDF/RDFS/OWL provide the formal grounding for what knowledge graphs actually represent
- [[directed-graphical-models]] — contrasts-with: RDF graphs and Bayesian networks are both directed graphs over entities; different semantics (open-world vs. probabilistic)
- [[description-logic]] — grounds: description logic is the theoretical foundation for OWL; understanding DL explains OWL's expressivity/tractability tradeoffs
- [[open-world-assumption]] — grounds: OWA is the foundational epistemic principle distinguishing Semantic Web from relational and Prolog-style systems

## Chapters
- [[allemang-semantic-web-ch01]] — Ch. 1 — What is the Semantic Web?
- [[allemang-semantic-web-ch02]] — Ch. 2 — Semantic modeling
- [[allemang-semantic-web-ch03]] — Ch. 3 — RDF — The basis of the Semantic Web
- [[allemang-semantic-web-ch04]] — Ch. 4 — Semantic Web application architecture
- [[allemang-semantic-web-ch05]] — Ch. 5 — Querying the Semantic Web — SPARQL
- [[allemang-semantic-web-ch06]] — Ch. 6 — RDF and inferencing
- [[allemang-semantic-web-ch07]] — Ch. 7 — RDF schema
- [[allemang-semantic-web-ch08]] — Ch. 8 — RDFS-Plus
- [[allemang-semantic-web-ch09]] — Ch. 9 — Using RDFS-Plus in the wild
- [[allemang-semantic-web-ch10]] — Ch. 10 — SKOS — Managing vocabularies with RDFS-Plus
- [[allemang-semantic-web-ch11]] — Ch. 11 — Basic OWL
- [[allemang-semantic-web-ch12]] — Ch. 12 — Counting and sets in OWL
- [[allemang-semantic-web-ch13]] — Ch. 13 — Ontologies on the Web — Putting it all together
- [[allemang-semantic-web-ch14]] — Ch. 14 — Good and bad modeling practices
- [[allemang-semantic-web-ch15]] — Ch. 15 — Expert modeling in OWL
- [[allemang-semantic-web-ch16]] — Ch. 16 — Conclusions
