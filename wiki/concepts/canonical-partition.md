---
aliases: []
also_type: []
analogous-to:
- principal-stratification
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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
- bayesian-stats
id: pkis:concept:canonical-partition
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- partial-identification-bounds
related_concepts: []
sources:
- pearl-causality-ch08
specializes:
- potential-outcomes-framework
tags:
- canonical-partition
- response-variable
- mapping-variable
- principal-strata
- complier-typology
- equivalence-classes
- counterfactual-types
title: Canonical Partition (Response Variables)
understanding: 0
---

## Definition
A device for replacing an arbitrary, possibly continuous and high-dimensional latent variable U by a finite-state variable without changing any observable or interventional prediction (Pearl 1994a). Because a binary child can stand in only four possible functional relations to a binary parent (f0: y=0, f1: y=x, f2: y!=x, f3: y=1), as U ranges over its domain its only effect is to switch among these four functions. This partitions U's domain into equivalence classes; the class index R(u) -- called a *response variable* (Balke & Pearl 1994) or *mapping variable* (Heckerman & Shachter 1995) -- is a state-minimal sufficient summary, and P(u) collapses to P(r).

For the binary Z->X->Y model, U splits into 16 classes indexed by two four-valued variables: the **compliance type** R_x and the **response type** R_y. The compliance typology (Imbens & Rubin 1997) is *never-taker, complier, defier, always-taker*; the response typology (Heckerman & Shachter 1995) is *never-recover, helped, hurt, always-recover*. These types map directly onto the counterfactuals Y_{x0}, Y_{x1} of the potential-outcomes framework (helped = Y_{x1}=1, Y_{x0}=0). The joint P(r_x, r_y) needs 15 free parameters and fully specifies the model, turning ACE(X->Y) = P(r_y=1) - P(r_y=2) and the constraints linking it to observed P(y,x|z) into *linear* relations -- the key step that makes linear-programming bounds and Gibbs-sampling Bayesian estimation tractable. (Closely related to, and a precursor of, principal stratification.)

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[partial-identification-bounds]] — prerequisite-of: the finite response-type encoding is needed before LP bounds can be set up
- [[principal-stratification]] — analogous-to: compliance-type strata; principal strata are the same latent partition by potential treatment
- [[potential-outcomes-framework]] — specializes: response types are a finite enumeration of counterfactual outcome patterns Y_x
[To be populated during integration]