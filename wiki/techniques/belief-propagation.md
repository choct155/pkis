---
id: "pkis:technique:belief-propagation"
aliases: []
title: "Belief Propagation"
knowledge_type: technique
also_type: []
domain: [bayesian-stats, knowledge-representation]
tags: [probability-theory, graph-theory, expert-systems, message-passing]
related_concepts: ["[[directed-graphical-models]]", "[[conditional-independence]]", "[[bayesian-networks]]", "[[mcmc]]", "[[variational-inference]]"]
sources: ["[[pearl-reverend-bayes-1982]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Message-passing algorithm for exact Bayesian inference in tree-structured graphical models: each node maintains bottom-up evidential support λ(B_i) = P(D^d|B_i) and top-down anticipatory support π(B_i) = P(B_i|D^u), with posterior P(B_i) ∝ λ(B_i)·π(B_i); messages diffuse through the network in a single pass equal to the graph diameter, with the two-parameter decoupling preventing infinite update loops.

## Reading Path
- [[pearl-reverend-bayes-1982]] (unread) — original formulation; proves single-pass convergence, derives propagation equations, demonstrates on binary tree token game; AAAI-82
