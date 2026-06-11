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
- computer-vision
- deep-learning
id: pkis:concept:gabor-function
instantiates:
- feature-detection-vision
- convolution-operation-nn
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch09
tags:
- Gabor filter
- V1
- simple cell
- natural image statistics
- feature detection
title: Gabor Function (Neuroscience / Vision)
understanding: 0
uses:
- simple-cells-complex-cells-v1
---

## Definition
A **Gabor function** describes the spatial weighting profile of a V1 simple cell:
$$w(x,y) = \alpha\,\exp\!\left(-\beta_x x'^2 - \beta_y y'^2\right)\cos(f x' + \varphi)$$
where $x' = (x-x_0)\cos\tau+(y-y_0)\sin\tau$ is a rotated, translated coordinate.

It is the product of a Gaussian envelope (localisation in space) and a cosine grating (selectivity for spatial frequency and orientation).

### Why it matters
Reverse-correlation experiments show that most V1 simple-cell weight profiles are well-described by Gabor functions. Remarkably, many unsupervised and supervised deep learning algorithms independently learn Gabor-like filters in their first layer when trained on natural images, providing empirical support for the link between CNN feature detectors and biological vision.

### Parameters
$\alpha$ — amplitude; $\beta_x,\beta_y$ — Gaussian spread; $f$ — spatial frequency; $\varphi$ — phase; $x_0,y_0$ — center; $\tau$ — orientation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[convolution-operation-nn]] — instantiates: Gabor functions describe V1 simple-cell kernels; first-layer CNN kernels learn Gabor-like shapes.
- [[feature-detection-vision]] — instantiates
- [[simple-cells-complex-cells-v1]] — uses
[To be populated during integration]