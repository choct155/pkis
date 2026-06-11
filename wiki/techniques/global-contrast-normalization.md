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
- computer-vision
- deep-learning
- preprocessing
id: pkis:technique:global-contrast-normalization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch12
tags:
- normalisation
- preprocessing
- image
- contrast
- computer-vision
title: Global Contrast Normalization (GCN)
understanding: 0
---

## Definition
Given an image tensor $\mathbf{X} \in \mathbb{R}^{r \times c \times 3}$ with mean $\bar{X}$, GCN produces a normalised image $\mathbf{X}'$ via
$$X'_{i,j,k} = s\,\frac{X_{i,j,k} - \bar{X}}{\max\!\left\{\epsilon,\,\sqrt{\lambda + \frac{1}{3rc}\sum_{i,j,k}(X_{i,j,k}-\bar{X})^2}\right\}},$$
where $s$ is a target scale, $\lambda \geq 0$ is a regularisation constant that prevents amplification of near-zero-contrast images, and $\epsilon > 0$ avoids division by zero. Geometrically, GCN maps each image to a point on a hyperspherical shell of radius $s$, removing the distance-from-origin component and retaining only directional information.

### Why it matters
Reduces one major nuisance factor (global illumination / contrast variation) before learning, allowing the model to focus capacity on shape and texture. The spherical-shell geometry is beneficial because many network architectures are more sensitive to input direction than magnitude.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]