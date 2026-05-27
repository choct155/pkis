---
id: "pkis:source:papadaki-rdf-analytics-survey"
aliases: []
title: "A Brief Survey of Methods for Analytics over RDF Knowledge Graphs"
authors: "Maria-Evangelia Papadaki, Yannis Tzitzikas, Michalis Mountantonakis"
year: 2023
type: paper
domain: [knowledge-representation]
tags: [rdf, sparql, linked-data, olap, semantic-web, data-cube, knowledge-graphs, lod-cloud]
doi: "10.3390/analytics2010004"
venue: "Analytics 2(1), 55-74"
drive_id: "1vBh6E-vnHIn-OzO6WjxpL0qoeCcxB_kT"
drive_path: "PKIS/sources/papers/papadaki-rdf-analytics-survey.pdf"
status: read
date_added: 2026-05-20
concepts:
  - "[[knowledge-graph]]"
  - "[[rdf]]"
  - "[[linked-open-data]]"
  - "[[sparql]]"
  - "[[olap]]"
  - "[[faceted-search]]"
---

## Summary

This survey reviews the landscape of analytic methods applied to knowledge graphs expressed in RDF (Resource Description Framework). The authors identify two categories of analytic queries — (A) domain-specific queries (information needs for which the KG was built, expressible in SPARQL) and (B) quality-related queries (completeness, connectivity, freshness metrics across one or more datasets). Against these query types, they organize 45 surveyed systems into five approach categories:

- **C1** — Direct formulation of analytic queries over RDF via SPARQL aggregate extensions
- **C2** — Definition of data cubes over RDF, then OLAP operations (roll-up, drill-down, slice, dice, pivot)
- **C3** — Domain-specific pipelines that construct a KG from heterogeneous sources, then serve fixed analytics (medical, publications, digital humanities)
- **C4** — Publishing statistical data in RDF via standard vocabularies (RDF Data Cube, VoID)
- **C5** — Quality analytics at LOD scale: power-law distributions, dataset discovery, connectivity measurements across hundreds of RDF datasets

The central challenge: RDF data presupposes no single homogeneous schema (different resources have different property sets, multi-valued properties are common, types may be absent), so classical analytical methods (which assume a single uniform dataset) don't transfer cleanly. Analytic queries over RDF must navigate semantic heterogeneity, leverage RDFS inference, and manage completeness and freshness issues.

Key finding: there is very limited work supporting user-friendly, interactive analytics directly over RDF (only two systems found: SynopsViz and SPARKLIS). Most C1 works propose lower-level technical solutions (MapReduce, index structures, materialized views) inaccessible to non-experts. C2 approaches (OLAP over RDF) require expert configuration of the data cube upfront. The most user-accessible systems tend to be the domain-specific pipelines (C3), where the schema is fixed.

Efficiency notes: star-pattern data cubes yield faster SPARQL query times than snowflake pattern, but most RDF cubes are available only in snowflake form. LOD-scale indexes (LODsyndesis: 2B+ triples) take ~7 hours to construct but return connectivity analytics in seconds.

## Key Knowledge Objects

- [[rdf]] (concept/framework, high) — W3C standard triple-based graph data model; foundation for the Semantic Web and Linked Data
- [[sparql]] (technique, high) — Standard query language for RDF; supports GROUP BY, aggregation, federation; SPARQL 1.1 adds complex path expressions
- [[knowledge-graph]] (concept/framework, high) — Graph structure aggregating/integrating data from multiple sources for unified querying and analytics
- [[olap]] (technique/framework, high) — Sec 2.4: data cube model with dimensions, measures, and cube operations (roll-up, drill-down, slice, dice, pivot)
- [[linked-open-data]] (concept, high) — The LOD cloud; Linked Data publishing paradigm connecting RDF datasets via URIs; C5 analytics operate at this scale
- [[faceted-search]] (technique, moderate) — Interactive RDF access method via faceted filtering; discussed as one of several access methods beyond SPARQL (Sec 2.3)

## Key Extractions

1. The core tension: RDF's expressiveness (heterogeneous schemas, multi-valued properties, optional types) is exactly what makes it powerful for integration but difficult for analytics. Classical OLAP assumes a rigid star/snowflake schema that RDF refuses to commit to. (Sec 3.1)

2. The 5-category taxonomy (C1–C5) maps cleanly onto a complexity vs. usability tradeoff: C1/C2 require SPARQL expertise; C3 sacrifices generality for usability; C4/C5 focus on meta-level quality rather than domain content. (Sec 3.2)

3. Star vs. snowflake data cubes over RDF: running SPARQL queries over cubes in star pattern is faster than snowflake pattern (Virtuoso benchmark), but most RDF cubes in the wild use snowflake form — creating a systematic performance gap. (Sec 5.1)

4. LOD-scale connectivity analytics via LODsyndesis: 400+ RDF datasets indexed once (~7 hrs), then connectivity queries (common entities, coverage, dataset discovery) return in seconds. The index captures the "semantic warehouse" connectivity layer. (Sec 4.6, 5.1)

5. SPARQL aggregate extensions (GROUP BY, COUNT, SUM, AVG, MIN, MAX, GROUP_CONCAT) are the building blocks for type-A analytic queries — standard SQL-like aggregation, but operating on a graph rather than a table. (Sec 2.2)

6. Two underexplored integration opportunities visible from the survey: (a) ML methods for KG construction (entity alignment, relation extraction) are assumed as prior pipeline steps, not analyzed here; (b) using KG structure for explainable ML is flagged as future direction (Tiddi & Schlobach 2022 cited). (Sec 5.1, Ref 89)

## Sections

| Sec. | Title | Key topics |
|---|---|---|
| 1 | Introduction | KG integration trend; paper scope and structure |
| 2 | Background | RDF, SPARQL, access methods over RDF, OLAP, related surveys |
| 3 | Challenges and Approaches | Core challenges; 5-category taxonomy; 2 query category types |
| 4.2 | C1: Direct RDF Analytics | SPARQL aggregation systems; MapReduce, materialized views, vertex-centric |
| 4.3 | C2: Data Cubes over RDF | OLAP over RDF; QB4OLAP; CubeViz; Power BI; Tableau |
| 4.4 | C3: Domain-Specific Pipelines | Medical (PhLeGrA, cancer, COVID KGs); publications (OpenAIRE, ORKG); cultural |
| 4.5 | C4: Statistical Data Publishing | RDF Data Cube vocabulary; VoID vocabulary; Aether; Loupe; LODStats |
| 4.6 | C5: LOD Scale Quality Analytics | LODVader; LODStats; LOD-a-Lot; LODsyndesis; power-law distributions |
| 5 | Efficiency and Visualization | Query performance patterns; chart types used across categories |
| 6 | Conclusions | Trends; open problems; future directions |

## Connection Candidates

- [[directed-graphical-models]] — Both RDF KGs and Bayesian networks encode structured relational knowledge, but for different purposes: RDF KGs are open-world fact stores; BNs are closed-world probabilistic models. `contrasts-with` edge warranted after deepening.
- [[em-algorithm]] — C3 pipelines often use ML (including EM for clustering/alignment) as preprocessing steps for KG construction; the survey doesn't cover this in depth.
- [[knowledge-representation]] domain — this paper is the first systematic entry in this domain; establishes vocabulary for future papers on OWL, ontology engineering, causal graphs expressed as KGs.

## Awaiting Classification

*(none — all extracted nodes assessed high or moderate confidence)*
