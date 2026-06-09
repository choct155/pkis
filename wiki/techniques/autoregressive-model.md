---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- deep-learning
- statistical-learning
id: pkis:technique:autoregressive-model
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch21
specializes:
- bayesian-networks
tags:
- generative-model
- time-series
- sequence-modeling
- no-latent-variables
title: Autoregressive Model
understanding: 0
---

## Definition
A generative model in which each element x_i of the data vector is predicted from other elements, with no latent variables. For fixed-size x it is a fully observable (possibly fully connected) Bayes net, so computing the likelihood of a data vector, predicting a single missing variable, and sampling are all trivial. The most common application is time series, where an AR model of order k predicts x_t from x_{t-k},...,x_{t-1}; in HMM terms it is a non-hidden Markov model, and an n-gram model is an AR model of order n−1. In the classical real-valued case the conditional P(x_t | x_{t-k},...,x_{t-1}) is a linear-Gaussian (standard linear regression) model solved by the Yule–Walker equations. A deep autoregressive model replaces the linear-Gaussian conditional with an arbitrary deep network and a suitable output layer; e.g. DeepMind's WaveNet implements a nonlinear AR model of order 4800 over raw audio with a convolutional structure for realistic speech generation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-networks]] — specializes: a fixed-size AR model is a fully observable, possibly fully connected Bayes net
[To be populated during integration]