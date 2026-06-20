---
aliases: []
also_type: []
applies:
- feed-forward-neural-network
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-20'
domain:
- machine-learning
- approximation-theory
id: pkis:result:universal-approximation-theorem-nn
instantiates:
- universal-approximation-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch05
- nielsen-nndl-ch04
tags:
- expressiveness
- neural-networks
- function-approximation
title: Universal Approximation Theorem (Neural Networks)
understanding: 0
---

## Definition
**Theorem (Cybenko 1989; Hornik et al. 1989).** For any continuous function $f$ on a compact subset of $\mathbb{R}^D$ and any $\varepsilon > 0$, there exists a two-layer network with a finite number $M$ of sigmoidal hidden units and linear output units such that
$$\sup_{\mathbf{x}} |y(\mathbf{x}, \mathbf{w}) - f(\mathbf{x})| < \varepsilon.$$
The result holds for a wide class of non-polynomial activation functions.

Despite guaranteeing existence of a sufficiently wide single-hidden-layer approximator, the theorem gives no prescription for finding suitable weights $\mathbf{w}$ from finite data.

### Why it matters
Provides theoretical justification for neural networks as general-purpose function approximators, motivating gradient-based training rather than hand-crafted feature engineering. It does not, however, address sample efficiency, optimisation difficulty, or the benefits of depth.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[universal-approximation-theorem]] — instantiates
- [[feed-forward-neural-network]] — applies
[To be populated during integration]