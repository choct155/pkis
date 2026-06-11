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
- neuroscience
- deep-learning
id: pkis:concept:simple-cells-complex-cells-v1
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch09
tags:
- V1
- Hubel Wiesel
- simple cell
- complex cell
- quadrature pair
- pooling motivation
title: Simple Cells and Complex Cells (V1)
understanding: 0
---

## Definition
Hubel and Wiesel's classification of neurons in primary visual cortex (V1):

- **Simple cells**: respond approximately linearly to oriented luminance gratings within a small, fixed receptive field; well modelled by a Gabor filter $s(I)=\sum_{x,y}w(x,y)I(x,y)$.
- **Complex cells**: respond to the same features as simple cells but are invariant to small spatial shifts; modelled as $c(I)=\sqrt{s_0(I)^2+s_1(I)^2}$ for a **quadrature pair** $(s_0,s_1)$ differing by a $\tfrac{\pi}{2}$ phase offset.

### Why it matters
Simple cells inspired the *detector stage* (linear filter + nonlinearity) of convolutional layers; complex cells inspired *max pooling* and $L^2$ spatial pooling. The simple→complex hierarchy is the biological archetype for the selectivity→invariance pattern replicated in deep CNNs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]