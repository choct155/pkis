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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:framework:pharmacokinetic-modeling
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch19
tags:
- mechanistic-model
- differential-equations
- compartment-model
- informative-priors
- risk-assessment
title: Physiological Pharmacokinetic Modeling
understanding: 0
---

## Definition
A mechanistic modeling framework in which the concentration of a compound (drug or toxin) in the body is described by a system of first-order differential equations over physiological 'compartments' (e.g. well-perfused tissue, poorly perfused tissue, fat, liver), each parameterized by interpretable physical quantities: compartment volume, blood flow, partition coefficient, and metabolic constants (e.g. Michaelis-Menten coefficients). Given parameters and exposure conditions, the ODE system is solved numerically to predict observable concentrations (e.g. in blood and exhaled air) as nonlinear functions g_m(omega, E, t) of the parameters; these become the mean of a (typically lognormal) measurement model. Because the parameters of a multi-compartment model are essentially impossible to identify from concentration data alone (the inverse problem is ill-conditioned, resembling the estimation of decay rates of mixed exponentials), the framework's signature advantage is that physically meaningful parameters can be assigned informative priors drawn from physiological literature and allometric scaling. Embedding such a model in a hierarchical Bayesian structure separates posterior parameter uncertainty from genuine inter-individual population variation, yielding a posterior usable directly for uncertainty analysis in risk assessment. Illustrated by the BDA3 Ch. 19 perchloroethylene (PERC) example.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]