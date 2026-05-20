---
title: "Directed Graphical Models (Bayesian Networks)"
knowledge_type: framework
also_type: []
domain: [bayesian-stats, knowledge-representation, causal-analysis]
tags: [probability-theory, graph-theory]
related_concepts: ["[[probability-theory]]", "[[undirected-graphical-models]]", "[[structural-causal-models]]", "[[d-separation]]"]
sources: ["[[deisenroth-mml]]", "[[pearl-causality]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

## Reading Path
- [[deisenroth-mml]] (unread) — probabilistic treatment; DAG factorization and Bayesian network inference
- [[pearl-causality-ch01]] (unread) — Pearl's treatment; d-separation and the bridge from probability to causal DAGs

Framework for representing joint probability distributions as directed acyclic graphs (DAGs) where edges encode conditional dependencies; the joint factors as $p(x_{1:n}) = \prod_i p(x_i | \text{pa}(x_i))$ where $\text{pa}(x_i)$ are the parents of node $i$ — the probabilistic counterpart to causal DAGs and the structural backbone of Bayesian networks and many generative models. Pearl's SCMs extend this framework to the interventional and counterfactual layers by adding structural equations to the probabilistic skeleton.
