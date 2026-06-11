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
contrasts-with:
- word-embeddings
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- nlp
- information-retrieval
extends:
- bag-of-words-model
id: pkis:technique:tf-idf
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch01
tags:
- text-preprocessing
- document-representation
- vector-space-model
- nlp
title: TF-IDF Weighting
understanding: 0
uses:
- one-hot-encoding
---

## Definition
A document-term weighting scheme that down-weights terms frequent across the corpus while up-weighting terms informative for a specific document:
$$\text{TFIDF}_{ij} = \log(\text{TF}_{ij}+1) \times \text{IDF}_i, \quad \text{IDF}_i = \log\frac{N}{1+\text{DF}_i}$$
where $\text{TF}_{ij}$ is the count of term $i$ in document $j$, $N$ is the total number of documents, and $\text{DF}_i$ is the number of documents containing term $i$.

### Why it matters
Raw term frequencies give undue influence to stop words. TF-IDF produces a sparse, weighted vector space model that substantially improves the discriminability of document representations for text classification, retrieval, and clustering, at essentially zero computational cost.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[word-embeddings]] — contrasts-with
- [[one-hot-encoding]] — uses
- [[bag-of-words-model]] — extends
[To be populated during integration]