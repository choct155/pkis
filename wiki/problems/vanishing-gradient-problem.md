---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- deep-learning
- optimization
id: pkis:problem:vanishing-gradient-problem
knowledge_type: problem
maturity: settled
related_concepts:
- '[[backpropagation]]'
- '[[activation-functions]]'
- '[[neural-networks]]'
- '[[weight-initialization]]'
sources:
- '[[nielsen-nndl]]'
- nielsen-nndl-ch05
tags:
- training-dynamics
- backpropagation
- sigmoid
- deep-networks
- gradient-flow
title: Vanishing Gradient Problem
understanding: 0
---

The phenomenon in deep networks where gradients propagated to early layers become exponentially small relative to those in later layers: because backpropagation through sigmoid activations multiplies by σ'(z) ≤ 1/4 at each layer, gradients shrink with depth, causing early layers to learn orders of magnitude more slowly than later layers and making effective end-to-end training of deep networks difficult.

## Reading Path
- [[nielsen-nndl-ch05]] (unread) — primary diagnosis; derives quantitative explanation showing gradient magnitude products shrink with depth when |w| ≈ 1