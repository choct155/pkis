---
aliases: []
also_type: []
analogous-to:
- algorithmic-fairness
applies:
- interpretable-ml-ecosystem
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- interpretability
- philosophy-of-science
id: pkis:principle:no-universal-interpretability-metric
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch33
tags:
- interpretability
- evaluation
- impossibility
- user-study
- downstream-performance
title: No Universal Metric of Interpretability
understanding: 0
---

## Definition
**Principle:** There is no single, context-free mathematical definition of interpretability, and no universal metric for evaluating whether an explanation is good.

Formally, for any proposed scalar interpretability metric $\mathcal{I}(E, f)$, there exist contexts $(\text{user}, \text{end-task})$ and pairs of explanations $E_1, E_2$ such that $\mathcal{I}(E_1, f) > \mathcal{I}(E_2, f)$ yet $E_2$ produces strictly better downstream performance than $E_1$ in that context.

The corollary is that the only ultimate criterion is **downstream performance**: how well the explanation enables the user to accomplish their specific end-task given their context, constraints, and cognitive characteristics.

### Why it matters
This principle disciplines interpretability research: one cannot evaluate a new explanation method in isolation—the evaluation must specify context, end-task, and downstream metric. It mirrors similar impossibility results in fairness (no single fairness metric satisfies all desiderata simultaneously) and in general ML evaluation (accuracy, precision, recall, log-likelihood, calibration can all conflict). The practical implication is that computational property checks (faithfulness, sparsity, stability) are necessary but not sufficient—they are proxies for downstream performance that must ultimately be validated via user studies.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[algorithmic-fairness]] — analogous-to: Both fields face impossibility results: no single metric satisfies all desiderata simultaneously.
- [[interpretable-ml-ecosystem]] — applies
[To be populated during integration]