---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- bayesian-stats
- knowledge-representation
- causal-analysis
generalizes:
- naive-bayes-model
id: pkis:framework:bayesian-networks
knowledge_type: framework
maturity: settled
related_concepts:
- '[[directed-graphical-models]]'
- '[[belief-propagation]]'
- '[[conditional-independence]]'
- '[[d-separation]]'
sources:
- '[[pearl-reverend-bayes-1982]]'
tags:
- probability-theory
- graph-theory
- expert-systems
title: Bayesian Networks
understanding: 0
uses:
- variable-elimination
- likelihood-weighting
- gibbs-sampler
---

Directed acyclic graphs where nodes represent random variables and directed edges encode conditional probability tables P(B|A); the joint distribution factorizes as the product of local conditional distributions; inference proceeds via belief propagation (exact on trees, approximate via loopy BP on general DAGs) — Pearl's 1982 paper presents the proto-form of this framework for hierarchical tree-structured expert systems. Classification note: bayesian-networks specializes directed-graphical-models; the distinction is that BNs emphasize the inference algorithm (BP) while the DGM framework is more general.

## Reading Path
- [[pearl-reverend-bayes-1982]] (unread) — earliest formulation: hierarchical inference net, local message passing, proof of single-pass correctness

## Connections
- [[gibbs-sampler]] — uses
- [[likelihood-weighting]] — uses
- [[variable-elimination]] — uses
- [[naive-bayes-model]] — generalizes