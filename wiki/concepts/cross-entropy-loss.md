---
id: "pkis:concept:cross-entropy-loss"
aliases: []
title: "Cross-Entropy Loss"
knowledge_type: concept
also_type: []
domain: [deep-learning, optimization, statistical-learning]
tags: [information-theory, loss-functions, neural-networks, classification]
related_concepts: ["[[neural-networks]]", "[[backpropagation]]", "[[activation-functions]]", "[[kl-divergence]]"]
sources: ["[[nielsen-nndl]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Loss function for classification defined as C = −(1/n) Σ[y ln(a) + (1−y) ln(1−a)], where a is the network's output and y is the target; the key property is that its gradient ∂C/∂w_j = (a − y)x_j does not contain a σ'(z) factor, eliminating the learning slowdown that occurs when output neurons are saturated under mean squared error loss.

## Reading Path
- [[nielsen-nndl-ch03]] (unread) — primary treatment; derives cross-entropy from scratch and demonstrates elimination of learning slowdown compared to quadratic cost
