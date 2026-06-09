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
- bayesian-stats
id: pkis:principle:conservation-of-logical-independence
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch06
tags:
- logical-independence
- exchangeability
- prior
- sampling
- binomial-prior
title: Conservation of Logical Independence
understanding: 0
---

## Definition
If the members of a population are **logically independent in the prior** — $P(R_1 R_2 \mid I)=P(R_1\mid I)P(R_2\mid I)$ — then under suitable conditions that independence is *preserved in the posterior*, so observing some members tells you nothing about the unobserved ones. Jaynes (Ch. 6) derives this as the "weird" property of the **binomial prior**: if an urn is filled so that each ball independently has probability $g$ of being red, then the posterior estimate of the fraction of red among the *unsampled* balls is exactly the prior estimate $g$, *independent of the data* — even after sampling 99% of the population you are "no wiser about the remaining 1%." Sampling is futile unless you sample essentially the whole population.

### Mechanism
The binomial/independence prior is "so loose that it destroys the logical link between different members of the population." Knowing one ball is red gives no information about any other, because the filling mechanism made them independent; Bayes' theorem cannot manufacture a link the prior threw away. This contrasts sharply with the uniform prior on $R$, under which the data *do* inform the unsampled fraction (estimate $(r+1)/(n+2)$ depends on the data). The lesson is general: it is the *prior correlation structure* among population members — not the sampling distribution — that determines whether sampling is informative about the rest of the population.

### Conjecture
Jaynes raises the converse as an open line of thought (Exercise 6.4): does the *appearance* of a binomial sampling distribution already imply logical independence of the separate events? Connects to de Finetti-style exchangeability: independence-in-prior is the degenerate (non-exchangeable-learning) extreme.

## Reading Path
- [[jaynes-probability-ch06]] — binomial prior nullifies the data; §6.5 and Exercise 6.4

## Connections
- [[exchangeability]] — contrasts-with: exchangeable priors let data inform beliefs about unsampled members; the independence (binomial) prior is the extreme where sampling carries no such information.
- [[bayesian-inference]] — instantiates: a concrete consequence of applying Bayes' theorem with an independence-structured prior.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]