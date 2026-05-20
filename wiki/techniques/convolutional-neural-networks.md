---
title: "Convolutional Neural Networks"
knowledge_type: technique
also_type: [framework]
domain: [deep-learning]
tags: [neural-networks, image-recognition, translation-invariance, shared-weights]
related_concepts: ["[[neural-networks]]", "[[backpropagation]]", "[[activation-functions]]"]
sources: ["[[nielsen-nndl]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Neural network architecture exploiting spatial locality through local receptive fields (each neuron connects to only a small patch of the previous layer), shared weights (the same filter is applied across all positions), and pooling layers (spatial subsampling), dramatically reducing parameters and building in translation invariance. Classification note: assigned as technique but also functions as a framework — CNNs define an architecture space (depth, filter sizes, pooling strategies) and training methodology.

## Reading Path
- [[nielsen-nndl-ch06]] (unread) — primary treatment; introduces local receptive fields, shared weights, pooling, and achieves ~99% MNIST accuracy
