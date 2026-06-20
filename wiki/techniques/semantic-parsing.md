---
aliases: []
also_type: []
applies:
- probabilistic-context-free-grammar
coverage: 2
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- knowledge-representation
- symbolic-subsymbolic
id: pkis:technique:semantic-parsing
knowledge_type: technique
maturity: evolving
related_concepts:
- sparql
- formal-ontology
- ontology-lexicon
- discourse-representation-theory
- knowledge-graph-question-answering
sources:
- '[[cimiano-ontology-nlp]]'
- '[[sequeda-kg-benchmark-llm-2023]]'
- yih-the-2016
- cimiano-ontology-nlp-ch01
- cimiano-ontology-nlp-ch06
- cimiano-ontology-nlp-ch09
- cimiano-ontology-nlp-ch10
tags:
- natural-language-processing
- sparql
- question-answering
- formal-semantics
- ontology
- nlp
- meaning-representation
title: Semantic Parsing
understanding: 0
---

Semantic parsing is the technique of mapping a natural language utterance to a formal meaning representation (e.g., logical form, SPARQL query, lambda calculus expression) that can be executed against a structured knowledge source to retrieve answers or verify claims.

## Reading Path
- [[cimiano-ontology-nlp-ch09]] (unread) — primary treatment in this context; full compositional DUDES-to-SPARQL pipeline for NL question answering over RDF data
- [[cimiano-ontology-nlp-ch03]] (unread) — prerequisite: DUDES semantic representation formalism that is the intermediate representation before translation to SPARQL
- [[sequeda-kg-benchmark-llm-2023]] (unread) — text-to-SPARQL via OWL context as semantic parsing variant; GPT-4 zero-shot achieves 54.2% execution accuracy; contrasted with text-to-SQL to quantify the advantage of formal ontology context

## Connections
- [[probabilistic-context-free-grammar]] — applies