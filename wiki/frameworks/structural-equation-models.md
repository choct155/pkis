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
contrasts-with:
- potential-outcomes-framework
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
- econometrics
- social-science-methods
id: pkis:framework:structural-equation-models
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch05
specializes:
- structural-causal-models
tags:
- sem
- causal-inference
- econometrics
- path-diagrams
- wright
- haavelmo
title: Structural Equation Models (Causal Reading)
understanding: 0
uses:
- d-separation
---

## Definition
A modeling framework, originated by Wright (1921, path analysis) and the Cowles Commission econometricians (Haavelmo 1943; Koopmans; Marschak; Simon), in which a system of equations x_i = f_i(pa_i, e_i) — one per variable — encodes qualitative cause-effect knowledge so it can be combined with statistical data to yield quantitative causal claims. The defining (and, Pearl argues, widely forgotten) feature of a STRUCTURAL equation is that its coefficient carries a causal meaning fixed PRIOR to and INDEPENDENTLY of any statistical relationship among its constituents: the equality sign is asymmetric ('is determined by', behaving like an assignment :=), not algebraic. Pearl's chapter reinstates this reading against the dominant modern view (Holland, Muthen, Bollen) that treats a structural equation as merely a shorthand for a conditional density or covariance summary, and shows that the 'self-containment'/'isolation' condition cov(x,e)=0 is neither necessary nor sufficient for the causal interpretation of the coefficient. Graphical methods (causal diagrams, d-separation) supply the missing mathematical notation that the founders left implicit.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[potential-outcomes-framework]] — contrasts-with: Pearl's two mathematically-equivalent languages for causality; SEM/path-analysis vs Neyman-Rubin potential outcomes.
- [[d-separation]] — uses: d-separation characterizes the testable zero-partial-correlation content of a linear SEM.
- [[structural-causal-models]] — specializes: Linear/parametric SEM is the path-coefficient special case of the general nonparametric SCM x_i = f_i(pa_i, e_i).
[To be populated during integration]