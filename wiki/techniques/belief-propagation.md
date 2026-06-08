---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- bayesian-stats
- knowledge-representation
id: pkis:technique:belief-propagation
instantiates:
- sum-product-algorithm
knowledge_type: technique
maturity: settled
related_concepts:
- '[[directed-graphical-models]]'
- '[[conditional-independence]]'
- '[[bayesian-networks]]'
- '[[mcmc]]'
- '[[variational-inference]]'
sources:
- '[[pearl-reverend-bayes-1982]]'
specializes:
- message-passing
tags:
- probability-theory
- graph-theory
- expert-systems
- message-passing
title: Belief Propagation
understanding: 0
---

Message-passing algorithm for exact Bayesian inference in tree-structured graphical models: each node maintains bottom-up evidential support λ(B_i) = P(D^d|B_i) and top-down anticipatory support π(B_i) = P(B_i|D^u), with posterior P(B_i) ∝ λ(B_i)·π(B_i); messages diffuse through the network in a single pass equal to the graph diameter, with the two-parameter decoupling preventing infinite update loops.

## Reading Path
- [[pearl-reverend-bayes-1982]] (unread) — original formulation; proves single-pass convergence, derives propagation equations, demonstrates on binary tree token game; AAAI-82

## Connections
- [[message-passing]] — specializes: BP is the Bayesian-inference instance of message passing on trees.
- [[sum-product-algorithm]] — instantiates: BP is sum-product on a probabilistic graphical model; lambda/pi messages are the backward/forward passes.