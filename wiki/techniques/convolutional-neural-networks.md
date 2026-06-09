---
aliases: []
also_type:
- framework
applies:
- image-formation-model
coverage: 2
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- deep-learning
generalizes:
- feature-detection-vision
id: pkis:technique:convolutional-neural-networks
knowledge_type: technique
maturity: settled
related_concepts:
- '[[neural-networks]]'
- '[[backpropagation]]'
- '[[activation-functions]]'
sources:
- '[[nielsen-nndl]]'
- '[[marcus-dl-critical-appraisal-2018]]'
tags:
- neural-networks
- image-recognition
- translation-invariance
- shared-weights
title: Convolutional Neural Networks
understanding: 0
uses:
- convolution-of-distributions
---

Neural network architecture exploiting spatial locality through local receptive fields (each neuron connects to only a small patch of the previous layer), shared weights (the same filter is applied across all positions), and pooling layers (spatial subsampling), dramatically reducing parameters and building in translation invariance. Classification note: assigned as technique but also functions as a framework — CNNs define an architecture space (depth, filter sizes, pooling strategies) and training methodology.

## Reading Path
- [[nielsen-nndl-ch06]] (unread) — primary treatment; introduces local receptive fields, shared weights, pooling, and achieves ~99% MNIST accuracy
- [[marcus-dl-critical-appraisal-2018]] (unread) — §5–6: uses CNNs as the central case study for brittleness (adversarial examples, texture bias, distribution shift); argues that CNN translation invariance is a narrow inductive bias that fails on geometric transformations, viewpoint changes, and novel compositions; CNNs' successes in image recognition are presented as local maxima rather than general solutions

## Connections
- [[feature-detection-vision]] — generalizes: Learned CNN features supersede hand-crafted texture/point descriptors like SIFT and HOG.
- [[image-formation-model]] — applies: CNN classifiers learn to invert image-formation effects (lighting, foreshortening, aspect, occlusion, deformation) from data.
- [[convolution-of-distributions]] — uses: CNN layers apply discrete convolution of an image with learned kernels.