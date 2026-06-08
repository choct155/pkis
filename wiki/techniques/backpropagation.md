---
aliases: []
also_type: []
applies:
- multilayer-perceptron
coverage: 4
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- deep-learning
- statistical-learning
id: pkis:technique:backpropagation
knowledge_type: technique
maturity: settled
related_concepts:
- '[[neural-networks]]'
- '[[automatic-differentiation]]'
- '[[vector-calculus]]'
sources:
- '[[hastie-esl]]'
- '[[deisenroth-mml]]'
- '[[nielsen-nndl]]'
- '[[liu-kan-2024]]'
- '[[marcus-dl-critical-appraisal-2018]]'
tags:
- optimization
- linear-algebra
title: Backpropagation
understanding: 0
uses:
- gradient-descent
---

Efficient computation of gradients in layered computational graphs via the chain rule applied backward from the loss, enabling gradient-based training of neural networks.

## Reading Path
- [[nielsen-nndl-ch02]] (unread) — primary treatment; derives the four fundamental BP equations from scratch with full mathematical derivation and code
- [[deisenroth-mml-ch05]] (unread) — vector calculus and Jacobian prerequisites
- [[hastie-esl-ch11]] (unread) — statistical learning perspective
- [[liu-kan-2024]] (unread) — KANs are trained via backpropagation since all operations are differentiable; LBFGS and Adam variants used
- [[marcus-dl-critical-appraisal-2018]] (unread) — §4: Hinton's public doubts about backpropagation as a biologically plausible or theoretically satisfying learning algorithm; Marcus cites these concerns as part of a broader critique of the DL paradigm's theoretical foundations

## Connections
- [[multilayer-perceptron]] — applies: Backprop is the efficient chain-rule procedure for computing gradients of an MLP's parameters.
- [[gradient-descent]] — uses: Backprop supplies the gradient that gradient descent uses to minimize the training objective M(w).