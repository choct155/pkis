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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
- signal-processing
id: pkis:framework:linear-gaussian-ssm
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch08
tags:
- state-space-model
- kalman
- linear-dynamical-system
- Gaussian
- time-series
title: Linear Gaussian State Space Model (LG-SSM)
understanding: 0
---

## Definition
$$p(\mathbf{z}_t|\mathbf{z}_{t-1},\mathbf{u}_t) = \mathcal{N}(\mathbf{z}_t|\mathbf{F}_t\mathbf{z}_{t-1}+\mathbf{B}_t\mathbf{u}_t+\mathbf{b}_t, Q_t), \quad p(\mathbf{y}_t|\mathbf{z}_t,\mathbf{u}_t) = \mathcal{N}(\mathbf{y}_t|\mathbf{H}_t\mathbf{z}_t+\mathbf{D}_t\mathbf{u}_t+\mathbf{d}_t, R_t)$$

A state-space model in which both the transition and observation distributions are linear functions of the state with additive Gaussian noise, also called a **linear dynamical system (LDS)**. Because all conditional distributions are Gaussian, the entire joint $p(\mathbf{y}_{1:T},\mathbf{z}_{1:T})$ is a multivariate Gaussian, and exact filtering/smoothing runs in $O(T N_z^3)$ time.

### Why it matters
LG-SSMs are the canonical tractable SSM: they underlie the Kalman filter, Kalman smoother, recursive least squares, and structural time-series models. They also serve as the local linearization target for nonlinear extensions such as the EKF and UKF.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]