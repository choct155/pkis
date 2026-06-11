---
aliases: []
also_type: []
applies:
- image-segmentation
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
id: pkis:framework:encoder-decoder-unet
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch14
tags:
- semantic-segmentation
- dense-prediction
- skip-connection
- unet
- image-to-image
title: Encoder–Decoder Architecture (U-Net)
understanding: 0
uses:
- convolutional-neural-network
- transposed-convolution
- dilated-convolution
- residual-block
---

## Definition
A CNN architecture for **dense prediction** (pixel-to-pixel mapping) consisting of:
- An **encoder** (contracting path) that applies successive convolutions and downsampling to build a compact high-level feature representation at coarse resolution.
- A **decoder** (expanding path) that uses transposed convolution to upsample back to full resolution.
- **Skip connections** from each encoder level to the corresponding decoder level that concatenate fine-grained spatial features with high-level semantic features, compensating for information lost during downsampling.

The network's overall shape, when drawn as a graph, resembles the letter U, giving the model its name (U-Net [RFB15]).

### Why it matters
The encoder–decoder design with skip connections achieves state-of-the-art results across semantic segmentation, depth prediction, surface normal estimation, and medical image analysis, and is also the backbone of many generative image models (e.g., diffusion model U-Nets).

### Variants
Dilated convolution in the encoder replaces pooling to preserve spatial resolution while capturing global context; multiple output heads enable multi-task dense prediction.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[residual-block]] — uses: Skip connections in U-Net play the same role as in ResNet
- [[image-segmentation]] — applies: U-Net is the standard architecture for semantic segmentation
- [[dilated-convolution]] — uses: Dilated convolution in encoder for context without spatial reduction
- [[transposed-convolution]] — uses: Decoder upsamples via transposed convolution
- [[convolutional-neural-network]] — uses: Both encoder and decoder paths consist of CNN layers
[To be populated during integration]