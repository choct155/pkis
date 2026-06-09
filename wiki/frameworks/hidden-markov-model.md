---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- state-space-models
- time-series
- statistical-learning
id: pkis:framework:hidden-markov-model
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch14
tags:
- hmm
- temporal-model
- discrete-state
- transition-model
- sensor-model
- markov-assumption
- speech-recognition
- matrix-formulation
title: Hidden Markov Model (HMM)
understanding: 0
---

## Definition
A hidden Markov model is a temporal probabilistic model in which the state of the process is described by a *single, discrete* random variable X_t whose possible values are the possible states of the world, observed only indirectly through evidence variables E_t. It is specified by three time-homogeneous components: a prior P(X_0), a transition model P(X_t | X_{t-1}), and a sensor (observation) model P(E_t | X_t), subject to the first-order Markov assumption P(X_t | X_{0:t-1}) = P(X_t | X_{t-1}) and the sensor Markov assumption P(E_t | X_{0:t}, E_{1:t-1}) = P(E_t | X_t). These yield the joint factorization P(X_{0:t}, E_{1:t}) = P(X_0) prod_i P(X_i | X_{i-1}) P(E_i | X_i).

## Matrix formulation
With S states, the transition model becomes an S x S matrix T with T_ij = P(X_t = j | X_{t-1} = i), and each observation is encoded in an S x S diagonal observation matrix O_t whose i-th diagonal entry is P(e_t | X_t = i). All the standard inference recursions then reduce to matrix-vector products: forward f_{1:t+1} = alpha O_{t+1} T^T f_{1:t}; backward b_{k+1:t} = T O_{k+1} b_{k+2:t}. The forward-backward algorithm therefore runs in O(S^2 t) time and O(S t) space, and the matrix form exposes optimizations such as constant-space smoothing (requires T invertible and no zero sensor entries) and constant-time fixed-lag smoothing via a backward transformation matrix B.

## Expressiveness limit
Any model with several state variables can be forced into the HMM framework by combining them into a single 'megavariable' over all tuples, but this is exponentially costly: n discrete variables of domain size d give a transition matrix of size O(d^{2n}). HMMs are thus an *atomic* representation (states are unstructured integer labels), which motivates the factored dynamic Bayesian network representation when many state variables are present. Despite this, HMMs are workhorses in speech recognition, language processing, and computational biology.

## Origin
The HMM and its inference/learning algorithms (including forward-backward) were developed by Baum and Petrie (1966).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]