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
- information-theory
- statistics
id: pkis:concept:asymptotic-equipartition-property
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch05
tags:
- typical-set
- entropy
- source-coding
- law-of-large-numbers
- aep
title: Asymptotic Equipartition Property (AEP)
understanding: 0
---

## Definition
For i.i.d. samples $x_1, \ldots, x_N \sim p(x)$, the **Asymptotic Equipartition Property** states that the sample average log-probability converges in probability to the entropy:

$$-\frac{1}{N}\log p(x_1,\ldots,x_N) \xrightarrow{p} \mathbb{H}(p) \quad \text{as } N \to \infty$$

This means that for large $N$ virtually all probability mass is concentrated on the **$\epsilon$-typical set** $A_\epsilon^N$, defined as sequences satisfying:

$$\mathbb{H}(p) - \epsilon \leq -\frac{1}{N}\log p(x_1,\ldots,x_N) \leq \mathbb{H}(p) + \epsilon$$

The typical set has $|A_\epsilon^N| \approx 2^{N\mathbb{H}(p)}$ elements, each with roughly equal probability $2^{-N\mathbb{H}(p)}$, and $P(A_\epsilon^N) \to 1$.

### Why it matters
The AEP is the probabilistic foundation of Shannon's source coding theorem, justifying why $\mathbb{H}(p)$ bits per symbol are necessary and sufficient for lossless compression. It also shows that most high-dimensional data occupies an exponentially small fraction of the sample space — a key insight for sampling and compression.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]