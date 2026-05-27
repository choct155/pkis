---
id: "pkis:technique:partial-dependence"
aliases: []
title: "Partial Dependence"
knowledge_type: technique
also_type: []
domain: [statistical-learning]
tags: [interpretability, visualization, interaction-effects, black-box-models, model-explanation]
related_concepts: ["[[rule-ensembles]]", "[[gradient-boosting]]", "[[ensemble-learning]]", "[[decision-trees]]"]
sources: ["[[friedman-rulefit-2005]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

A technique for visualizing and quantifying the marginal dependence of a fitted model F(x) on a subset x_s of predictor variables by averaging predictions over the empirical distribution of all other variables x_{-s}: F̂_s(x_s) = (1/N) Σ_i F(x_s, x_i_{-s}).

The partial dependence function reveals main effects when applied to single variables and exposes interaction structure when applied to pairs. If two variables do not interact, F_{jk}(x_j, x_k) = F_j(x_j) + F_k(x_k); deviations from this additive decomposition quantify interactions via the H-statistic (eq. 44 in Friedman/Popescu). Applicable to any fitted model F(x) given the training data; can be used as a general model-agnostic explanation tool, not just for rule ensembles.

## Reading Path
- [[friedman-rulefit-2005]] (unread) — introduces partial dependence for RuleFit interpretation; H-statistics using partial dependence to detect two- and three-variable interactions; parametric bootstrap for null distributions
