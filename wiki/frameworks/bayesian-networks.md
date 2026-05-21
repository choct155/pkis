---
title: "Bayesian Networks"
knowledge_type: framework
also_type: []
domain: [bayesian-stats, knowledge-representation, causal-analysis]
tags: [probability-theory, graph-theory, expert-systems]
related_concepts: ["[[directed-graphical-models]]", "[[belief-propagation]]", "[[conditional-independence]]", "[[d-separation]]"]
sources: ["[[pearl-reverend-bayes-1982]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Directed acyclic graphs where nodes represent random variables and directed edges encode conditional probability tables P(B|A); the joint distribution factorizes as the product of local conditional distributions; inference proceeds via belief propagation (exact on trees, approximate via loopy BP on general DAGs) — Pearl's 1982 paper presents the proto-form of this framework for hierarchical tree-structured expert systems. Classification note: bayesian-networks specializes directed-graphical-models; the distinction is that BNs emphasize the inference algorithm (BP) while the DGM framework is more general.

## Reading Path
- [[pearl-reverend-bayes-1982]] (unread) — earliest formulation: hierarchical inference net, local message passing, proof of single-pass correctness
