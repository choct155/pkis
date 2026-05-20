---
title: "Convolutional Neural Networks"
knowledge_type: technique
also_type: [framework]
domain: [deep-learning]
tags: [neural-networks, image-recognition, translation-invariance, shared-weights]
related_concepts: ["[[neural-networks]]", "[[backpropagation]]", "[[activation-functions]]"]
sources: ["[[nielsen-nndl]]", "[[marcus-dl-critical-appraisal-2018]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

Neural network architecture exploiting spatial locality through local receptive fields (each neuron connects to only a small patch of the previous layer), shared weights (the same filter is applied across all positions), and pooling layers (spatial subsampling), dramatically reducing parameters and building in translation invariance. Classification note: assigned as technique but also functions as a framework — CNNs define an architecture space (depth, filter sizes, pooling strategies) and training methodology.

## Reading Path
- [[nielsen-nndl-ch06]] (unread) — primary treatment; introduces local receptive fields, shared weights, pooling, and achieves ~99% MNIST accuracy
- [[marcus-dl-critical-appraisal-2018]] (unread) — §5–6: uses CNNs as the central case study for brittleness (adversarial examples, texture bias, distribution shift); argues that CNN translation invariance is a narrow inductive bias that fails on geometric transformations, viewpoint changes, and novel compositions; CNNs' successes in image recognition are presented as local maxima rather than general solutions
