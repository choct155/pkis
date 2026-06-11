---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- information-theory
- machine-learning
- representation-learning
id: pkis:principle:information-bottleneck-principle
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch32
tags:
- mutual-information
- compression
- VIB
- robustness
- rate-distortion
title: Information Bottleneck Principle
understanding: 0
---

## Definition
Given input $X$, representation $Z$, and target $Y$, the information bottleneck (IB) seeks the representation that is maximally predictive of $Y$ while being maximally compressed about $X$:

$$\max_{p(z|x)} \; I(Z; Y) - \beta\, I(X; Z), \quad \beta \geq 0.$$

The Lagrange multiplier $\beta$ controls the compression–prediction tradeoff. The variational information bottleneck (VIB) approximates this objective using variational bounds, enabling optimisation with stochastic encoders $q_\phi(z|x)$.

### Why it matters
The IB principle provides a formal information-theoretic criterion for which bits of the input a representation should preserve: exactly those bits that are predictive of the label. Applied to deep networks, VIB has been shown to improve robustness to adversarial examples and distributional shift.

### Limitations
For deterministic encoders mapping continuous inputs, $I(X;Z) = \infty$, making the compression term vacuous. The principle has more teeth for stochastic encoders or discrete representations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]