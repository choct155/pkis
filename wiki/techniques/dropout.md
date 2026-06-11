---
aliases: []
also_type: []
analogous-to:
- bayesian-model-averaging
- ensemble-learning
applies:
- feedforward-neural-network
- overfitting-and-underfitting
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- deep-learning
- optimization
id: pkis:technique:dropout
instantiates:
- regularization
knowledge_type: technique
maturity: settled
related_concepts:
- '[[regularization]]'
- '[[neural-networks]]'
- '[[bias-variance-tradeoff]]'
sources:
- '[[nielsen-nndl]]'
tags:
- regularization
- neural-networks
- ensemble
- overfitting
title: Dropout
understanding: 0
---

Regularization technique for neural networks that randomly zeros out half the hidden neurons (with their connections) on each mini-batch forward pass during training; at test time all neurons are active but their outgoing weights are halved to compensate, approximating the geometric mean of an exponentially large ensemble of thinned networks.

## Reading Path
- [[nielsen-nndl-ch03]] (unread) — primary treatment; describes mechanics, motivation as implicit ensembling, and empirical results on MNIST

## Connections
- [[ensemble-learning]] — analogous-to: dropout at test time corresponds to an ensemble of sparse subnetworks
- [[overfitting-and-underfitting]] — applies
- [[bayesian-model-averaging]] — analogous-to
- [[feedforward-neural-network]] — applies
- [[regularization]] — instantiates