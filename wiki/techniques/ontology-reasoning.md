---
title: "Ontological Reasoning"
knowledge_type: technique
also_type: [framework]
domain: [knowledge-representation, symbolic-subsymbolic]
tags: [logic, datalog, knowledge-graphs, rule-based, inference, chase-procedure, explainability, ontology]
related_concepts: [knowledge-graph, neurosymbolic-ai, directed-graphical-models]
sources: ["[[baldazzi-soft-ontological-reasoning]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Logic-based inference over knowledge graphs using formal rule systems (e.g., Datalog and its extensions); the chase procedure incrementally applies tuple-generating dependency rules to a database until fixpoint, deriving all entailed facts with full provenance and explainability.

Classification note: assigned as technique (a procedure with inputs/outputs: rules + data → augmented KG), but also functions as a framework — ontological reasoning systems (Vadalog, OWL reasoners) organize entire KRR pipelines with architectural conventions around rule languages, chase semantics, and query answering.

## Reading Path
- [[baldazzi-soft-ontological-reasoning]] (unread) — primary treatment; the Vadalog/Warded Datalog± system and the chase procedure; soft chase extension using LLMs as semantic unifiers for NL binding identification
