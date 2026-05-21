---
title: "Execution Accuracy"
knowledge_type: technique
also_type: [result]
domain: [knowledge-representation, deep-learning]
tags: [benchmark, evaluation, nlp, text-to-sql, question-answering, scoring, llm]
related_concepts: [text-to-sql, knowledge-graph-question-answering, semantic-parsing]
sources: ["[[sequeda-kg-benchmark-llm-2023]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

A benchmark scoring method for text-to-query systems (originating from the Spider benchmark) that measures accuracy by comparing the results of an LLM-generated query against the results of a reference query, rather than comparing query syntax; extended to Overall Execution Accuracy (OEA, accuracy rate across repeated runs for a single question) and Average Overall Execution Accuracy (AOEA, mean OEA across a question set) to handle LLM non-determinism.

Classification note: assigned as technique (it is a scoring procedure applied to evaluate query generation systems) but also_type result because it establishes a specific, reproducible measurement — the Sequeda et al. benchmark reports specific AOEA numbers (16.7% SQL vs. 54.2% SPARQL) that constitute empirical claims.

## Reading Path
- [[sequeda-kg-benchmark-llm-2023]] (unread) — primary treatment; defines EA, OEA, and AOEA; reports benchmark results across the 4-quadrant complexity classification; discusses partial accuracy and inaccuracy analysis
