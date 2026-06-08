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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:concept:likelihood-ratio-evidence
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch03
tags:
- likelihood-ratio
- bayes-factor
- prosecutors-fallacy
- base-rate
- weight-of-evidence
title: Likelihood Ratio as Evidence
understanding: 0
uses:
- bayesian-inference
---

## Definition
The contribution of a single body of data $D$ to a binary question $S$ vs. $\bar S$ is exactly the likelihood ratio $P(D\mid S)/P(D\mid \bar S)$, which multiplies the prior odds to give the posterior odds. Evidence is *relative*: data that raise the probability of one hypothesis must lower that of some other.

### Why it matters
It separates the data's contribution from the prior, which is essential in forensic and diagnostic reasoning. In MacKay's blood-trace example, type-O blood (60% frequent) found at the scene gives ratio $1/(2p_O)=0.83$ — *weak evidence against* the type-O suspect, not for him, because common evidence is expected anyway.

### The prosecutor's fallacy
Confusing $P(D\mid H)$ with $P(H\mid D)$ corrupts this reasoning. The wife-beater lawyer cites $P(\text{murder}\mid \text{beating})=1/1000$, but the relevant quantity is $P(\text{guilty}\mid \text{murdered \& beaten})\approx 95\%$. The likelihood ratio, applied correctly, is the antidote.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-inference]] — uses: posterior odds = likelihood ratio x prior odds, a direct application of Bayes' theorem
[To be populated during integration]