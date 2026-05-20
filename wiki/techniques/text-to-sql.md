---
title: "Text-to-SQL"
knowledge_type: technique
also_type: []
domain: [knowledge-representation, deep-learning]
tags: [natural-language-processing, sql, question-answering, semantic-parsing, llm, benchmark, nlp, databases]
related_concepts: [semantic-parsing, knowledge-graph-question-answering, sparql]
sources: ["[[sequeda-kg-benchmark-llm-2023]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

A technique for translating natural language questions into SQL queries executable against a relational database, using the database schema (DDL) as context; benchmarked on datasets such as Spider, WikiSQL, and KaggleDBQA, but shown to degrade sharply in enterprise settings with complex schemas and high question complexity.

## Reading Path
- [[sequeda-kg-benchmark-llm-2023]] (unread) — primary treatment in this wiki; GPT-4 zero-shot text-to-SQL achieves only 16.7% AOEA on an enterprise insurance schema; accuracy drops to 0% for queries requiring >4 table joins; compared against text-to-SPARQL over a KG representation
