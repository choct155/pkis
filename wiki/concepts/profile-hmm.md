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
- bioinformatics
- machine-learning
id: pkis:concept:profile-hmm
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch29
tags:
- HMM
- bioinformatics
- sequence-alignment
- protein-families
title: Profile HMM
understanding: 0
---

## Definition
A specialized HMM for biological sequence analysis in which each position $t$ of a consensus sequence has three hidden states: Match ($M$), Insert ($I$), and Delete ($D$), with position-specific emission distributions:

- $p(y_t = v \mid z_t = M) = \theta_t(v)$ (position-specific scoring matrix)
- $p(y_t = v \mid z_t = I) = 1/V$ (uniform over vocabulary)
- $p(y_t = - \mid z_t = D) = 1$ (gap symbol)

Match and Delete states advance along the consensus; Insert states self-loop. Sequence membership is decided by log-odds score $L(y) = \log p(y \mid \theta)/p(y \mid \mathcal{M}_0)$ computed via the forwards algorithm in $O(T)$. Alignment uses the Viterbi algorithm.

### Why it matters
Profile HMMs are the standard tool in bioinformatics for protein family modeling (e.g., Pfam database), multiple sequence alignment, and homology detection, combining probabilistic inference with evolutionary domain knowledge.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]