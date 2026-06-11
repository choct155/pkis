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
- deep-learning
- computer-vision
id: pkis:framework:object-detection-anchor-boxes
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch14
tags:
- object-detection
- YOLO
- SSD
- bounding-box-regression
- multi-task-learning
title: Object Detection with Anchor Boxes
understanding: 0
---

## Definition
A framework for predicting a variable number of objects in an image by discretizing the output space into a fixed grid of **anchor boxes** at multiple scales and aspect ratios. For each anchor $(i,j)$ the network predicts:
- $p_{ij}\in[0,1]$: objectness score
- $y_{ij}\in\{1,\ldots,C\}$: class label
- $\delta_{ij}\in\mathbb{R}^4$: bounding box offset from anchor centroid

Formally:
$$f_\theta:\mathbb{R}^{H\times W\times K}\to[0,1]^{A\times A}\times\{1,\ldots,C\}^{A\times A}\times(\mathbb{R}^4)^{A\times A}$$
Examples include SSD (Single Shot Detector) and YOLO, which perform detection in a single forward pass.

### Why it matters
Anchor-box detectors convert the open-world problem of detecting an unknown number of objects into a closed-world regression/classification problem amenable to standard supervised learning with a CNN backbone, enabling real-time detection.

### Limitation
Requires careful anchor design (scale, aspect ratio); largely superseded by anchor-free transformer-based detectors (DETR) in recent work.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]