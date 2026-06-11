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
- causal-inference
- statistics
id: pkis:concept:m-bias-bias-amplification
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch36
tags:
- collider-bias
- covariate-selection
- confounding
- sensitivity-analysis
- z-bias
title: m-Bias and Bias Amplification
understanding: 0
---

## Definition
**m-bias** arises when a researcher conditions on a *collider* $D$ that is influenced by two separate unmeasured confounders: one confounding $A$ and one confounding $Y$. Graphically the structure forms an 'M' shape ($U_A \to A$, $U_A \to D \leftarrow U_Y$, $U_Y \to Y$). Conditioning on $D$ opens a non-causal path $A \leftarrow U_A \to D \leftarrow U_Y \to Y$, inducing spurious association even if $D$ is pre-treatment.

**Bias amplification** (z-bias) is a related phenomenon: including an instrumental-like variable that strongly predicts $A$ but not $Y$ in an adjustment set can *increase* bias in the presence of unobserved confounding, because the IPTW weights $1/g(X)$ become more extreme, magnifying the contribution of unobserved confounders. Formally, under the Austen sensitivity model:
$$\text{bias} \propto \mathbb{E}\!\left[\frac{1}{g(X)}+\frac{1}{1-g(X)}\right],$$
which grows when propensity scores become extreme.

### Why it matters
Both phenomena show that naïvely conditioning on more pre-treatment variables does not monotonically reduce bias. Principled covariate selection—guided by the backdoor criterion or the VanderWeele–Shpitser heuristic—is necessary to avoid these pitfalls.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]