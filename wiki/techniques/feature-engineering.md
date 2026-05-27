---
id: "pkis:technique:feature-engineering"
aliases: []
title: "Feature Engineering"
knowledge_type: technique
also_type: []
domain: [statistical-learning]
tags: [features, representation, data-preprocessing, domain-knowledge, information-gain]
related_concepts: ["[[inductive-bias]]", "[[curse-of-dimensionality]]", "[[empirical-risk-minimization]]", "[[principal-component-analysis]]", "[[regularization]]"]
sources: ["[[domingos-useful-things]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

## Reading Path
- [[domingos-useful-things]] (unread) — §8: the most important factor in ML project success; domain-specific creativity; XOR problem

The practice of constructing informative input representations from raw data before applying a learning algorithm. Domingos: "easily the most important factor" in whether ML projects succeed. Key challenges: (1) features irrelevant in isolation may be jointly relevant (XOR problem — automatic feature selection by information gain will discard all XOR components); (2) domain-specific, resisting automation; (3) the iterative nature of ML pipelines means feature engineering cycles with model evaluation. The "holy grail" — automating feature engineering through representation learning and deep architectures — is the central motivation for learned representations in neural networks.
