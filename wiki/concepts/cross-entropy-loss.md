---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- deep-learning
- optimization
- statistical-learning
id: pkis:concept:cross-entropy-loss
knowledge_type: concept
maturity: settled
related_concepts:
- '[[neural-networks]]'
- '[[backpropagation]]'
- '[[activation-functions]]'
- '[[kl-divergence]]'
sources:
- '[[nielsen-nndl]]'
tags:
- information-theory
- loss-functions
- neural-networks
- classification
title: Cross-Entropy Loss
understanding: 0
uses:
- self-information
---

Loss function for classification defined as C = −(1/n) Σ[y ln(a) + (1−y) ln(1−a)], where a is the network's output and y is the target; the key property is that its gradient ∂C/∂w_j = (a − y)x_j does not contain a σ'(z) factor, eliminating the learning slowdown that occurs when output neurons are saturated under mean squared error loss.

## Reading Path
- [[nielsen-nndl-ch03]] (unread) — primary treatment; derives cross-entropy from scratch and demonstrates elimination of learning slowdown compared to quadratic cost

## Connections
- [[self-information]] — uses