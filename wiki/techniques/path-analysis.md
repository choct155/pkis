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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
- social-science-methods
id: pkis:technique:path-analysis
instantiates:
- structural-equation-models
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch05
tags:
- wright
- path-coefficients
- correlation-decomposition
- identifiability
title: Path Analysis (Method of Path Coefficients)
understanding: 0
uses:
- path-coefficient
---

## Definition
Sewall Wright's (1919-1921) technique for computing cause-effect magnitudes from correlations given a path diagram believed to represent the data-generating process. One writes one equation per pair (X_i, X_j) equating the standardized correlation rho_ij with a sum of products of path coefficients and residual correlations taken along every path connecting the two variables (Wright's tracing rules), then attempts to solve for the path coefficients in terms of observed correlations. A coefficient with a unique solution independent of unobserved residual correlations is IDENTIFIABLE; a model in which every correlation matrix is compatible with some choice of coefficients is untestable/saturated (just-identified). Wright's method is partly graphical, partly algebraic; the modern directed-graph theory it seeded lets testability and identifiability be settled in purely graphical terms before data collection and extends the analysis to nonlinear/nonparametric models. Wright insisted 'prior knowledge of the causal relations is assumed as prerequisite.'

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[path-coefficient]] — uses: Path analysis solves for path coefficients from correlations along traced paths.
- [[structural-equation-models]] — instantiates: Wright's method of path coefficients is the original concrete SEM technique.
[To be populated during integration]