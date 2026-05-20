---
title: "SPARQL"
knowledge_type: technique
also_type: []
domain: [knowledge-representation]
tags: [rdf, query-language, semantic-web, aggregation, federation]
related_concepts: []
sources: ["[[papadaki-rdf-analytics-survey]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

W3C standard query language for RDF data; uses graph pattern matching over triple stores. SPARQL 1.1 adds aggregate functions (COUNT, SUM, AVG, MIN, MAX, GROUP_CONCAT), GROUP BY, HAVING, subqueries, regular path expressions, and federated querying across SPARQL endpoints. The primary mechanism for analytic queries over knowledge graphs, with limitations around schema heterogeneity and scalability for complex aggregations over large RDF datasets.
