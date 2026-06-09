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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- computer-vision
- deep-learning
id: pkis:technique:edge-detection
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- image-segmentation
related_concepts: []
sources:
- russell-norvig-aima-ch25
tags:
- computer-vision
- low-level-vision
- gradient
- gaussian-filter
- canny
title: Edge Detection
understanding: 0
uses:
- convolution-of-distributions
---

## Definition
An early, low-level vision operation that abstracts an image into curves of significant brightness change. Naively, edges are points where the gradient magnitude ||grad I|| is large, but raw differentiation amplifies noise, producing spurious peaks. The standard remedy is to smooth first with a Gaussian filter G_sigma (a weighted average of nearby pixels) via convolution I * G_sigma, then differentiate. Because the derivative of a convolution equals convolution with the derivative ((f*g)' = f*g'), smoothing and differentiation combine into a single convolution with the derivative-of-Gaussian G'_sigma. In 2D the gradient grad I = (dI/dx, dI/dy) gives both an edge strength ||grad I|| and an illumination-invariant edge orientation theta(x,y) = grad I / ||grad I||. Edge points are local maxima of gradient magnitude along the gradient direction that exceed a threshold (non-maximum suppression); they are then linked into curves by joining neighboring edge pixels with consistent orientation. Edge detectors cannot disentangle the cause of an intensity discontinuity (depth, normal, reflectance, or shadow), leaving that to later processing. The classic instance is the Canny (1986) detector.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[image-segmentation]] — prerequisite-of: Boundary detection refines and extends simple edge detection; edges are a low-level input to segmentation.
- [[convolution-of-distributions]] — uses: Smoothing and differentiation are implemented as image convolution with a (derivative-of-)Gaussian kernel.
[To be populated during integration]