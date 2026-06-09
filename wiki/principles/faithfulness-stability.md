---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
- statistical-learning
- bayesian-stats
id: pkis:principle:faithfulness-stability
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- ic-algorithm
related_concepts: []
sources:
- pearl-causality-ch02
tags:
- faithfulness
- stability
- perfect-map
- dag-isomorphism
- conditional-independence
- zero-measure
title: Faithfulness (Stability)
understanding: 0
uses:
- d-separation
---

## Definition
The assumption that every conditional independence holding in the data distribution P is *structural* -- entailed by the DAG topology via d-separation -- rather than accidental, i.e. arising from a fine-tuned cancellation of parameters. Formally (Pearl's Definition 2.4.1, Stability), a model M=<D,Theta_D> is stable iff its independencies survive every reparameterization: I(P(D,Theta_D)) subset of I(P(D,Theta'_D)) for all Theta'. Equivalently P is a *perfect map* of D: (X indep Y | Z)_P iff (X indep Y | Z)_D. Known as stability or DAG-isomorphism (Pearl 1988) and faithfulness (Spirtes et al. 1993). It rules out pathological distributions such as the same-coins example where every pair is marginally independent yet pairwise dependent given the third, which admits three indistinguishable minimal structures; under faithfulness only the true collider A->C<-B retains its independence pattern as parameters vary. Justification: equality constraints among structural coefficients (e.g. alpha=-beta*gamma making X indep Y in a linear model) have zero Lebesgue measure when mechanisms vary independently, so they almost never occur naturally. The deeper rationale is *autonomy*: causal mechanisms are invariant relations that change independently of one another, so structural coefficients -- not derived correlations -- are the free parameters, and constraints among them are unstable. Under faithfulness (and no latent variables) every distribution has a unique minimal causal structure up to d-separation equivalence.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[d-separation]] — uses: Stability is defined as P being a perfect map: independence in P iff d-separation in D.
- [[ic-algorithm]] — prerequisite-of: IC takes a *stable* distribution as input; without faithfulness independencies need not reflect d-separation.
[To be populated during integration]