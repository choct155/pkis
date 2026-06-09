---
aliases: []
also_type: []
analogous-to:
- optimal-linear-filter
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
- bayesian-stats
- information-theory
id: pkis:technique:matched-filter
instantiates:
- signal-detection-theory
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch14
tags:
- detection
- signal-processing
- signal-to-noise-ratio
- linear-filter
- radar
title: Matched Filter
understanding: 0
uses:
- likelihood-ratio-evidence
---

## Definition
The receiver front-end design that maximizes output signal-to-noise ratio for a known signal shape in additive noise. Historically (Jaynes PT:LOS Ch. 14) it was derived empirically by electrical engineers, then as a variational principle: choose the linear input-stage response that maximizes the ratio (peak signal)^2 / (mean-square noise). First obtained by W. W. Hansen (1941) and rediscovered independently by dozens of workers through the 1950s (satirized in Peter Elias's 1958 editorial 'Two famous papers'). Jaynes' key insight is that for a linear system with Gaussian noise the matched filter is *identical* to the optimal Bayesian/decision-theoretic solution: applying Bayes' theorem in logarithmic (decibel) form, the evidence increment for S1 over S0 is log[p(V|S1)/p(V|S0)] = const + (S1-S0)V/sigma^2 (14.55), so the observed voltage is itself a linear function of the posterior log-odds. The two conceptually distinct approaches — maximize SNR vs. maximize posterior probability — must therefore give the same answer, which the robot's viewpoint makes obvious in advance.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[likelihood-ratio-evidence]] — uses
- [[optimal-linear-filter]] — analogous-to
- [[signal-detection-theory]] — instantiates
[To be populated during integration]