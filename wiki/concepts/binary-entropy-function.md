---
aliases: []
also_type: []
applies:
- binomial-distribution
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
- probability
id: pkis:concept:binary-entropy-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch06
specializes:
- entropy
tags:
- entropy
- bernoulli
- binary
title: Binary Entropy Function
understanding: 0
uses:
- fanos-inequality
---

## Definition
$$\mathbb{H}(\theta) \triangleq -[\theta \log_2 \theta + (1-\theta)\log_2(1-\theta)]$$

The entropy of a Bernoulli random variable with success probability $\theta$, achieving its maximum of 1 bit at $\theta = 0.5$ (fair coin) and its minimum of 0 at $\theta \in \{0,1\}$ (degenerate).

### Why it matters
Serves as the canonical one-dimensional illustration of entropy: it is symmetric around $\theta=0.5$, strictly concave, and equals zero only at degenerate distributions. It appears in bounds throughout information theory (e.g., Fano's inequality, sphere-packing bounds) and is the building block for understanding how uncertainty scales with bias in binary classification.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[binomial-distribution]] — applies
- [[fanos-inequality]] — uses
- [[entropy]] — specializes
[To be populated during integration]