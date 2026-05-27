---
id: "pkis:concept:llm-hallucination"
aliases: []
title: "LLM Hallucination"
knowledge_type: concept
also_type: []
domain: [deep-learning, knowledge-representation]
tags: [llm, reliability, accuracy, trustworthiness, generative-ai, sql, sparql, enterprise-data]
related_concepts: [knowledge-graph, knowledge-graph-question-answering, retrieval-augmented-generation, neurosymbolic-ai]
sources: ["[[sequeda-kg-benchmark-llm-2023]]", "[[sequeda-kg-trust-llm-2025]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: evolving
---

The phenomenon in which a large language model generates plausible-sounding but factually incorrect or ungrounded outputs — in structured query generation contexts, manifesting as invented column names, non-existent table joins, or fabricated values that are syntactically valid but semantically incorrect relative to the actual schema.

## Reading Path
- [[sequeda-kg-benchmark-llm-2023]] (unread) — primary treatment in this wiki; empirically characterizes SQL hallucination types (column name hallucinations, value hallucinations, join hallucinations) vs. SPARQL path inconsistencies; demonstrates that OWL ontology context suppresses class/property hallucinations entirely in SPARQL generation
- [[sequeda-kg-trust-llm-2025]] (unread) — positions KGs as a formal validation framework that detects or prevents hallucinations in enterprise QA; full treatment requires body content access
