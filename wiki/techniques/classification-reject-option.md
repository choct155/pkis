---
aliases: []
also_type: []
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
- machine-learning
- decision-theory
extends:
- cost-sensitive-classification
id: pkis:technique:classification-reject-option
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch05
tags:
- reject-option
- abstention
- chow-rule
- classification
- confidence-threshold
title: Classification with Reject Option (Chow's Rule)
understanding: 0
uses:
- loss-function-posterior-expected-loss
- calibration
---

## Definition
Introduce a reject action (label 0) alongside the $C$ class labels, with loss

$$\ell(y^*,a)=\begin{cases}0 & y^*=a,\;a\in\{1,\ldots,C\}\\\lambda_r & a=0\\\lambda_e & \text{otherwise}\end{cases}$$

Chow's rule (1970) states that the Bayes-optimal policy is:

$$a^* = \begin{cases}\arg\max_y p(y|x) & \text{if } \max_y p(y|x) > \lambda^*\\\text{reject} & \text{otherwise}\end{cases}$$

where $\lambda^* = 1 - \lambda_r/\lambda_e$ is the confidence threshold.

### Why it matters
In safety-critical or high-stakes settings (medicine, finance, autonomous systems), the cost of a wrong committed answer may vastly exceed the cost of abstaining. Chow's rule provides the decision-theoretically optimal abstention policy: reject exactly when the posterior probability of the best class is too low relative to the cost ratio $\lambda_r/\lambda_e$. IBM Watson's Jeopardy strategy (buzz-in only when sufficiently confident) is a practical instantiation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[calibration]] — uses: Chow's rule requires well-calibrated posteriors to set the threshold meaningfully
- [[loss-function-posterior-expected-loss]] — uses
- [[cost-sensitive-classification]] — extends
[To be populated during integration]