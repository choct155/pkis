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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- computer-vision
- deep-learning
id: pkis:concept:feature-detection-vision
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- optical-flow
- stereo-and-depth
related_concepts: []
sources:
- russell-norvig-aima-ch25
tags:
- computer-vision
- texture
- feature
- descriptor
- sift
- hog
- histogram-of-orientations
title: Visual Feature and Texture Representation
understanding: 0
uses:
- edge-detection
---

## Definition
A feature is a number obtained by simple computation on an image; useful representations summarize an image patch in a way that is invariant to nuisance variation (illumination) yet sensitive to meaningful structure (orientation). Texture is a (statistically) repetitive pattern of elements (texels) defined over a patch rather than a single pixel. A basic, illumination-robust texture descriptor is a histogram of gradient orientations over the patch: gradient orientation is invariant to brightness scaling, and the histogram captures pattern (e.g., vertical stripes give two orientation peaks; leopard spots give uniform orientations). Local point descriptors build feature vectors from parts of objects using three key strategies: use orientations for illumination invariance, describe nearby structure in detail but distant structure coarsely, and use spatial histograms to absorb small localization errors. Lowe's SIFT (2004) and the HOG descriptor (Dalal & Triggs, 2005) are the canonical hand-crafted instances. These features enable object identification and, crucially, patch matching across images (correspondence). Modern systems learn such features from data with CNNs rather than hand-crafting them.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[stereo-and-depth]] — prerequisite-of: Descriptor-based patch matching solves the stereo correspondence problem.
- [[optical-flow]] — prerequisite-of: Patch/texture matching is the correspondence mechanism optical flow relies on.
- [[edge-detection]] — uses: Gradient/orientation computations underlying texture and point descriptors build on edge/gradient operations.
[To be populated during integration]