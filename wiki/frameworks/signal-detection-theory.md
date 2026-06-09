---
aliases: []
also_type: []
applies:
- decision-theory-foundations
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
contrasts-with:
- hypothesis-testing
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- information-theory
id: pkis:framework:signal-detection-theory
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch14
tags:
- detection
- decision-theory
- likelihood-ratio
- false-alarm
- significance-test
title: Signal Detection Theory
understanding: 0
uses:
- likelihood-ratio-evidence
- expected-loss
---

## Definition
The theory of deciding, from a noisy observation, which of several hypothesized signals is present. Jaynes (PT:LOS Ch. 14) treats the canonical binary problem: a linear system delivers an observed voltage V = S + N where the noise N has prior pdf W(N), and we must choose between 'no signal' (S0 = 0) and 'signal present' (S1). A decision rule p(D|V) maps observations to decisions; it may be deterministic (values 0/1) or randomized (a genuine probability distribution, which simplifies the variational analysis). Jaynes emphasizes that the detection problem, Laplace's problem of detecting unknown systematic influences in celestial mechanics, Shewhart's industrial quality-control drift problem, and the statistician's 'significance test' are all the *same problem*, repeatedly rediscovered. The central theorem of the field is that essentially every proposed optimality criterion — minimax, the Bayes criterion, Neyman-Pearson, and Siegert's 'ideal observer' (minimize total error probability) — reduces to a *likelihood-ratio (probability-ratio) threshold test*; the criteria differ only in where they place the threshold. Two error types arise in the binary case: the false alarm A = (D1, S0) and the false rest R = (D0, S1), and the decision rule (14.34) chooses D1 when the likelihood ratio p(V|S1)/p(V|S0) exceeds qL_a/pL_r. For Gaussian noise of variance sigma^2 the false-alarm and false-rest probabilities are governed by the cumulative normal Phi at a threshold set by the signal-to-noise ratio s = S1/sigma, yielding extremely reliable operation for s > 6. From the Bayesian ('robot') viewpoint the whole apparatus collapses: one simply computes posterior odds O(S1|VX) = O(S1|X) p(V|S1)/p(V|S0) (14.53) and applies the loss function — recovering the same rule in two lines.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hypothesis-testing]] — contrasts-with
- [[decision-theory-foundations]] — applies
- [[expected-loss]] — uses
- [[likelihood-ratio-evidence]] — uses
[To be populated during integration]