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
- causal-analysis
id: pkis:framework:markovian-causal-model
instantiates:
- bayesian-networks
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch01
specializes:
- structural-causal-models
tags:
- causality
- functional-equations
- causal-markov-condition
- exogenous-variables
- dag
- reichenbach
title: Markovian Causal Model
understanding: 0
---

## Definition
A functional causal model $\{x_i = f_i(pa_i, u_i)\}_{i=1}^n$ whose causal diagram is acyclic **and** whose background (error) variables $U_1,\dots,U_n$ are *jointly independent*. Acyclicity alone (with arbitrary error dependence) gives only a *semi-Markovian* model; adding error independence makes it Markovian.

One-line intuition: a Markovian model is a causal world with no hidden common causes — every dependence between observed variables is explained by the arrows in the graph.

### Causal Markov Condition (Theorem 1.4.1)
Every Markovian causal model $M$ induces a distribution $P(x_1,\dots,x_n)$ satisfying the parental Markov condition relative to its diagram $G$: each $X_i$ is independent of its nondescendants given its parents $PA_i$. Proof sketch: $\{PA_i,U_i\}$ determines $X_i$, so $P(x,u)$ is Markov relative to the augmented DAG $G(X,U)$ in which the $U_i$ are explicit roots; the result follows by d-separation on $G(X,U)$.

### Two underlying assumptions
The error independence rests on (1) including in the model every variable that is a cause of two or more others, and (2) Reichenbach's common-cause principle ("no correlation without causation"). Together these force the $U_i$ to be mutually independent.

### Why it matters
Markovianity is the bridge from causal structure to ordinary Bayesian-network factorization (1.33): once $P(x_i \mid pa_i)$ is estimated, all probabilistic properties are fixed regardless of the actual $f_i$ or $P(u_i)$ (Druzdzel–Simon). It explains why the parental Markov condition is so often treated as an inherent feature of causal models, and it is the standard simplifying assumption under which causal effects become identifiable.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-networks]] — instantiates
- [[structural-causal-models]] — specializes
[To be populated during integration]