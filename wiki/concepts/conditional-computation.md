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
- deep-learning
- model-efficiency
id: pkis:concept:conditional-computation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch12
tags:
- mixture-of-experts
- gating
- sparse-activation
- efficiency
- dynamic-routing
title: Conditional Computation (Dynamic Structure in Neural Networks)
understanding: 0
---

## Definition
Conditional computation refers to network architectures where the subset of parameters or sub-networks activated at inference time depends on the input $\mathbf{x}$:
$$y = f_{\mathcal{S}(\mathbf{x})}(\mathbf{x}), \quad \mathcal{S}(\mathbf{x}) \subseteq \{1,\ldots,K\},$$
where $\mathcal{S}(\mathbf{x})$ is selected by a gating function (hard: argmax / Bernoulli; soft: weighted average). Hard gating reduces FLOPs but introduces non-differentiable routing; soft gating is differentiable but activates all components.

### Why it matters
Offers a route to scale model capacity without proportionally scaling inference cost; precursor to modern Mixture-of-Experts (MoE) layers and sparse activation in large language models; the tension between parallelism and dynamic routing is a central hardware challenge.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]