---
aliases: []
also_type: []
applies:
- multilayer-perceptron
coverage: 4
date_created: 2026-05-20
date_updated: '2026-06-08'
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

## What Backpropagation Computes: Gradient of the Regularized Objective
An MLP is trained on data $D=\{\mathbf{x}^{(n)}, \mathbf{t}^{(n)}\}$ by minimizing an error function, e.g. the sum-of-squares

$$E_D(\mathbf{w}) = \tfrac{1}{2}\sum_n\sum_i\big(t_i^{(n)} - y_i(\mathbf{x}^{(n)};\mathbf{w})\big)^2.$$

Minimization proceeds by repeated evaluation of $\nabla E_D$, and **this gradient is exactly what backpropagation computes efficiently** (Rumelhart et al., 1986) — a single forward pass followed by a backward pass that applies the chain rule layer by layer, reusing intermediate quantities so the whole gradient costs roughly the same as one forward evaluation.

In practice the objective is regularized (weight decay):

$$M(\mathbf{w}) = \beta E_D + \alpha E_W,\qquad E_W = \tfrac{1}{2}\sum_i w_i^2,$$

which penalises large weights and curbs overfitting. Backpropagation supplies $\nabla M$ just as readily — the regularizer's gradient $\alpha\mathbf{w}$ is trivial — and gradient descent on $M(\mathbf{w})$ has been used to solve non-trivial tasks (symmetry detection, text-to-speech in NETtalk, telescope focussing). For classification heads the squared error $\beta E_D$ is replaced by the cross-entropy negative log likelihood, but the backprop mechanism for obtaining the gradient is unchanged.