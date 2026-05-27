---
id: "pkis:principle:linked-data-principles"
aliases: []
title: "Linked Data Principles"
knowledge_type: principle
also_type: []
domain: [knowledge-representation]
tags: [semantic-web, linked-data, uri, http, rdf, berners-lee, open-data, interoperability]
related_concepts: ["[[rdf]]", "[[linked-open-data]]", "[[sparql]]", "[[semantic-web]]"]
sources: ["[[allemang-semantic-web]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Tim Berners-Lee's four rules for publishing data as Linked Data on the Web: (1) use URIs as names for things; (2) use HTTP URIs so people can look up those names; (3) when someone looks up a URI, provide useful information using the standards (RDF, SPARQL); (4) include links to other URIs so people can discover more things. These principles operationalize the Semantic Web vision at the data publication level, transforming isolated RDF datasets into an interlinked web of data (the LOD cloud). The principles encode an engineering ethic of openness, reusability, and federation that distinguishes Linked Data from private RDF triple stores.

## Connections
- [[rdf]] — uses: Linked Data principles require RDF (or RDF-compatible formats) as the primary representation
- [[linked-open-data]] — grounds: Linked Data principles are the normative basis for LOD publishing; the LOD cloud is their realization at scale
- [[sparql]] — uses: principle 3 (provide useful information) is typically implemented via a SPARQL endpoint
- [[open-world-assumption]] — uses: the openness of Linked Data (anyone can publish about any URI) is the OWA in practice
- [[semantic-web]] — grounds: Linked Data principles operationalize the abstract Semantic Web vision into concrete engineering guidelines

## Reading Path
- [[allemang-semantic-web-ch01]] (unread) — motivating context: the distributed web of data vision that Linked Data principles implement
- [[allemang-semantic-web-ch03]] (unread) — HTTP URIs, namespaces, and identity — the technical substrate of principles 1–2
- [[allemang-semantic-web-ch09]] (unread) — FOAF as a primary Linked Data deployment example
