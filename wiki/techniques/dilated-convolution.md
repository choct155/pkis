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
- computer-vision
id: pkis:technique:dilated-convolution
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch14
tags:
- atrous-convolution
- receptive-field
- segmentation
- dense-prediction
title: Dilated (Atrous) Convolution
understanding: 0
---

## Definition
A convolution variant that samples the input at regular intervals determined by a **dilation rate** $r$, effectively inserting $r-1$ zeros between filter taps:
$$z_{i,j,d} = b_d + \sum_{u=0}^{H-1}\sum_{v=0}^{W-1}\sum_{c=0}^{C-1} x_{i+ru,\,j+rv,\,c}\;w_{u,v,c,d}$$
With $r=1$ this reduces to standard convolution. A rate-$r$ dilated convolution with a $k\times k$ filter has an effective receptive field of $(r(k-1)+1)\times(r(k-1)+1)$ without any increase in the number of parameters or computation.

### Why it matters
Dilated convolution exponentially enlarges the receptive field as layers are stacked with increasing rates (e.g., $r=1,2,4,8$), which is critical for semantic segmentation and other dense-prediction tasks where global context must be captured without spatial downsampling.

### Applications
Used in encoder paths of U-Net–style segmentation models; also central to WaveNet for audio generation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]