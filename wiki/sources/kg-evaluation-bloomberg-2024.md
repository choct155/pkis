---
id: "pkis:source:kg-evaluation-bloomberg-2024"
aliases: []
title: "Knowledge Graph Evaluation: Measuring Current State and Improvements"
authors: "Bloomberg B-FAIR Team"
year: 2024
type: article
domain: [knowledge-representation]
tags: [knowledge-graphs, ontology-evaluation, ontology-quality, kg-metrics, fitness-for-purpose, enterprise-kg, ontology-maturity, structural-metrics, competency-questions]
source_url: ""
drive_id: "1-uYZyw-9pAcN49SQROFYXSU0r88XpCxh"
drive_path: "PKIS/sources/papers/Knowledge Graph Evaluation.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[ontology-quality-dimensions]]", "[[competency-questions]]", "[[kg-maturity-model]]", "[[knowledge-graph]]", "[[ontology-reasoning]]", "[[formal-ontology]]"]
---

## Summary

This is an internal Bloomberg strategy and working document produced by the B-FAIR KG initiative (2024) that establishes a measurement framework for evaluating the Bloomberg Semantic Model (BSM) and Bloomberg Semantic Repository (BSR) knowledge graph. The document synthesizes relevant academic literature on ontology evaluation with pragmatic organizational concerns, arriving at a phased approach to KG measurement that begins with operational (structural + usage) metrics and matures toward task-based, fitness-for-purpose assessments.

The document identifies seven quality dimensions for knowledge graphs — accuracy, completeness, conciseness, adaptability, clarity, computational efficiency, and consistency — drawn from a HAL-hosted survey on ontology evaluation methods. It distinguishes four evaluation method families: (1) comparison to gold-standard reference ontologies, (2) corpus-based comparison, (3) task-based/fitness-for-purpose methods, and (4) criteria-based/structural methods. A phased roadmap is proposed: Phase 1 focuses on structural inventory counts (class/property/domain counts, KG shape metrics, graph-theoretic properties) and usage-based metrics (BSR service calls, ERM invocations, feature store hydrations); later phases shift to outcome-based assessment tied to specific use cases (Search, Field Discovery, Cross-Domain BQL Queries, Query Understanding, Standardized Metadata).

The document also addresses KG maturity — not just quality — citing the Ontology Maturing Process Model with three relevant phases at Bloomberg: folksonomy tagging, formalization into SKOS taxonomies, and specification into OWL/RDFS class structures. It presents baseline statistics for the BSM (155 classes, 159 properties, relation diversity ratio of 0.73) and describes supply-side and demand-side quality control approaches including linting and reasoning validation via HermiT/Pellet. Meeting notes from April–June 2024 document the collaborative process of defining metrics, connecting them to use cases, and negotiating the tension between structural counts and externally meaningful outcome measures.

## Key Knowledge Objects

- [[ontology-quality-dimensions]] (concept, high) — the seven recognized dimensions (accuracy, completeness, conciseness, adaptability, clarity, computational efficiency, consistency) used to characterize KG/ontology quality
- [[competency-questions]] (technique, high) — a validation technique that asks whether the KG can answer a predefined set of representative domain questions; used both for regression testing and for defining fitness-for-purpose
- [[kg-maturity-model]] (framework, moderate — could be concept) — a staged model of organizational KG adoption progressing from folksonomy tagging through SKOS formalization to OWL specification; adapted from the Ontology Maturing Process Model
- [[knowledge-graph]] (concept, high) — KG as enterprise data product evaluated along multiple quality dimensions
- [[ontology-reasoning]] (technique, high) — HermiT/Pellet reasoning used as supply-side quality validation (checking for inconsistencies in the BSM)
- [[formal-ontology]] (concept, high) — OWL/RDFS class structure as the specification-phase target in the maturity model

## Key Extractions

1. **Seven quality dimensions**: The HAL survey cited identifies accuracy, completeness, conciseness, adaptability, clarity, computational efficiency, and consistency as the core KG evaluation dimensions. Bloomberg adopts these as its evaluation framework.

2. **Four evaluation method families**: Gold-standard comparison, corpus-based comparison, task-based/fitness-for-purpose, and criteria-based structural methods — each with different strengths across the seven dimensions.

3. **Phased measurement strategy**: Phase 1 uses structural inventory metrics (class/property counts, KG shape metrics like instantiated class ratio and relation diversity, graph properties like average degree) and usage metrics (BSR service calls, ERM invocations). Later phases move to outcome-based measures tied to use cases.

4. **Baseline BSM statistics (2024)**: 155 classes, 159 properties (89 object, 70 datatype), 12 root classes, 125 leaf classes, relation diversity (RR) of 0.73 — meaning 73% of relationships in the ontology are non-inheritance relationships.

5. **Ontology maturity phases**: Folksonomy (informal tags) → Formalization (SKOS controlled vocabularies/taxonomies) → Specification (OWL/RDFS with properties, axioms, restrictions). Bloomberg operates primarily in the formalization phase, selectively moving to specification.

6. **Competency questions as regression tests**: The document proposes using competency questions as periodic regression tests to ensure the model remains "performant" for its intended query use cases, rather than treating them only as design-time requirements.

7. **Thin ontology design principle**: Bloomberg BSM is intentionally designed as a "thin ontology" (limited number of classes, few data properties due to a UFM integration plan) — this constrains which structural metrics are meaningful and requires metrics to account for intentional deviation from typical ontology patterns.

## Connection Candidates

- [[knowledge-graph]] — uses: the Bloomberg BSM/BSR is the KG being evaluated; this source directly discusses multi-dimensional KG quality assessment
- [[formal-ontology]] — uses: OWL/RDFS is the target specification-phase representation in Bloomberg's maturity model; HermiT/Pellet validate its logical consistency
- [[ontology-reasoning]] — uses: reasoning validation (HermiT, Pellet) is a supply-side quality control approach for the BSM
- [[skos]] — uses: SKOS taxonomies are the intermediate formalization step in Bloomberg's maturity model between folksonomy tags and full OWL specification
- [[semantic-web]] — grounds: the Semantic Web stack (RDF, SKOS, OWL) provides the technological context for Bloomberg's BSM architecture
- [[knowledge-graph-question-answering]] — connects: competency questions as a demand-side KG evaluation technique are a form of structured QA; this bridges KG quality assessment to the KGQA problem
