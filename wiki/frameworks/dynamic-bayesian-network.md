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
- knowledge-representation
- time-series
extends:
- bayesian-networks
id: pkis:framework:dynamic-bayesian-network
instantiates:
- state-space-models
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch14
tags:
- dbn
- temporal-model
- factored-representation
- transition-model
- sensor-model
- unrolling
- first-order-markov
- sensor-failure
- slam
title: Dynamic Bayesian Network (DBN)
understanding: 0
---

## Definition
A dynamic Bayesian network extends the semantics of standard Bayesian networks to temporal probability models: each time slice may contain any number of state variables X_t and evidence variables E_t, with variables, links, and conditional distributions replicated identically from slice to slice (time-homogeneous), and edges restricted so each variable has parents only within its own slice or the immediately preceding slice (first-order Markov). A DBN is thus equivalent to a Bayesian network with infinitely many variables, fully specified by P(X_0), the transition model P(X_{t+1} | X_t), and the sensor model P(E_t | X_t) on a single slice.

## Relation to HMMs and Kalman filters
Every HMM is a DBN with one state and one evidence variable, and every discrete-variable DBN can be flattened into an HMM by merging all state variables into a single megavariable; every Kalman filter is a DBN with continuous, linear-Gaussian conditionals. The decisive advantage of the DBN is its *factored* representation: a process with n discrete variables (each up to d values, at most k parents) needs only O(n d k) parameters versus the HMM's O(d^{2n}) transition matrix - linear rather than exponential in the number of variables (e.g. reducing 5 x 10^{29} probabilities to a few thousand for the vacuum robot). Unlike a Kalman filter, whose posterior is always a single multivariate Gaussian, a DBN can represent arbitrary distributions, including multimodal beliefs and mixed discrete-continuous state.

## Modeling sensor behavior
DBNs cleanly express realistic sensor phenomena. A naive Gaussian error model wrongly believes a single spurious reading; a transient failure model (a fixed probability of returning a wrong value) gives belief 'inertia' against blips; and a persistent failure model adds a status variable (e.g. BMBroken) joined by a persistence arc so the network can infer that a sensor is broken rather than that the world changed. DBNs also capture sensor drift, decalibration, and exogenous effects.

## Inference
Given observations, a DBN is unrolled into a finite Bayesian network and solved with any standard algorithm (variable elimination, clustering). Naive unrolling costs O(t) space and grows per update, but running variable elimination in temporal order - keeping at most two slices in memory - mimics recursive filtering at constant space/time per step. The catch: that 'constant' is generally exponential in the number of state variables (max factor O(d^{n+k})), which motivates approximate methods such as particle filtering. DBNs were introduced to AI by Dean and Kanazawa (1989).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[state-space-models]] — instantiates: A DBN is a factored state-space model with per-slice state and evidence variables.
- [[bayesian-networks]] — extends: A DBN extends standard Bayesian-network semantics to an unbounded sequence of replicated time slices.
[To be populated during integration]