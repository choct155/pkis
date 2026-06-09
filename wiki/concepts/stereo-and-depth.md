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
id: pkis:concept:stereo-and-depth
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch25
tags:
- computer-vision
- stereopsis
- disparity
- structure-from-motion
- depth-map
- slam
title: Stereo and Depth Reconstruction
understanding: 0
---

## Definition
Recovery of 3D scene structure from one or more images. With two views from different viewpoints, the horizontal shift of a scene point between the left and right image is its disparity, which is inversely related to depth. For parallel optical axes separated by baseline b, horizontal disparity H = b/Z and vertical disparity is zero, so depth Z is recovered from measured H. For converging (fixated) eyes, disparity = b*dZ/Z^2; with a human baseline of ~6 cm this yields sub-millimeter depth discrimination at arm's length. The central difficulty is the correspondence problem: matching each point in one view to its projection in the other, solved (as in optical flow) by SSD block matching or richer texture descriptors plus geometric and smoothness constraints. Given correspondences, multi-view geometry reconstructs both scene points and camera parameters up to a scale factor; with many views (structure from motion, multiview stereo) one can accurately reconstruct entire cities, supporting SLAM, model building, and construction monitoring. Depth can even be predicted from a single image by learning image-to-depth maps, and single-view shape cues include occlusion, texture gradients, shading, known-object pose, and spatial relations (e.g., the ground-plane/horizon constraint on object scale).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]