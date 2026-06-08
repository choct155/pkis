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

## Belief Propagation as Forward-Backward on a Trellis
MacKay explicitly lists '**belief propagation**' as a synonym for the forward-backward / BCJR algorithm that performs exact bitwise marginalization on a code's **trellis**. Because a trellis is a chain (tree-structured) graph, belief propagation on it is exact: the $\alpha$ (forward) and $\beta$ (backward) messages are the standard BP messages, and the per-bit posteriors are recovered by multiplying incoming messages at each time slice. This is the same algorithm that, run on the loopy factor graph of a parity-check code, becomes the (approximate) iterative decoder for LDPC and turbo codes.

## Loopy belief propagation and the limits of exactness
Belief propagation (the sum-product algorithm on a factor graph) is *exact* only when the graph is tree-like, because the message-creation schedule relies on each node receiving all of its dependencies exactly once. On a graph with cycles there is no such schedule.

Two responses exist. The principled one is to make the graph a tree by clustering variables (the junction tree algorithm), paying a cost exponential in treewidth. The pragmatic one is **loopy belief propagation**: run the local message updates as if the graph were a tree, iterate, and hope for convergence. Loopy BP is not guaranteed to converge and, when it does, generally returns only approximate marginals — yet it is of enormous practical importance, most famously in the iterative decoding of sparse-graph error-correcting codes (LDPC, turbo) where it works strikingly well. A complementary 'factorization view' of the updates,
$$P^*(\mathbf{x}) = \prod_m \phi_m(\mathbf{x}_m)\prod_n \psi_n(x_n),$$
in which $\psi_n$ converges to the marginal $Z_n(x_n)$, holds whether or not the graph is a tree, clarifying what loopy BP is attempting to compute.