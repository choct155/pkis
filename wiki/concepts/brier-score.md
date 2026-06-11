---
aliases: []
also_type: []
applies:
- calibration
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- cross-entropy-loss
- kl-divergence
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
- meteorology
id: pkis:concept:brier-score
instantiates:
- scoring-rules
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch05
- murphy-pml2-advanced-ch14
tags:
- proper-scoring-rule
- probabilistic-forecast
- calibration
- evaluation
- squared-loss
title: Brier Score
understanding: 0
uses:
- calibration
---

## Definition
$$\text{BS}(p,q) \triangleq \frac{1}{N}\sum_{n=1}^{N}\sum_{c=1}^{C}(q_{nc}-y_{nc})^2$$

where $y_{nc}=1$ iff observation $n$ belongs to class $c$ (one-hot encoding), and $q_{nc}=q(Y_n=c|x_n)$ is the predicted probability. For binary classification the convention is the simpler form $\frac{1}{N}\sum_n(q_n-y_n)^2\in[0,1]$.

### Why it matters
The Brier score is a **proper scoring rule** (minimised iff $q=p$), and a mean-squared-error analogue for probabilistic forecasts. Compared with cross-entropy / log-loss, it is less sensitive to extremely rare or extremely common events because it is based on squared rather than logarithmic differences. The **Brier Skill Score** $\text{BSS}=1-\text{BS}/\text{BS}_{\text{ref}}$ provides a relative metric against a reference model (e.g., the empirical base rate), with 1 being perfect and 0 indicating no improvement.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[calibration]] — applies
- [[kl-divergence]] — contrasts-with
- [[calibration]] — uses
- [[scoring-rules]] — instantiates
- [[cross-entropy-loss]] — contrasts-with
[To be populated during integration]