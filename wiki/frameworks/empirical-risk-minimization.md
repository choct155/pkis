---
aliases:
- ERM
also_type: []
contrasts-with:
- bias-variance-tradeoff
coverage: 2
date_created: 2026-05-20
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:framework:empirical-risk-minimization
knowledge_type: framework
maturity: settled
related_concepts:
- '[[model-selection-problem]]'
- '[[bias-variance-tradeoff]]'
- '[[regularization]]'
- '[[continuous-optimization]]'
- '[[inductive-bias]]'
sources:
- '[[deisenroth-mml]]'
- '[[domingos-useful-things]]'
- '[[liu-kan-2024]]'
tags:
- probability-theory
- optimization
title: Empirical Risk Minimization (ERM)
understanding: 0
---

## Reading Path
- [[deisenroth-mml]] (unread) — formal treatment: risk, empirical risk, regularization as Lagrangian
- [[domingos-useful-things]] (unread) — §2: learning = representation + evaluation + optimization; the ERM decomposition made intuitive with Table 1
- [[liu-kan-2024]] (unread) — KAN training minimizes prediction loss plus L1 + entropy sparsification regularization; grid extension provides a non-standard approach to the bias-variance tradeoff

The formal framework underlying supervised learning: choose a hypothesis class and loss function, then minimize average loss on training data as a surrogate for true risk (expected loss over the data-generating distribution); the choice of loss and hypothesis class determines the method — cross-entropy gives logistic regression, hinge loss gives SVMs, squared loss gives OLS.

## Connections
- [[bias-variance-tradeoff]] — contrasts-with: MML Ch.1: minimizing empirical (training) risk can yield memorization rather than generalization; the bias-variance tradeoff names exactly the failure mode that makes pure ERM insufficient for unseen data.

## Generalization is the goal, not training fit
Deisenroth et al. (MML Ch. 1) frame the central tension of learning through a hill-climbing analogy: training optimizes parameters against a utility function evaluated on the *training* data, where the peak corresponds to a maximum of some performance measure. But strong training-set performance may merely indicate that the model has memorized the data. The practitioner cares about performance on *unseen* data, so the objective is to find models that generalize well rather than ones that minimize empirical risk alone. This motivates the gap between empirical risk (computed on the sample) and true risk (the expectation over the data-generating distribution), and it is the conceptual entry point for regularization, the bias-variance tradeoff, and held-out evaluation. MML organizes all of supervised learning around three components — data (represented as vectors), a model (chosen via a probabilistic or optimization view), and learning (numerical optimization of parameters) — with generalization as the criterion that judges the whole pipeline.