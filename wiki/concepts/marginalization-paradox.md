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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:concept:marginalization-paradox
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch15
tags:
- jaynes
- dawid-stone-zidek
- improper-prior
- nuisance-parameter
- reduction-principle
- paradox
- complete-ignorance
title: Marginalization Paradox
understanding: 0
---

## Definition
The apparent inconsistency of Dawid, Stone & Zidek (1973): a conscientious Bayesian B1, with data x=(y,z), parameters theta=(eta,zeta), nuisance eta integrated out under prior pi(eta,zeta), obtains a marginal posterior p(zeta|x). A 'lazy' Bayesian B2 notes that when the sampling distribution for z is independent of eta (p(z|eta,zeta)=p(z|zeta)) and B1's posterior 'is a function of z only', it seems B2 should reproduce B1's result by applying Bayes' theorem to the reduced model p(z|zeta) — yet for no prior pi(zeta) can he do so. DSZ blamed B1's use of an improper prior for eta, concluding that improper priors generate inconsistencies; the result was institutionalized and used to discredit Bayesian inference for decades.

## Jaynes's resolution
B2's 'reduction principle' (15.61) is an intuitive guess that does *not* follow from the rules of probability theory; B1 and B2 simply solve *different problems* with different prior information I_1, I_2 — which Jeffreys-style notation P(A|B I) (always carrying the prior information / model) makes immediately clear. B1's marginal posterior remains a *functional* of the eta-prior even when y drops out, because that prior is genuine information B2 ignores. DSZ's proof that proper priors force agreement uses mutually contradictory assumptions: D. A. S. Fraser saw that with a proper (hence informative) prior the separation property (15.60) *cannot* hold, so the reduction step fails — the paradox dissolves not by B1/B2 agreeing but because B2's principle is inapplicable. Salvage: a prior leaving B1 and B2 in agreement must be *completely uninformative* about eta, giving an objective definition of complete ignorance arising directly from the sum/product rules (for scale parameters this is the k=1 Jeffreys prior eta^{-1}). DSZ's Example #5 shows the deeper point: the mere qualitative *existence* of a nuisance parameter in the model can already be relevant prior information (kernel incompleteness in the governing Fredholm equation), so the phenomenon is not even essentially about nuisance parameters.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]