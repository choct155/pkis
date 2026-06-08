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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:framework:sampling-theory
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch37
tags:
- frequentist
- p-value
- significance-level
- sampling-distribution
- null-hypothesis
title: Sampling Theory (Frequentist Statistics)
understanding: 0
---

## Definition
**Sampling theory** (the frequentist school of statistics) seeks inference procedures with guaranteed long-run properties under repeated sampling, given minimal assumptions. Probability is defined as the limiting frequency of outcomes over imagined repetitions of the experiment, so the central objects are the *sampling distribution* of a statistic and frequency-based guarantees (significance levels, confidence levels, power).

The canonical procedure is the significance test: choose a statistic $T(D)$ measuring deviation from a null hypothesis $H_0$, derive its sampling distribution *assuming $H_0$ is true*, and report a $p$-value:
$$p = P\big(T(D') \ge T(D_\text{obs}) \mid H_0\big),$$
the probability that a repetition $D'$ would give a result as extreme as, or more extreme than, what was observed. Crucially, $H_0$ is rejected purely on how *unexpected* the data are under $H_0$ — the alternative $H_1$ and its predictions play no role in the test statistic.

### Why it matters
Sampling theory dominates published empirical work: confidence intervals, significance levels, and $p$-values are the lingua franca of most journals. MacKay treats it as the contrasting framework against which Bayesian methods are sharpened. Its appeal is robustness — guarantees that hold without committing to a prior or a full alternative model.

### Failure modes MacKay highlights
Because the $p$-value integrates over the whole sample space (outcomes that did *not* occur), it depends on the experimenter's intentions and stopping rule, violating the likelihood principle. It can be 'trigger-happy', rejecting $H_0$ on data that actually favour it, and can miss evidence that intuition and Bayes both judge strong.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]