---
aliases: []
also_type:
- framework
coverage: 4
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- knowledge-representation
- symbolic-subsymbolic
id: pkis:technique:ontology-reasoning
knowledge_type: technique
maturity: settled
related_concepts:
- knowledge-graph
- neurosymbolic-ai
- directed-graphical-models
sources:
- '[[baldazzi-soft-ontological-reasoning]]'
- '[[allemang-semantic-web]]'
- '[[cimiano-ontology-nlp]]'
- '[[kg-evaluation-bloomberg-2024]]'
- allemang-semantic-web-ch06
- allemang-semantic-web-ch07
- allemang-semantic-web-ch11
- allemang-semantic-web-ch15
- cimiano-ontology-nlp-ch01
- cimiano-ontology-nlp-ch07
tags:
- logic
- datalog
- knowledge-graphs
- rule-based
- inference
- chase-procedure
- explainability
- ontology
title: Ontological Reasoning
understanding: 0
---

Logic-based inference over knowledge graphs using formal rule systems (e.g., Datalog and its extensions); the chase procedure incrementally applies tuple-generating dependency rules to a database until fixpoint, deriving all entailed facts with full provenance and explainability.

Classification note: assigned as technique (a procedure with inputs/outputs: rules + data → augmented KG), but also functions as a framework — ontological reasoning systems (Vadalog, OWL reasoners) organize entire KRR pipelines with architectural conventions around rule languages, chase semantics, and query answering.

## Reading Path
- [[baldazzi-soft-ontological-reasoning]] (unread) — primary treatment; the Vadalog/Warded Datalog± system and the chase procedure; soft chase extension using LLMs as semantic unifiers for NL binding identification
- [[allemang-semantic-web-ch06]] (unread) — SPARQL as the expository language for RDF inference rules; asserted vs. inferred triples
- [[allemang-semantic-web-ch07]] (unread) — RDFS inference rules: subClassOf, subPropertyOf, domain, range propagation
- [[allemang-semantic-web-ch11]] (unread) — OWL inference: property restrictions, individual identity under OWA
- [[allemang-semantic-web-ch15]] (unread) — OWL 2 profiles and tractable reasoning regimes (EL, QL, RL)
- [[cimiano-ontology-nlp-ch07]] (unread) — extends ontological reasoning to DL-based OWL reasoning for NL ambiguity resolution; contrasts with Datalog/chase approach in [[baldazzi-soft-ontological-reasoning]]
- [[kg-evaluation-bloomberg-2024]] (unread) — HermiT and Pellet used as supply-side quality control validators for the Bloomberg BSM; reasoning used to detect logical inconsistencies rather than to derive new facts