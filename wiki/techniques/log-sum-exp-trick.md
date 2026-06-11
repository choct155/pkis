---
aliases: []
also_type: []
applies:
- softmax-function
- cross-entropy-loss
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
- numerical-methods
- machine-learning
- probability-theory
id: pkis:technique:log-sum-exp-trick
instantiates:
- log-scale-computation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch02
tags:
- numerical-stability
- softmax
- log-sum-exp
- floating-point
title: Log-Sum-Exp (LSE) Trick
understanding: 0
uses:
- partition-function
---

## Definition
$$\log\sum_{c=1}^{C}\exp(a_c) = m + \log\sum_{c=1}^{C}\exp(a_c - m), \quad m = \max_c a_c$$

The **log-sum-exp trick** stabilizes the computation of $\text{lse}(\mathbf{a})\triangleq\log\sum_c\exp(a_c)$ by subtracting the maximum logit before exponentiation. This ensures the largest exponentiated value equals $e^0=1$ (no overflow) and suppresses underflow gracefully. Probabilities are then recovered as $p_c = \exp(a_c - \text{lse}(\mathbf{a}))$.

### Why it matters
Without this trick, softmax computation fails catastrophically at logit magnitudes $\gtrsim 700$ (IEEE 754 double overflow) or $\lesssim -700$ (underflow to zero). The LSE function is ubiquitous in probabilistic computing: log-likelihood evaluation, logsumexp in message passing, log-normalizers of exponential families, and cross-entropy loss implementations in all major deep-learning frameworks use this identity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[log-scale-computation]] — instantiates
- [[partition-function]] — uses
- [[cross-entropy-loss]] — applies
- [[softmax-function]] — applies
[To be populated during integration]