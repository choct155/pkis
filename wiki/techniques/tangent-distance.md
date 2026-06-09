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
- statistical-learning
- computer-vision
id: pkis:technique:tangent-distance
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch13
tags:
- invariant-metric
- nearest-neighbors
- digit-recognition
- classification
title: Tangent Distance
understanding: 0
---

## Definition
An invariant distance metric for nearest-neighbor classification that makes objects close when one is a known transformation of the other (Simard et al., 1993). Motivation: a handwritten '3' rotated slightly is still a '3', yet its 256 grayscale pixel values can be far from the original in Euclidean R^256. The set of rotated versions of an image traces a one-dimensional curve in pixel space, the invariance manifold; an invariant metric uses the shortest Euclidean distance between two images' manifolds rather than between the images themselves. Computing manifold-to-manifold distance exactly is intractable and admits undesirable large transformations (a '6' becomes a '9' under 180-degree rotation). Tangent distance solves both problems by approximating each invariance manifold by its tangent (hyper)plane at the image, computed from small transformations (or spatial smoothing). Distance is then the shortest Euclidean distance between the two tangent lines/hyperplanes, restricting to small transformations. With seven transformation classes (rotation, two translations, two scalings, shear, thickness) the manifolds and tangents are 7-dimensional. Tangent-distance 1-NN achieved near-human error on USPS digits. Contrasts with 'hints' (Abu-Mostafa), which adds explicitly transformed copies to the training set — feasible only when the invariance space is small. The K-means analog of the invariant metric (Hastie & Simard, 1998) reduces the computational load.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]