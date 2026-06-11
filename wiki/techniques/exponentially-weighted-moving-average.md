---
aliases: []
also_type: []
analogous-to:
- nonstationary-bandit-step-size
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
- signal-processing
id: pkis:technique:exponentially-weighted-moving-average
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch04
tags:
- online-learning
- recursive-estimation
- bias-correction
- Adam
title: Exponentially Weighted Moving Average (EWMA)
understanding: 0
uses:
- stochastic-gradient-descent
---

## Definition
$$\hat{\mu}_t = \beta\,\hat{\mu}_{t-1} + (1-\beta)\,y_t, \qquad \tilde{\mu}_t = \frac{\hat{\mu}_t}{1-\beta^t}$$

EWMA is a recursive online estimator that gives exponentially decaying weight $\beta^k(1-\beta)$ to an observation $k$ steps in the past, with a bias-correction term $1/(1-\beta^t)$ for the initial transient.

### Why it matters
EWMA is the standard method for tracking non-stationary signals in online learning: $\beta$ close to 1 gives long memory (slow adaptation), while $\beta$ close to 0 gives short memory (fast adaptation). The bias-corrected form is used in the Adam optimiser for gradient moment estimates (Kingma & Ba 2015). Unlike the plain running average (which weights all data equally), EWMA can track distribution shifts.

### Relationship to recursive MLE
The plain recursive mean $\hat{\mu}_t = \hat{\mu}_{t-1} + \frac{1}{t}(y_t - \hat{\mu}_{t-1})$ is a special case with time-varying step size $1/t$, which decreases to zero—appropriate for stationary distributions but not for non-stationary ones.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[stochastic-gradient-descent]] — uses: Adam optimizer uses bias-corrected EWMA for first and second moment estimates
- [[nonstationary-bandit-step-size]] — analogous-to: Both use fixed step-size updates to track non-stationary distributions
[To be populated during integration]