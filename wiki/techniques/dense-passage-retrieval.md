---
aliases:
- bi-encoder retrieval
- dense retrieval
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
id: pkis:technique:dense-passage-retrieval
knowledge_type: technique
maturity: evolving
needs_canonical_source: true
related_concepts: []
sources: []
tags:
- retrieval
- embeddings
- bi-encoder
- semantic-search
title: Dense Passage Retrieval
understanding: 0
---

## Definition
Retrieval by semantic similarity in a learned embedding space: a bi-encoder maps queries and passages to dense vectors independently, and approximate nearest-neighbour search returns the passages whose vectors are closest to the query's. It captures meaning beyond surface term overlap — handling paraphrase and vocabulary mismatch — but, lacking exact-match grounding, it can surface topically-near-but-wrong passages. This is the complement to lexical (BM25) retrieval; reciprocal rank fusion exploits their independence by combining both.

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