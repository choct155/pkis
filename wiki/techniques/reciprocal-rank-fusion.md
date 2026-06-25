---
aliases:
- RRF
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
id: pkis:technique:reciprocal-rank-fusion
knowledge_type: technique
maturity: evolving
needs_canonical_source: true
related_concepts: []
sources: []
tags:
- retrieval
- fusion
- rank-aggregation
- hybrid-search
title: Reciprocal Rank Fusion
understanding: 0
---

## Definition
A rank-aggregation method that merges several ranked candidate lists into one by summing 1/(k + rank) across the lists for each item (k ≈ 60). It needs no score calibration between retrievers — only their rank positions — which makes it a robust default for fusing lexical (BM25) and dense (embedding) retrieval. An item ranked highly by several retrievers accumulates weight, while the constant k damps the influence of deep ranks. It is the fusion stage in PKIS's hybrid search.

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