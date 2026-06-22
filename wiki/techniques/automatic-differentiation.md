---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-22'
domain:
- deep-learning
- optimization
id: pkis:technique:automatic-differentiation
knowledge_type: technique
maturity: settled
related_concepts:
- '[[vector-calculus]]'
- '[[backpropagation]]'
- '[[gradient-descent]]'
sources:
- '[[deisenroth-mml]]'
- '[[liu-kan-2024]]'
- betancourt-a-2018
- margossian-efficient-2021
tags:
- calculus
- computational-methods
title: Automatic Differentiation
understanding: 0
---

Systematic application of the chain rule to arbitrary differentiable programs to compute exact derivatives; forward mode accumulates derivatives from inputs to outputs (cheap for few inputs), reverse mode from outputs to inputs (cheap for few outputs, most common in ML); backpropagation is reverse-mode AD applied to neural network loss functions.

## Reading Path
- [[deisenroth-mml]] (unread) — foundational treatment of forward and reverse AD modes
- [[liu-kan-2024]] (unread) — KAN operations are all differentiable, making the architecture trainable via standard AD frameworks