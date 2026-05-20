---
title: "Neural Networks (Feedforward)"
knowledge_type: technique
also_type: [framework]
domain: [deep-learning, statistical-learning]
tags: [optimization, linear-algebra]
related_concepts: ["[[bias-variance-tradeoff]]", "[[regularization]]"]
sources: ["[[hastie-esl]]", "[[nielsen-nndl]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

Layered function approximators that compose affine transformations with nonlinear activation functions, trained by gradient-based optimization (backpropagation). Classification note: assigned as technique but also functions as a framework — neural networks encompass an architecture space, training methodology, regularization strategies (weight decay, early stopping, dropout), and Bayesian extensions.

## Reading Path
- [[nielsen-nndl-ch01]] (unread) — builds a working feedforward MNIST classifier from perceptrons and sigmoid neurons; the primary principle-oriented treatment
- [[nielsen-nndl-ch03]] (unread) — covers practical improvements: cross-entropy loss, regularization, dropout, weight initialization
- [[hastie-esl-ch11]] (unread) — statistical learning perspective on neural networks
