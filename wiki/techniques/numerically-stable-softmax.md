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
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- numerical-computation
- deep-learning
id: pkis:technique:numerically-stable-softmax
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch04
tags:
- softmax
- log-sum-exp
- numerical-stability
- floating-point
title: Numerically Stable Softmax
understanding: 0
---

## Definition
Replace the raw softmax computation with a shifted version:

$$\text{softmax}(\mathbf{x})_i = \frac{\exp(x_i - c)}{\sum_j \exp(x_j - c)}, \quad c = \max_k x_k.$$

Subtracting $c$ is algebraically neutral (cancels in numerator and denominator) but ensures the largest exponent argument is $0$, preventing overflow, while keeping at least one denominator term equal to $1$, preventing denominator underflow.

### Why it matters
Without this trick, softmax fails for inputs with large positive values (overflow) or large negative values (underflow leading to $0/0$). Log-softmax requires a separate stable implementation to avoid $\log(0) = -\infty$. This pattern—algebraic equivalence + numerical re-centering—generalises to log-sum-exp computations throughout probabilistic ML.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]