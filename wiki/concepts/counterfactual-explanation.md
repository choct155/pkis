---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- interpretability
- causal-inference
id: pkis:concept:counterfactual-explanation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch33
tags:
- interpretability
- recourse
- actionability
- counterfactual
- fairness
title: Counterfactual Explanation
understanding: 0
---

## Definition
A **counterfactual explanation** for a prediction $f(x) = y$ is a minimal perturbation $\delta$ such that $f(x + \delta) = y'\neq y$, with $y'$ being a desired alternative outcome:
$$\delta^* = \arg\min_{\delta} \|\delta\|_p \quad \text{s.t.} \quad f(x+\delta) = y'$$

The explanation is the pair $(x, x + \delta^*)$, which answers the question: *"What is the smallest change to the input that would change the decision?"

### Why it matters
Counterfactual explanations provide **actionable recourse**: a denied loan applicant learns the minimal changes (increase income by \$5k, reduce debt by \$10k) that would flip the decision. This is directly useful for individual-level appeals and is increasingly a legal requirement in automated decision-making (e.g., GDPR Article 22). The choice of distance metric $\|\cdot\|_p$, which features are mutable, and whether the perturbed point must lie on the data manifold are critical design decisions with large effects on the explanation's practical usefulness.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]