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
- machine-learning
- computational-neuroscience
id: pkis:principle:slowness-principle
instantiates:
- inductive-bias
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch13
tags:
- temporal-coherence
- invariance
- inductive-bias
- self-supervised-learning
title: Slowness Principle
understanding: 0
uses:
- regularization
---

## Definition
Semantically meaningful features of the world vary slowly compared to the raw sensory measurements that encode them; therefore, a learning system should prefer representations $f(\mathbf{x}^{(t)})$ whose temporal derivatives are small.

Formally, add a temporal coherence regulariser to any loss:
$$\mathcal{L}_{\text{slow}} = \lambda \sum_t L\!\left(f(\mathbf{x}^{(t+1)}), f(\mathbf{x}^{(t)})\right)$$
where $L$ is typically mean squared difference.

### Why it matters
The principle motivates SFA as a closed-form instantiation and generalises to any gradient-trained model. It provides an inductive bias that favours invariant, abstract representations — relevant to building perception systems that are robust to low-level fluctuations (illumination, viewpoint, motion blur). Related ideas appear in predictive coding, contrastive predictive coding, and temporal self-supervised learning.

### Limitation
The principle can be too strong: it penalises rapidly changing but genuinely informative features such as object position when velocity is high, potentially discarding useful information.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[regularization]] — uses
- [[inductive-bias]] — instantiates
[To be populated during integration]