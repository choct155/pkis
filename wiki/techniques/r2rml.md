---
title: "R2RML (RDB-to-RDF Mapping Language)"
knowledge_type: technique
also_type: []
domain: [knowledge-representation]
tags: [rdf, sql, mapping, semantic-web, w3c-standard, ontology, knowledge-graph-construction, virtualization]
related_concepts: [rdf, owl, sparql, knowledge-graph, knowledge-graph-construction]
sources: ["[[sequeda-kg-benchmark-llm-2023]]", "[[sequeda-kg-trust-llm-2025]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

A W3C standard language for defining declarative transformation rules from relational SQL schemas to RDF; R2RML mappings specify how tables, columns, and foreign-key relationships map to OWL classes, properties, and individuals, enabling either materialized KG construction (ETL) or semantic virtualization (query-time SQL translation via SPARQL endpoints).

## Reading Path
- [[sequeda-kg-benchmark-llm-2023]] (unread) — primary treatment in this wiki; R2RML used to define the KG context layer over the OMG P&C insurance schema; drives semantic virtualization in data.world so SPARQL queries over OWL classes are translated to SQL at runtime; direct evidence that R2RML-defined KG raises LLM accuracy from 16.7% to 54.2%
- [[sequeda-kg-trust-llm-2025]] (unread) — R2RML cited as a keyword/component of the trust infrastructure; full treatment requires body content access
