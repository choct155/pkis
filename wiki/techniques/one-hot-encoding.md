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
- machine-learning
- feature-engineering
id: pkis:technique:one-hot-encoding
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- bag-of-words-model
- feature-crosses
related_concepts: []
sources:
- murphy-pml1-intro-ch01
specializes:
- feature-engineering
tags:
- categorical-data
- preprocessing
- dummy-encoding
- feature-engineering
title: One-Hot Encoding
understanding: 0
---

## Definition
A preprocessing transformation that maps a categorical variable $x \in \{1,\ldots,K\}$ to a binary vector of length $K$:
$$\text{one-hot}(x) = [\mathbb{I}(x=1),\, \mathbb{I}(x=2),\, \ldots,\, \mathbb{I}(x=K)] \in \{0,1\}^K$$
Exactly one component equals 1 (the active category) and all others equal 0.

### Why it matters
Categorical variables have no natural numeric ordering, so feeding raw integer codes to linear models introduces spurious ordinal structure. One-hot encoding removes this artefact and allows linear models to learn independent weights for each category. It is the standard first step for tabular categorical data and the basis for bag-of-words and word-count representations in NLP.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[feature-crosses]] — prerequisite-of
- [[word-embeddings]] — contrasts-with
- [[feature-engineering]] — specializes
- [[bag-of-words-model]] — prerequisite-of
[To be populated during integration]