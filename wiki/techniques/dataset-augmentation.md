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
- machine-learning
- deep-learning
- regularization
- computer-vision
id: pkis:technique:dataset-augmentation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch07
tags:
- data-augmentation
- invariance
- regularization
- image-recognition
- noise-injection
title: Dataset Augmentation
understanding: 0
---

## Definition
A regularization strategy that expands the effective training set by applying label-preserving transformations $\tau$ to existing examples $(\mathbf{x}, y)$ to produce synthetic examples $(\tau(\mathbf{x}), y)$.

Augmentation injects prior knowledge about invariances (translation, rotation, scale, color jitter, noise, …) directly into the training distribution.

### Why it matters
Dataset augmentation is among the most effective regularizers for image recognition and speech tasks because it directly encodes domain invariances without changing the model architecture. Input noise injection (including Dropout viewed at the raw-input level) is a special case. Crucially, benchmark comparisons must control for augmentation: improvements attributed to a new algorithm may be due to stronger augmentation rather than the algorithm itself.

### Relationship to tangent propagation
Dataset augmentation is the **non-infinitesimal** version of tangent propagation — it applies finite transformations, while tangent propagation only regularizes against infinitesimal perturbations along the manifold tangent directions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]