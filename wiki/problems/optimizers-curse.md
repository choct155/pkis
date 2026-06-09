---
aliases: []
also_type: []
analogous-to:
- regression-to-the-mean
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
contrasts-with:
- maximum-expected-utility-principle
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:problem:optimizers-curse
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch16
tags:
- decision-theory
- selection-bias
- order-statistics
- post-decision-disappointment
- winners-curse
title: Optimizer's Curse
understanding: 0
uses:
- bayesian-decision-analysis
---

## Definition
## Definition
The **optimizer's curse** is the systematic tendency for the *realized* utility of the action chosen by expected-utility maximization to fall short of its *estimated* utility, even when every individual estimate is unbiased (R&N Section 16.3.3). Because $\arg\max$ over noisy estimates preferentially selects whichever estimate happened to be most optimistic, the maximum is biased upward: the selection step — not the estimates — is the source of bias.

### The order-statistic argument
With $k$ choices of true utility 0 and independent unit-normal estimation errors, the chosen estimate $X^*=\max\{X_1,\ldots,X_k\}$ has CDF $F(x)^k$ and density $kf(x)F(x)^{k-1}$. The expected disappointment grows with $k$: about $0.85\sigma$ for $k=3$ and roughly $2\sigma$ for $k=30$. This is a computation of an order statistic.

### Manifestations and cure
The curse appears wherever utility-maximizing selection is ubiquitous: a drug that cured 9 of 10 patients but was picked from thousands is probably worse than one that cured 800 of 1000; advertised above-average funds; "miracle" drugs. It is the same phenomenon as the **winner's curse** in competitive bidding (overbidding wins the auction) and was called **post-decision disappointment** by Harrison and March (1984). Smith and Winkler (2006) brought it to decision analysts' attention. The cure is a **Bayesian** treatment: model $P(\widehat{EU}\mid EU)$ explicitly, put a prior on the true utilities, treat each estimate as evidence, and use the posterior mean — shrinking optimistic outliers back toward the prior.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[regression-to-the-mean]] — analogous-to: selecting the max and being disappointed is regression to the mean by another name
- [[bayesian-decision-analysis]] — uses: a Bayesian posterior treatment of estimates cures the curse
- [[maximum-expected-utility-principle]] — contrasts-with: the curse is the failure mode of naive argmax over noisy utility estimates
- Afflicts naive application of the maximum-expected-utility principle.
- Quantified via the distribution of an order statistic (the maximum).
- Cured by a Bayesian (shrinkage) treatment of utility estimates.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]