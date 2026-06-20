---
aliases: []
also_type: []
coverage: 4
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- knowledge-representation
extends:
- semantic-network
id: pkis:concept:description-logic
instantiates:
- expressiveness-tractability-tradeoff
knowledge_type: concept
maturity: settled
related_concepts:
- formal-ontology
- ontology-reasoning
- rdf
- knowledge-graph
sources:
- '[[cimiano-ontology-nlp]]'
- '[[allemang-semantic-web]]'
- '[[delong-nsai-kg-survey-2024]]'
- '[[luong-ontology-constrained-neural-2026]]'
- allemang-semantic-web-ch11
- allemang-semantic-web-ch12
- allemang-semantic-web-ch15
- cimiano-ontology-nlp-ch02
- cimiano-ontology-nlp-ch07
- cimiano-ontology-nlp-ch08
specializes:
- first-order-logic
tags:
- logic
- ontology
- owl
- description-logic
- formal-semantics
- decidability
- knowledge-representation
title: Description Logic
understanding: 0
---

Description Logics (DLs) are a family of decidable fragments of first-order logic used for representing structured domain knowledge; they form the logical foundation of the OWL family of ontology languages, with OWL DL corresponding to SHOIN(D) and OWL 2 DL to SROIQ(D).

## Reading Path
- [[cimiano-ontology-nlp-ch02]] (unread) — primary treatment; formal semantics of ALC, SHOIN(D), SROIQ(D); constructors for class expressions, role restrictions, nominals, and concrete domains
- [[allemang-semantic-web-ch11]] (unread) — practitioner introduction to DL as motivation for OWL's property restrictions and individual identity
- [[allemang-semantic-web-ch12]] (unread) — cardinality and set operations as the DL constructs with highest practical modeling impact
- [[allemang-semantic-web-ch15]] (unread) — OWL 2 DL profiles (EL, QL, RL) corresponding to tractable DL sub-languages
- [[delong-nsai-kg-survey-2024]] (unread) — DL-based ontologies (OWL, OWL 2 EL) as semantic framework for KG reasoning; EL fragment for polynomial-time inference in biomedical KGs
- [[luong-ontology-constrained-neural-2026]] (unread) — three-layer enterprise ontology grounded in DL semantics; formal constraints on LLM agent inputs

## Connections
- [[expressiveness-tractability-tradeoff]] — instantiates: DLs restrict negation/disjunction to keep subsumption polynomial — a canonical expressiveness/tractability instance
- [[semantic-network]] — extends: description logics evolved from semantic networks to formalize their meaning while keeping taxonomy central
- [[first-order-logic]] — specializes