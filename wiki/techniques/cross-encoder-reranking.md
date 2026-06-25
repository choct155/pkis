---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 0
date_created: '2026-06-25'
date_updated: '2026-06-25'
domain:
- machine-learning
- knowledge-representation
id: pkis:technique:cross-encoder-reranking
knowledge_type: technique
maturity: evolving
needs_canonical_source: true
related_concepts: []
sources: []
tags:
- retrieval
- reranking
- cross-encoder
- neural-ir
title: Cross-Encoder Reranking
understanding: 0
---

## Definition
A second-stage retrieval refinement that re-scores a candidate set by feeding each (query, document) pair jointly through a transformer that outputs a single relevance score. Unlike a bi-encoder — which embeds query and document independently and compares by cosine similarity — a cross-encoder attends over the concatenated pair, capturing fine-grained term interactions. This is far more precise but too expensive to run over a whole corpus, so it is applied only to the top-k candidates from a cheap first-stage retriever. It is the optional rerank stage in PKIS's search pipeline.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]

## Needs Canonical Source
This stub was created without a source. Suggested references:

**Already in corpus:**
[none in corpus]

**External candidates (Semantic Scholar):**
[none found]