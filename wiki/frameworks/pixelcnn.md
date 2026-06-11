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
- generative-models
id: pkis:framework:pixelcnn
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch22
tags:
- PixelCNN
- image-generation
- autoregressive
- masked-convolution
- raster-scan
title: PixelCNN (2-D Autoregressive Image Model)
understanding: 0
---

## Definition
$$p(x \mid \theta) = \prod_{r=1}^{R}\prod_{c=1}^{C} p\!\left(x_{r,c} \mid f_\theta(x_{1:r-1,1:C},\, x_{r,1:c-1})\right)$$

PixelCNN factorises an image distribution in raster-scan order using 2-D masked (causal) convolutions, so each pixel is conditioned on all pixels above and to its left. Naive sampling is $O(N)$ sequential steps for $N = RC$ pixels.

### Why it matters
PixelCNN demonstrated that exact-likelihood autoregressive models can generate competitive natural images. Extensions such as PixelCNN++ (mixture-of-logistics conditionals), PixelRNN (recurrent context), and Subscale Pixel Network (bit-order sampling) progressively improved quality and efficiency.

### Key variants
| Model | Innovation |
|---|---|
| PixelCNN | Masked 2-D conv, raster order |
| PixelCNN++ | Mixture of logistics for $p(x_i)$ |
| PixelRNN | RNN + masked conv for long-range deps |
| Subscale PN | High-bits-first sampling |

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]