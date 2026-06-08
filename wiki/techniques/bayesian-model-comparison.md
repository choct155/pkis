---
aliases: []
also_type: []
applies:
- evidence-framework
- occams-razor
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- hypothesis-testing
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:technique:bayesian-model-comparison
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch03
tags:
- posterior-odds
- bayes-factor
- evidence
- hypothesis-comparison
- likelihood-ratio
title: Bayesian Model Comparison
understanding: 0
uses:
- marginal-likelihood
- likelihood-ratio-evidence
---

## Definition
Comparing competing models by applying Bayes' theorem at the level of hypotheses rather than parameters. For models $H_1, H_0$ the posterior odds factor into a prior odds times the evidence ratio:
$$\frac{P(H_1\mid D)}{P(H_0\mid D)} = \frac{P(D\mid H_1)}{P(D\mid H_0)} \cdot \frac{P(H_1)}{P(H_0)}.$$
The data-dependent factor $P(D\mid H_1)/P(D\mid H_0)$ is the ratio of marginal likelihoods (the **Bayes factor**); for a parameter-free model the evidence is just its likelihood.

### Built-in Occam's razor
Because each model's evidence is its likelihood averaged over its prior, an over-flexible model dilutes its predictions and is penalized automatically — no explicit complexity term is added by hand.

### Why it matters
It replaces orthodox null-hypothesis testing with a single coherent quantity. MacKay uses it to defuse the Belgian-euro coin claim: the p-value of 7% suggests bias, but the Bayes factor gives at most ~2.3:1 either way. 'The p-values and significance levels of classical statistics should be treated with extreme caution.'

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[occams-razor]] — applies: Ranking by evidence is the mechanism by which Bayesian model comparison embodies Occam's razor.
- [[evidence-framework]] — applies: Bayesian model comparison is the level-2 inference step of the evidence framework.
- [[hypothesis-testing]] — contrasts-with: Bayes factors / posterior odds replace p-values and significance levels
- [[likelihood-ratio-evidence]] — uses: the Bayes factor is the likelihood ratio at the model level
- [[marginal-likelihood]] — uses: posterior odds are formed from the ratio of model evidences (Bayes factor)
[To be populated during integration]

## Minimum Description Length: the coding view
A complementary view replaces probabilities by **message lengths** in bits, via $P(x)=2^{-L(x)}$, i.e. $L(x)=-\log_2 P(x)$. The **MDL principle** (Wallace & Boulton, 1968) prefers the model that communicates the data in the fewest bits. A two-part message states the model and then the data within it, $L(D,H)=L(H)+L(D\mid H)$, which maps onto $-\log P(H\mid D)+\text{const}$ — so MDL and Bayesian model comparison are formally interchangeable.

The data block divides into a *parameter block* and a *residual block*: few parameters give a short parameter block but long residuals, while more parameters lengthen the parameter block and shorten the residuals, with an optimum complexity minimizing the sum. The precision to which parameters are sent has a non-trivial optimum (Wallace & Freeman, 1987), closely tied to the posterior error bars $A^{-1}$; remarkably, the optimal parameter message length is virtually identical to the log of the [[occam-factor]]. MacKay notes MDL offers no practical advantage over the direct probabilistic approach but is a valuable pedagogical and prior-eliciting device. The 'bits-back' argument (Hinton & van Camp, 1993) recovers the exact description length $-\log P(D\mid H)$ by crediting back the random bits used to sample parameters from the posterior.