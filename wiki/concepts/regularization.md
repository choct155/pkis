---
aliases: []
also_type: []
coverage: 3
date_created: 2026-05-20
date_updated: '2026-06-08'
domain:
- statistical-learning
- optimization
id: pkis:concept:regularization
knowledge_type: concept
maturity: settled
related_concepts:
- '[[bias-variance-tradeoff]]'
sources:
- '[[hastie-esl]]'
- '[[nielsen-nndl]]'
- '[[kroese-statistical-modeling]]'
tags:
- linear-algebra
- model-selection
title: Regularization
understanding: 0
---

## Disambiguation

The term "regularization" has domain-specific meanings:

**Statistical learning / optimization:** Adding a penalty term to the objective function that discourages complexity, trading increased bias for reduced variance. Manifests as L1 (lasso), L2 (ridge), or elastic net penalties.

**Inverse problems (Tikhonov):** Stabilizing ill-posed problems by imposing smoothness or norm constraints on the solution.

**Deep learning:** Umbrella term for any technique that reduces overfitting — includes weight decay, dropout, early stopping, data augmentation.

These uses share a common core (constraining the solution space to improve generalization) but differ in mechanism and theoretical grounding.

## Reading Path
- [[nielsen-nndl-ch03]] (unread) — deep-learning treatment: L1/L2 weight decay, dropout, early stopping, and data augmentation with empirical MNIST comparisons
- [[hastie-esl-ch05]] (unread) — statistical learning perspective on regularization via basis expansions
- [[kroese-statistical-modeling-ch09]] (unread) — dedicated regularization chapter: James-Stein, ridge, lasso, and false discovery rate; shrinkage as a unified perspective

## Probabilistic Reading: Regularizer as Log-Prior
Under the learning-as-inference view, a regularizer is not a heuristic complexity penalty but *minus a log prior* over parameters. MacKay writes the prior $P(w\mid\alpha)=\tfrac{1}{Z_W(\alpha)}\exp(-\alpha E_W)$, so minimizing $G(w)+\alpha E_W(w)$ is MAP inference of $w$. The quadratic (ridge / weight-decay) penalty $E_W=\tfrac12\sum_i w_i^2$ corresponds to a zero-mean Gaussian prior with variance $1/\alpha$; an $L_1$ (lasso) penalty corresponds to a Laplacian prior. The regularization strength is therefore an *inverse prior variance*, which makes it a quantity the data can speak to: the evidence framework infers $\alpha$ by maximizing the marginal likelihood, in place of pure cross-validation.