---
aliases: []
also_type: []
applies:
- encoder-decoder-architecture
- machine-translation
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- nlp
- search
generalizes:
- greedy-best-first-search
id: pkis:technique:beam-search
instantiates:
- beam-search-decoding
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch15
tags:
- decoding
- machine-translation
- sequence-generation
- MAP
title: Beam Search Decoding
understanding: 0
---

## Definition
Beam search approximates the MAP sequence $y^*_{1:T} = \arg\max_{y_{1:T}} p(y_{1:T}|x)$ by maintaining a beam of the $K$ highest-scoring partial hypotheses at each step and expanding each into all $V$ possible next tokens, keeping only the top $K$:

$$\text{BeamScore}(y_{1:t}) = \log p(y_{1:t}|x) = \sum_{s=1}^t \log p(y_s | y_{1:s-1}, x)$$

Time complexity is $O(TVK)$, compared to $O(V^T)$ for exact search.

### Why it matters
Greedy decoding is suboptimal because the locally best token at step $t$ may not lie on the globally best path. Beam search trades a constant factor in compute for substantially better sequences in practice, and is the standard decoding algorithm for neural machine translation and text generation. Stochastic variants (stochastic beam search using Gumbel noise, diverse beam search) trade optimality for output diversity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[beam-search-decoding]] — instantiates
- [[machine-translation]] — applies
- [[greedy-best-first-search]] — generalizes
- [[encoder-decoder-architecture]] — applies
[To be populated during integration]