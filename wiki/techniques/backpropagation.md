---
title: "Backpropagation"
knowledge_type: technique
also_type: []
domain: [deep-learning, statistical-learning]
tags: [optimization, linear-algebra]
related_concepts: ["[[neural-networks]]", "[[automatic-differentiation]]", "[[vector-calculus]]"]
sources: ["[[hastie-esl]]", "[[deisenroth-mml]]", "[[nielsen-nndl]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 3
understanding: 0
maturity: settled
---

Efficient computation of gradients in layered computational graphs via the chain rule applied backward from the loss, enabling gradient-based training of neural networks.

## Reading Path
- [[nielsen-nndl-ch02]] (unread) — primary treatment; derives the four fundamental BP equations from scratch with full mathematical derivation and code
- [[deisenroth-mml-ch05]] (unread) — vector calculus and Jacobian prerequisites
- [[hastie-esl-ch11]] (unread) — statistical learning perspective
