---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:framework:mixtures-of-experts
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch14
tags:
- mixture-model
- gating-network
- input-dependent-mixing
- soft-splits
- EM
title: Mixtures of Experts
understanding: 0
---

## Definition
$$p(\mathbf{t}|\mathbf{x}) = \sum_{k=1}^{K} \pi_k(\mathbf{x})\,p_k(\mathbf{t}|\mathbf{x})$$

A probabilistic mixture model in which both the component (expert) densities $p_k(\mathbf{t}|\mathbf{x})$ *and* the mixing (gating) coefficients $\pi_k(\mathbf{x})$ are conditioned on the input $\mathbf{x}$ (Jacobs et al., 1991).

### Why it matters
By routing different regions of input space to specialised expert models, mixtures of experts overcome the limitations of both fixed mixture models (constant gates) and hard-split decision trees. Gating functions (typically softmax) implement soft, input-dependent partitioning. The model can be trained by EM, with the M-step for each expert reducing to a weighted regression/classification problem. The hierarchical mixture of experts (HME; Jordan & Jacobs, 1994) extends this to a tree-structured gating hierarchy, recovering a probabilistic decision tree as a special case.

### Connections
Related to mixture density networks, which share hidden units across experts and gates via a neural network, providing softer, non-axis-aligned, potentially nonlinear input-space partitioning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]