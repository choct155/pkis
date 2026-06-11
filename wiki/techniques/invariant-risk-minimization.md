---
aliases: []
also_type: []
applies:
- spurious-correlations
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- distributionally-robust-optimization
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- causality
id: pkis:technique:invariant-risk-minimization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch19
specializes:
- domain-generalization
tags:
- domain-generalization
- causality
- spurious-correlations
- invariance
title: Invariant Risk Minimization (IRM)
understanding: 0
uses:
- causal-vs-anticausal-prediction
- faithfulness-stability
---

## Definition
IRM seeks a feature representation $\Phi: X \to H$ and linear classifier $w$ such that $w$ is simultaneously optimal across all training environments $j \in \mathcal{E}$:

$$\min_{w,\Phi}\sum_{j\in\mathcal{E}}\mathcal{R}^j(w\circ\Phi) \quad \text{s.t.}\quad w \in \arg\min_{\tilde{w}}\mathcal{R}^j(\tilde{w}\circ\Phi)\ \forall j$$

Practically, the constraint is relaxed and a gradient-norm penalty $\|\nabla_w \mathcal{R}^j(w\circ\Phi)\|^2$ is added to the objective.

### Why it matters
IRM operationalizes the *invariant causal prediction* principle in high-dimensional (e.g., pixel) spaces: a predictor that is simultaneously optimal in every environment must rely on causally stable features rather than spurious correlates. It is motivated by the observation that causal features have the same relationship to $Y$ across environments, whereas spurious features do not.

### Limitations
IRM has been shown to fail on covariate shift both theoretically and empirically, and to succeed mainly in anti-causal settings with sufficient environment diversity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[faithfulness-stability]] — uses
- [[distributionally-robust-optimization]] — contrasts-with
- [[causal-vs-anticausal-prediction]] — uses
- [[spurious-correlations]] — applies
- [[domain-generalization]] — specializes
[To be populated during integration]