---
title: "A Benchmark to Understand the Role of Knowledge Graphs on Large Language Model's Accuracy for Question Answering on Enterprise SQL Databases"
authors: "Juan F. Sequeda, Dean Allemang, Bryon Jacob"
year: 2023
type: paper
domain: [knowledge-representation, deep-learning]
tags: [knowledge-graphs, llm, question-answering, text-to-sql, sparql, benchmark, enterprise-data, ontology, r2rml, owl, accuracy, hallucination, gpt-4]
source_url: ""
drive_id: "1UU3sRe8QaDPbct9kddNyIo29v6WfKmMt"
drive_path: "PKIS/sources/papers/A Benchmark to Understand the Role of Knowledge Graphs on Large Language Model's Accuracy for Question Answering on Enterprise SQL Databases - Sequeda, Allemang.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[knowledge-graph-question-answering]]", "[[text-to-sql]]", "[[r2rml]]", "[[sparql]]", "[[owl]]", "[[retrieval-augmented-generation]]", "[[knowledge-graph]]", "[[formal-ontology]]", "[[llm-hallucination]]"]
---

## Summary

This technical report (data.world, November 2023) by Sequeda, Allemang, and Jacob introduces a benchmark for evaluating LLM accuracy on enterprise question answering over SQL databases, and specifically investigates the contribution of Knowledge Graphs to that accuracy. The central finding is stark: using GPT-4 with zero-shot prompting directly over an enterprise SQL database achieves only 16.7% accuracy (Average Overall Execution Accuracy); providing a Knowledge Graph representation of the same database raises that to 54.2% — a 3.25x improvement.

The benchmark is built around the OMG Property and Casualty Data Model (a standard 199-table insurance domain schema), a subset of 13 tables, 43 natural language question-answer pairs, and a context layer consisting of an OWL ontology (business concepts, attributes, and relationships) plus R2RML mappings (SQL-to-ontology transformation rules) that together define the Knowledge Graph. Questions are classified across a 2x2 complexity quadrant by question complexity (reporting vs. KPIs) and schema complexity (few tables vs. many). For high schema complexity (5+ tables), SQL accuracy collapses to 0% while SPARQL over the KG maintains 35-38%.

The experimental setup uses zero-shot prompts to GPT-4 — for SQL, the DDL is injected; for SPARQL, the OWL ontology is injected — and measures Execution Accuracy (EA) by comparing query results to reference answers rather than comparing generated query syntax. The paper characterizes SQL inaccuracies as hallucinations (column names, values, joins that do not exist) while SPARQL inaccuracies are path inconsistencies (wrong traversal direction or path between correct nodes) — a qualitatively different failure mode. The authors call for the community to treat business context (ontologies + mappings) as a first-class citizen and invest in knowledge graph architecture as a prerequisite to reliable LLM-powered enterprise QA.

## Key Knowledge Objects

- [[knowledge-graph-question-answering]] (problem, high) — the core problem: accurate NL question answering over enterprise databases, benchmarked with and without KG context
- [[text-to-sql]] (technique, high) — translating natural language questions to SQL queries for execution against relational databases; the baseline comparison approach in this benchmark
- [[r2rml]] (technique, high) — W3C standard for defining mappings from relational SQL schemas to RDF/OWL ontologies; the mechanism by which the KG representation of the SQL database is defined
- [[sparql]] (technique, high) — SPARQL over the KG representation is the KG-augmented QA approach; achieves 54.2% vs. 16.7% for SQL
- [[owl]] (framework, high) — OWL ontology as the business context layer that defines concepts, attributes, and relationships of the insurance domain; injected into the LLM prompt
- [[llm-hallucination]] (concept, high) — hallucinations in SQL generation (non-existent column names, values, and join paths) are the primary failure mode for LLMs without KG context; SPARQL errors are path inconsistencies rather than hallucinations
- [[execution-accuracy]] (technique, moderate — could be result) — benchmark scoring metric borrowed from Spider: accuracy is measured on query result equivalence, not query syntax match; extended to OEA and AOEA for non-deterministic LLMs
- [[retrieval-augmented-generation]] (technique, high) — the KG-augmented QA system is a form of context-augmented generation; the OWL ontology serves as the retrieved structured context injected into the prompt
- [[knowledge-graph]] (concept, high) — KG as the semantic layer over enterprise SQL data; provides business context that dramatically reduces LLM hallucinations
- [[formal-ontology]] (concept, high) — OWL ontology as a formal business domain model; the structured representation that GPT-4 can use to generate correct SPARQL

## Key Extractions

1. **Main result**: GPT-4 zero-shot on SQL achieves 16.7% AOEA; GPT-4 zero-shot on KG (SPARQL over OWL ontology via R2RML virtualization) achieves 54.2% AOEA — 3.25x improvement.

2. **Schema complexity collapse**: For questions requiring >4 tables, SQL accuracy drops to exactly 0%; SPARQL maintains 35.7% (Low Question/High Schema) and 38.7% (High Question/High Schema). The KG representation abstracts away join complexity.

3. **Different failure modes**: SQL failures are hallucinations (column names, values, joins that don't exist in the schema); SPARQL failures are path inconsistencies (LLM knows start and end nodes but traverses wrong intermediate path). Notably, no class or property hallucinations were observed in SPARQL — only incorrect paths.

4. **Scoring methodology**: Execution Accuracy (EA) compares result DataFrames, not query syntax. Overall Execution Accuracy (OEA) is EA-rate over repeated runs to account for LLM non-determinism. Average OEA (AOEA) is the mean OEA across a question set.

5. **Context layer components**: OWL file (Turtle serialization) + R2RML file (Turtle serialization) hosted on data.world; the R2RML drives semantic virtualization so SPARQL queries referencing OWL concepts are translated to SQL at runtime.

6. **Design argument**: "Investing in Knowledge Graph provides higher accuracy for LLM powered question answering systems." The authors frame this as a call to treat business context (ontologies + mappings) as first-class citizens managed in data catalog platforms with KG architecture.

7. **Research agenda items**: (a) extending the benchmark to more domains and schemas; (b) testing few-shot/chain-of-thought prompting; (c) comparing open/closed models; (d) extending scoring to partial accuracy; (e) studying explainability with/without KG; (f) reducing the cost of KG investment via LLM-assisted knowledge engineering.

## Connection Candidates

- [[knowledge-graph-question-answering]] — specializes: this benchmark directly operationalizes KGQA as an accuracy measurement problem in the enterprise SQL context; provides concrete AOEA numbers
- [[sparql]] — uses: SPARQL is the KG query language used in the benchmark; GPT-4 generates SPARQL over the OWL ontology via R2RML virtualization
- [[owl]] — uses: OWL ontology is the structured context injected into the LLM prompt; its business semantics are what enable accurate SPARQL generation
- [[retrieval-augmented-generation]] — extends: the KG-augmented QA pipeline is conceptually a structured RAG variant — injecting ontology as context rather than retrieved text chunks
- [[graph-rag]] — contrasts-with: GraphRAG retrieves KG subgraphs for unstructured generation; this paper uses KG as a query schema for structured SPARQL generation — a structured QA vs. generative distinction
- [[neurosymbolic-ai]] — uses: LLM (neural) + OWL/SPARQL (symbolic) hybrid is a neurosymbolic architecture for enterprise QA; this paper provides empirical evidence for the hybrid advantage
- [[semantic-parsing]] — relates: text-to-SPARQL (via OWL ontology) is a form of semantic parsing; this benchmark quantifies the accuracy advantage of ontology-guided semantic parsing over raw DDL-guided SQL parsing
- [[llm-hallucination]] — grounds: the benchmark provides empirical evidence that ontological structure suppresses class/property hallucinations in SPARQL while hallucinations persist in SQL; partial support for the hypothesis that formal structure constrains LLM output
