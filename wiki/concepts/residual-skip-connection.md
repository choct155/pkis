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
- neural-network-architecture
id: pkis:concept:residual-skip-connection
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch16
tags:
- ResNet
- skip-connection
- gradient-flow
- architecture
title: Residual (Skip) Connection
understanding: 0
---

## Definition
$$y = \varphi(\text{conv}(x;\mathbf{W})) + x$$

A residual or skip connection routes the input of a block directly to its output, so the learned transformation only needs to model the *residual* (difference) between desired output and input, rather than the full mapping.

### Why it matters
Deep networks suffer from vanishing/exploding signals and gradients. Skip connections provide an identity shortcut that keeps gradients flowing and allows the block to initialize near the identity function, dramatically easing optimization of very deep networks (e.g., ResNets with hundreds of layers). The residual learning principle has become one of the most widely adopted architectural motifs in modern deep learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]