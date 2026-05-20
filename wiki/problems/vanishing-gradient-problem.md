---
title: "Vanishing Gradient Problem"
knowledge_type: problem
also_type: []
domain: [deep-learning, optimization]
tags: [training-dynamics, backpropagation, sigmoid, deep-networks, gradient-flow]
related_concepts: ["[[backpropagation]]", "[[activation-functions]]", "[[neural-networks]]", "[[weight-initialization]]"]
sources: ["[[nielsen-nndl]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

The phenomenon in deep networks where gradients propagated to early layers become exponentially small relative to those in later layers: because backpropagation through sigmoid activations multiplies by σ'(z) ≤ 1/4 at each layer, gradients shrink with depth, causing early layers to learn orders of magnitude more slowly than later layers and making effective end-to-end training of deep networks difficult.

## Reading Path
- [[nielsen-nndl-ch05]] (unread) — primary diagnosis; derives quantitative explanation showing gradient magnitude products shrink with depth when |w| ≈ 1
