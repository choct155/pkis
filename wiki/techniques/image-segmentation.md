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
id: pkis:technique:image-segmentation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch25
tags:
- computer-vision
- mid-level-vision
- normalized-cut
- graph-partitioning
- superpixels
title: Image Segmentation
understanding: 0
---

## Definition
The process of partitioning an image into groups of pixels that naturally belong together, where within-region attributes (brightness, color, texture) vary little while across-boundary attributes change sharply. Two complementary formulations exist: boundary detection finds object contours, and region extraction finds the regions themselves. Boundary detection can be posed as supervised classification: train a classifier to predict P_b(x,y,theta), the probability of a boundary at pixel (x,y) with orientation theta, from features compared across the two halves of a local disk, using human-marked ground-truth boundaries. Region-based segmentation clusters pixels; a leading formulation (Shi & Malik, 2000) treats it as graph partitioning, with pixels as nodes, edge weights W_ij encoding pixel similarity, and partitions chosen to minimize the normalized cut criterion (minimize cross-group weight, maximize within-group weight). Other formulations use Markov Random Fields (Geman & Geman, 1984) or the Mumford-Shah variational functional. Edges alone do not suffice (many edges are not object boundaries, e.g., tiger stripes). Low-level cues cannot by themselves recover correct object boundaries; a common practical strategy is over-segmentation into superpixels (hundreds of regions guaranteed not to miss true boundaries), which greatly reduces downstream computational cost.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]