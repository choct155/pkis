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
- deep-learning
- interpretability
id: pkis:technique:activation-maximization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch14
tags:
- feature-visualization
- CNN-interpretability
- deep-dream
- image-prior
title: Activation Maximization
understanding: 0
---

## Definition
A technique for visualizing what a trained neural network has learned by finding the input $x^*$ that maximizes the activation of a target neuron $j$ (or output class $c$), typically subject to an image prior $p(x)$:
$$x^* = \arg\max_x \left[\log p(y=c\mid x) + \log p(x)\right]$$
Optimization proceeds by gradient ascent in **input pixel space** using backpropagation to compute $\partial\log p(y=c|x)/\partial x$, combined with a regularizer such as a TV norm or Gaussian prior. Starting from random noise or a real image yields qualitatively different results.

### Why it matters
Activation maximization is the primary tool for interpreting CNN feature representations: early layers yield edge/Gabor-like features; intermediate layers yield textures; deep layers yield object parts and whole objects — empirically matching the hierarchy of the visual cortex.

### Related technique
Deep Dream uses activation maximization on intermediate layers of a trained network applied to a real input image to amplify and visualize learned features artistically.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]