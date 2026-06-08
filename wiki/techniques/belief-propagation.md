---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-08'
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

## Belief Propagation as Probabilistic Message Passing
Belief propagation is the probabilistic instance of the **sum-product algorithm** applied to a tree-structured graphical model: the $\lambda$ (bottom-up evidential) and $\pi$ (top-down anticipatory) messages are exactly the backward and forward sum-product messages, and the posterior $P(B_i)\propto\lambda(B_i)\,\pi(B_i)$ is the product of the two passes that, in MacKay's path-counting view, gives the weight of configurations through a node. Reading BP this way clarifies that its single-pass, graph-diameter convergence is the generic property of message passing on trees (where any node separates the graph into independent subtrees), not a quirk of Bayesian inference. The same machinery becomes the **max-product / min-sum** algorithm when one seeks the single most probable configuration instead of marginals.