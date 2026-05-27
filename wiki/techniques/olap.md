---
id: "pkis:technique:olap"
aliases: ["Online Analytical Processing"]
title: "OLAP (Online Analytical Processing)"
knowledge_type: technique
also_type: [framework]
domain: [knowledge-representation, statistical-learning]
tags: [data-cube, business-intelligence, multidimensional-analysis, aggregation]
related_concepts: []
sources: ["[[papadaki-rdf-analytics-survey]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Analytical framework organizing data into multidimensional cubes with dimensions (analysis attributes) and measures (pre-aggregated values of interest); supports five core operations: roll-up (aggregate up a hierarchy), drill-down (descend to more detail), slice (select one dimension value), dice (subcube from multiple selections), and pivot (reorient the view). Designed for fast interactive analysis of large datasets by pre-computing aggregations; applied to RDF via QB4OLAP and the RDF Data Cube vocabulary to bridge the graph-based and multidimensional data models.
