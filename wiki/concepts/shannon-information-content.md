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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
- statistical-learning
id: pkis:concept:shannon-information-content
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- entropy
related_concepts: []
sources:
- mackay-itila-ch04
tags:
- information-content
- surprise
- entropy
- self-information
- bits
title: Shannon Information Content
understanding: 0
---

## Definition
The information content (or "surprise") of a single outcome $x=a_i$ with probability $p_i$:
$$h(x=a_i) \equiv \log_2 \frac{1}{p_i} \quad \text{bits.}$$
Improbable outcomes carry more information than probable ones — observing a rare event tells you more. It is additive over independent events ($h(x,y)=h(x)+h(y)$), which forces the logarithm.

## Relationship to entropy
The **entropy** $H(X)=\sum_i p_i \log_2 \tfrac{1}{p_i}$ is the *expected* (average) Shannon information content of the ensemble: $H(X)=\mathbb{E}[h(x)]$. So information content is the per-outcome quantity; entropy is its mean. This is the bridge from "how surprising is this one outcome" to "how many bits per symbol does this source need."

## Why it matters
Information content is the natural codeword-length target: an optimal code assigns $\approx h(x)$ bits to outcome $x$ (achieved by arithmetic coding, approached by Huffman). It also underlies the typical set — strings whose average information content per symbol is $\approx H$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[entropy]] — prerequisite-of: Entropy is the expected Shannon information content; define h(x) first
[To be populated during integration]