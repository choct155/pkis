---
title: "Weight Initialization"
knowledge_type: technique
also_type: [principle]
domain: [deep-learning, optimization]
tags: [neural-networks, training-dynamics, gaussian, variance-control]
related_concepts: ["[[neural-networks]]", "[[vanishing-gradient-problem]]", "[[activation-functions]]"]
sources: ["[[nielsen-nndl]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

The strategy of initializing neural network weights with zero-mean Gaussians scaled by 1/√n_in (where n_in is the number of inputs to the neuron), ensuring that the weighted sum of inputs has variance ≈ 1 regardless of layer width, preventing neurons from saturating at initialization and enabling effective gradient flow. Classification note: assigned as technique but may also function as a principle — proper initialization is a guiding constraint that shapes the entire training trajectory.

## Reading Path
- [[nielsen-nndl-ch03]] (unread) — primary treatment; demonstrates that naive σ=1 initialization saturates neurons and shows improved 1/√n_in initialization
