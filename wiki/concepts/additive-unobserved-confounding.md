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
date_updated: '2026-06-20'
domain:
- causal-inference
- econometrics
generalizes:
- two-stage-least-squares
id: pkis:concept:additive-unobserved-confounding
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch36
- cunningham-causal-inference-mixtape-ch08
tags:
- instrumental-variables
- exclusion-restriction
- unobserved-confounding
- integral-equation
- nonparametric-IV
title: Additive Unobserved Confounding (IV Identification Assumption)
understanding: 0
uses:
- instrumental-variables
- structural-causal-model
---

## Definition
In the instrumental variables framework, **additive unobserved confounding** assumes that the structural equation for the outcome separates into an observed-data component and an unobserved-confounder component with no interaction:
$$Y \leftarrow f(A, X) + f_U(U).$$
This implies the exclusion restriction (since $U$ does not interact with $A$) and that conditional treatment contrasts are identifiable:
$$\mathbb{E}[Y|X, \mathrm{do}(A=a)] - \mathbb{E}[Y|X, \mathrm{do}(A=a')] = f(a,X) - f(a',X).$$

Under this assumption and IV unconfoundedness ($U \perp\!\!\!\perp Z|X$), the function $\tilde{f}(a,x) = f(a,x)+\mathbb{E}[f_U(U)|X=x]$ satisfies
$$\mathbb{E}[Y|z,x] = \int \tilde{f}(a,x)\,p(a|z,x)\,da,$$
an integral equation that implicitly identifies $\tilde{f}$ from observed data whenever the instrument is sufficiently relevant.

### Why it matters
Additive unobserved confounding is a *non-parametric* assumption weaker than full linearity (e.g., 2SLS), enabling identification with flexible models for $f$. The implicit identification equation connects to kernel/neural-network-based IV estimators. The absence of interaction terms means 'everyone responds to treatment in the same way regardless of their unobserved characteristics', which is testable in specific designs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[two-stage-least-squares]] — generalizes: Additive confounding does not require linearity, generalising beyond 2SLS assumptions
- [[structural-causal-model]] — uses
- [[instrumental-variables]] — uses
[To be populated during integration]