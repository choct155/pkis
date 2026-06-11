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
- multimodal-learning
id: pkis:concept:film-feature-wise-linear-modulation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch16
tags:
- conditioning
- multiplicative-interaction
- feature-modulation
- FiLM
- hypernetwork
title: Feature-wise Linear Modulation (FiLM)
understanding: 0
---

## Definition
$$f(x, z) = a(z) \odot x + b(z)$$

FiLM (Feature-wise Linear Modulation) is a conditioning mechanism in which a secondary input $z$ (e.g., a language instruction or class label) generates per-channel scale $a(z)$ and shift $b(z)$ vectors that are applied elementwise to the primary feature map $x$.

### Why it matters
FiLM is a lightweight but powerful form of multiplicative interaction that allows one modality or context signal to modulate the processing of another. It is a special case of a hypernetwork (where the secondary input generates affine parameters for the primary network) and has been widely used in visual question answering, multi-task learning, and conditional image synthesis. It also unifies gating (when $b=0$ and $a$ is sigmoid-activated) and standard affine conditioning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]