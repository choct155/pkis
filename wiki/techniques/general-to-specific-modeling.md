---
id: "pkis:technique:general-to-specific-modeling"
aliases: []
title: "General-to-Specific Modeling"
knowledge_type: technique
also_type: []
domain: [statistical-learning]
tags: [model-selection, variable-selection, econometrics, autometrics, hypothesis-testing, automatic-modeling]
related_concepts: ["[[model-selection-problem]]", "[[information-criteria]]", "[[regularization]]", "[[bias-variance-tradeoff]]"]
sources: ["[[castle-model-selection-algorithms]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

A regression model selection strategy that begins with a general model containing all candidate variables and progressively eliminates statistically insignificant variables through multi-path tree search, maintaining pre-specified diagnostic conditions throughout reduction. The canonical implementation is Autometrics (PcGive), which applies post-selection bias correction to retained coefficient estimates.

Inputs: a dataset with N observations, L candidate variables, and a significance level α. Output: a parsimonious model with K ≤ L variables retained. The gauge (null rejection frequency) approximates the nominal α level, making the penalty function directly interpretable. Under low signal-to-noise conditions (ψ ≤ 2) with many irrelevant variables (K/L ≤ 0.5), Autometrics at 1% significance dominates alternative selection strategies in coefficient UMSE.

## Reading Path
- [[castle-model-selection-algorithms]] (unread) — systematic Monte Carlo comparison; Autometrics at 1% and variable significance levels outperforms 18 other MSAs in over 90% of practically relevant experiments; bias correction mechanism discussed
