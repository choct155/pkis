---
title: "Dropout"
knowledge_type: technique
also_type: []
domain: [deep-learning, optimization]
tags: [regularization, neural-networks, ensemble, overfitting]
related_concepts: ["[[regularization]]", "[[neural-networks]]", "[[bias-variance-tradeoff]]"]
sources: ["[[nielsen-nndl]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Regularization technique for neural networks that randomly zeros out half the hidden neurons (with their connections) on each mini-batch forward pass during training; at test time all neurons are active but their outgoing weights are halved to compensate, approximating the geometric mean of an exponentially large ensemble of thinned networks.

## Reading Path
- [[nielsen-nndl-ch03]] (unread) — primary treatment; describes mechanics, motivation as implicit ensembling, and empirical results on MNIST
