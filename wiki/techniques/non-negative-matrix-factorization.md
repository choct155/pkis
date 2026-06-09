---
aliases:
- NMF
also_type: []
analogous-to:
- iterative-proportional-fitting
contrasts-with:
- principal-component-analysis
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- knowledge-representation
- deep-learning
id: pkis:technique:non-negative-matrix-factorization
knowledge_type: technique
maturity: settled
related_concepts:
- principal-component-analysis
- knowledge-graph-construction
- knowledge-graph
sources:
- '[[barron-legal-rag-nmf]]'
tags:
- dimensionality-reduction
- topic-modeling
- latent-patterns
- matrix-factorization
- interpretability
- clustering
title: Non-Negative Matrix Factorization (NMF)
understanding: 0
uses:
- mm-algorithm
---

A dimensionality reduction technique that factorizes a non-negative matrix V ≈ WH into two non-negative matrices W (basis components) and H (encoding coefficients), yielding interpretable additive parts-based representations; widely used for topic modeling, feature extraction, and pattern discovery from text and embedding matrices.

## Reading Path
- [[barron-legal-rag-nmf]] (unread) — application to legal document topic discovery; NMF applied to word-embedding matrices to extract latent legal topics; hierarchical NMF for multi-granularity topic structure; used to seed legal knowledge graph construction

## Connections
- [[iterative-proportional-fitting]] — analogous-to: the update rules relate to iterative proportional scaling for log-linear models
- [[mm-algorithm]] — uses: multiplicative updates derived as a minorization (MM) procedure for the Poisson log-likelihood
- [[principal-component-analysis]] — contrasts-with: non-negativity yields parts-based bases vs PCA's holistic eigen-bases