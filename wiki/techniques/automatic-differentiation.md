---
id: "pkis:technique:automatic-differentiation"
aliases: []
title: "Automatic Differentiation"
knowledge_type: technique
also_type: []
domain: [deep-learning, optimization]
tags: [calculus, computational-methods]
related_concepts: ["[[vector-calculus]]", "[[backpropagation]]", "[[gradient-descent]]"]
sources: ["[[deisenroth-mml]]", "[[liu-kan-2024]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Systematic application of the chain rule to arbitrary differentiable programs to compute exact derivatives; forward mode accumulates derivatives from inputs to outputs (cheap for few inputs), reverse mode from outputs to inputs (cheap for few outputs, most common in ML); backpropagation is reverse-mode AD applied to neural network loss functions.

## Reading Path
- [[deisenroth-mml]] (unread) — foundational treatment of forward and reverse AD modes
- [[liu-kan-2024]] (unread) — KAN operations are all differentiable, making the architecture trainable via standard AD frameworks
