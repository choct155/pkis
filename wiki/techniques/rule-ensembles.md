---
title: "Rule Ensembles"
knowledge_type: technique
also_type: []
domain: [statistical-learning]
tags: [ensemble-methods, decision-trees, lasso, interpretability, rule-learning, rulefit]
related_concepts: ["[[ensemble-learning]]", "[[decision-trees]]", "[[gradient-boosting]]", "[[lasso]]", "[[regularization]]", "[[partial-dependence]]"]
sources: ["[[friedman-rulefit-2005]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

A predictive learning technique (RuleFit) that generates a large pool of conjunctive binary rules by extracting every node of every tree in a tree ensemble, then selects a sparse weighted combination of rules via lasso regression, producing an interpretable model with accuracy competitive with the best tree ensemble methods.

Inputs: training data (x_i, y_i), a tree-growing algorithm, a pool of rules r_k(x) ∈ {0,1} and optional linear terms l_j(x). Output: a sparse linear model F(x) = Σ a_k r_k(x) + Σ b_j l_j(x) with typically 10-20% of candidate rules having non-zero coefficients. The lasso penalty in the fitting problem (eq. 10) simultaneously performs shrinkage and selection; support normalization gives rules equal a priori influence. Supports regression (squared-error or Huber loss) and binary classification (squared ramp loss).

## Reading Path
- [[friedman-rulefit-2005]] (unread) — primary treatment; ISLE ensemble generation, lasso-based rule fitting, variable importance measures, H-statistics for interaction detection, illustrated on Boston housing and adult census data
