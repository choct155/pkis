---
title: "Directed Graphical Models (Bayesian Networks)"
knowledge_type: framework
also_type: []
domain: [bayesian-stats, knowledge-representation, causal-analysis]
tags: [probability-theory, graph-theory]
related_concepts: ["[[probability-theory]]", "[[undirected-graphical-models]]"]
sources: ["[[deisenroth-mml]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Framework for representing joint probability distributions as directed acyclic graphs (DAGs) where edges encode conditional dependencies; the joint factors as $p(x_{1:n}) = \prod_i p(x_i | \text{pa}(x_i))$ where $\text{pa}(x_i)$ are the parents of node $i$ — the probabilistic counterpart to causal DAGs and the structural backbone of Bayesian networks and many generative models.
