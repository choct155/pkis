---
title: "Semantic Web"
knowledge_type: framework
also_type: [concept]
domain: [knowledge-representation]
tags: [semantic-web, rdf, rdfs, owl, skos, sparql, linked-data, w3c, knowledge-representation, distributed-systems]
related_concepts: ["[[rdf]]", "[[rdfs]]", "[[owl]]", "[[skos]]", "[[sparql]]", "[[linked-open-data]]", "[[linked-data-principles]]", "[[open-world-assumption]]", "[[ontology-reasoning]]", "[[knowledge-graph]]"]
sources: ["[[allemang-semantic-web]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

Tim Berners-Lee's vision of a Web extended from documents to data: a distributed, machine-readable layer of structured knowledge where data items are named by URIs, described in RDF, and queryable via SPARQL. The Semantic Web is defined by the AAA slogan (Anyone can say Anything about Any topic), the Open World Assumption, and the network-effect-driven Linked Data model. Its W3C standards stack is: RDF (data model), RDFS (basic schema), OWL (rich ontology), SKOS (vocabulary management), SPARQL (query and inference), and RDFa/JSON-LD (embedded markup). In practice, the Semantic Web vision is most fully realized in the Linked Open Data cloud (billions of RDF triples from government data, DBpedia, Wikidata, life sciences) and in enterprise knowledge graphs (Google Knowledge Graph, industrial ontologies). The tension between the vision's openness and practical interoperability requirements defines the working ontologist's challenge.

Classification note: assigned as framework because the Semantic Web is a coherent system organizing standards, principles, and techniques; also_type concept because it can be discussed as a named idea with a definition and history.

## Connections
- [[rdf]] — uses: RDF is the foundational data model of the Semantic Web
- [[rdfs]] — uses: RDFS provides the basic schema layer enabling class/property inference
- [[owl]] — uses: OWL provides the rich ontological expressiveness for formal knowledge representation
- [[skos]] — uses: SKOS provides vocabulary management for thesauri and classification schemes
- [[sparql]] — uses: SPARQL is the standard query and inference language for Semantic Web data
- [[linked-open-data]] — uses: LOD is the Semantic Web vision instantiated as a global network of linked RDF datasets
- [[open-world-assumption]] — uses: OWA is a foundational epistemic commitment of the Semantic Web
- [[knowledge-graph]] — extends: modern knowledge graphs are the Semantic Web vision applied at enterprise and Web scale

## Reading Path
- [[allemang-semantic-web-ch01]] (unread) — primary conceptual introduction: AAA slogan, OWA, distributed web of data
- [[allemang-semantic-web-ch16]] (unread) — conclusions: synthesizing the Semantic Web standards stack and its trajectory
