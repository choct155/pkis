---
title: "A Few Useful Things to Know About Machine Learning"
knowledge_type: source
source_type: paper
authors: ["Pedro Domingos"]
year: 2012
domain: [statistical-learning, optimization]
tags: [machine-learning, overfitting, generalization, feature-engineering, ensemble-methods, bias-variance, dimensionality, inductive-bias]
drive_id: "1bCkseO06512PFQyuBevRIAPy8BU3APCc"
status: unread
date_added: 2026-05-20
date_updated: 2026-05-20
coverage: 1
---

Survey of twelve pieces of "folk wisdom" that ML practitioners accumulate but textbooks rarely teach. Organized around classification as a running example, but the lessons apply across ML. Central organizing claim: learning = representation + evaluation + optimization, and the choice between these three components governs everything downstream.

## Key Knowledge Objects

- [[inductive-bias]] — §4: no learner can generalize without assumptions beyond the data; no-free-lunch theorem; the "knowledge lever" metaphor
- [[feature-engineering]] — §8: most important factor in ML project success; domain-specific, hard to automate
- [[bias-variance-tradeoff]] — §5: vivid dart-throwing analogy; strong false assumptions (e.g., naïve Bayes linearity assumption) can outperform weak true ones given limited data
- [[curse-of-dimensionality]] — §6: "blessing of non-uniformity" counterpoint — data concentrates on lower-dimensional manifolds in practice
- [[ensemble-learning]] — §10: bagging, boosting, stacking distinguished; BMA vs. ensembles clarified; ensembles change the hypothesis space, BMA weights within it
- [[empirical-risk-minimization]] — §2: learning = representation + evaluation + optimization is the ERM decomposition spelled out

## Twelve Lessons

| § | Lesson |
|---|--------|
| 2 | Learning = Representation + Evaluation + Optimization |
| 3 | It's Generalization That Counts (test ≠ train; use held-out data) |
| 4 | Data Alone Is Not Enough (inductive bias; no free lunch) |
| 5 | Overfitting Has Many Faces (bias-variance, noise, multiple testing) |
| 6 | Intuition Fails in High Dimensions (curse + blessing of non-uniformity) |
| 7 | Theoretical Guarantees Are Not What They Seem (PAC bounds are loose in practice) |
| 8 | Feature Engineering Is the Key |
| 9 | More Data Beats a Cleverer Algorithm (but scalability is the real bottleneck) |
| 10 | Learn Many Models, Not Just One (ensembles: bagging, boosting, stacking) |
| 11 | Simplicity Does Not Imply Accuracy (Occam's razor critique; SVMs, boosting as counterexamples) |
| 12 | Representable Does Not Imply Learnable (local optima, deep vs. shallow representations) |
| 13 | Correlation Does Not Imply Causation (connects to [[do-calculus]] and [[confounding]]) |

## Key Extractions

1. **Learning decomposition**: every learner combines a representation (hypothesis space), an evaluation function (loss/score), and an optimization method. Textbooks over-index on representation; the others matter equally.
2. **Inductive bias is unavoidable**: Wolpert's no-free-lunch theorems prove no learner beats random guessing over all functions. The assumptions that work — smoothness, similar examples having similar classes, limited dependences — are not universal truths but successful bets on structure in the real world.
3. **Strong false assumptions can beat weak true ones**: naïve Bayes's independence assumption is false almost everywhere, yet it outperforms a correct rule learner up to ~1000 examples because it needs less data to avoid overfitting. The dart-throwing bias-variance decomposition explains why.
4. **Ensembles vs. BMA**: model ensembles (bagging/boosting/stacking) change the hypothesis space; Bayesian model averaging (BMA) reweights within the original space. BMA weights are extremely skewed — effectively equivalent to selecting the single highest-weight classifier — so BMA rarely beats good ensembles in practice.
5. **Correlation ≠ causation — and it matters for action**: ML learns correlations; users often act on them as causal. Short of an experiment, causal claims require explicit causal structure (Pearl's framework); correlation is at best a guide to further investigation.
