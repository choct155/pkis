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
- natural-language-processing
- information-theory
id: pkis:concept:language-model-perplexity
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch20
tags:
- language-model
- evaluation
- NLP
- cross-entropy
- information-theory
title: Perplexity of a Language Model
understanding: 0
---

## Definition
For a language model $q$ evaluated on a dataset $\mathcal{D} = \{x_1,\ldots,x_N\}$, **perplexity** is defined as
$$\text{PPL} = 2^{H}, \quad H = -\frac{1}{N}\sum_{n=1}^N \log_2 q(x_n),$$
where $H$ is the empirical cross-entropy (negative log-likelihood) measured in bits.

Perplexity equals the effective number of equally likely next tokens: a model that achieves $H = 3$ bits behaves as if it is always choosing uniformly among $2^3 = 8$ alternatives.

### Why it matters
Perplexity is the canonical evaluation metric for language models. It directly relates to data compression efficiency (via Shannon's source-coding theorem) and is easy to compute for autoregressive models. However, perplexity can be decoupled from perceived quality in other modalities (images, audio), where likelihood and sample quality are known to be poorly correlated.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]