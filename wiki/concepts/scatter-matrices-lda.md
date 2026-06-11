---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:concept:scatter-matrices-lda
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch09
tags:
- scatter-matrix
- LDA
- dimensionality-reduction
- supervised-learning
title: Between-Class and Within-Class Scatter Matrices
understanding: 0
---

## Definition
$$S_B = \sum_{c=1}^C N_c (\mu_c - \mu)(\mu_c - \mu)^\top \quad (\text{between-class scatter})$$
$$S_W = \sum_{c=1}^C \sum_{n:y_n=c} (x_n - \mu_c)(x_n-\mu_c)^\top \quad (\text{within-class scatter})$$

The **between-class scatter matrix** $S_B$ measures how spread the class means are around the grand mean; the **within-class scatter matrix** $S_W$ measures the total spread of examples around their respective class means.

### Why it matters
These two matrices are the fundamental building blocks of Fisher's LDA and related supervised dimensionality reduction methods. The Fisher criterion $|S_B|/|S_W|$ (or its scalar analogue $w^\top S_B w / w^\top S_W w$) captures the intuition that good projections simultaneously pull class means apart and squeeze within-class variance.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]