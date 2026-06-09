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
contrasts-with:
- confidence-interval
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:concept:credible-interval
instantiates:
- bayesian-inference
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch06
tags:
- interval-estimation
- posterior
- bayesian
- percentile
- uncertainty-quantification
title: Credible Interval
understanding: 0
uses:
- uncertainty-quantification
---

## Definition
A **credible interval** is an interval $(a,b)$ for an unknown parameter $\theta$ that carries a stated amount of *posterior* probability, e.g. $P(a \le \theta \le b \mid D, I) = 0.90$. Unlike a frequentist confidence interval, the probability statement is a direct, post-data claim about the parameter given the data in hand: it is the natural Bayesian answer to "how accurately do we know $\theta$?". Jaynes (Ch. 6) frames interval estimation as not fundamentally different from point estimation or hypothesis testing: "the hypothesis that a parameter $\theta$ lies in a certain interval $a<\theta<b$ is a compound hypothesis," so interval estimation is automatically a compound-hypothesis test that probability theory as logic carries out from a single posterior calculation.

### Construction
Given the posterior pdf $p(\theta\mid D I)$, one reports either (i) **highest-posterior-density / central** regions stated directly as "$f$ of the posterior probability lies in $(a,b)$" (Jaynes: "90% of the posterior probability is concentrated in the interval $\alpha < n_1 < \beta$"), or (ii) **percentile-based** spans such as the median $\pm$ interquartile span. The percentile/median construction is *reparameterization-invariant*: if $\lambda=\lambda(\theta)$ is monotone, then $\lambda_{q}=\lambda(\theta_q)$ for every percentile $q$, so the interval has the same meaning under any relabeling of the parameter (a property the mean $\pm$ standard deviation interval lacks).

### Mean ± standard deviation as a quick interval
In practice Jaynes most often reports the posterior (mean) $\pm$ (standard deviation) as a combined point-and-interval estimate, e.g. $\langle F\rangle_{\rm est}=p\pm\sqrt{p(1-p)/(n+3)}$ for the urn fraction. When moments fail to exist (heavy tails, improper-prior limits) the median/percentile interval survives where the mean $\pm$ s.d. does not. Chebyshev's inequality $P\ge 1-1/t^2$ bounds the probability mass within $\pm t\sigma$ for any distribution with finite variance.

## Reading Path
- [[jaynes-probability-ch06]] — interval estimation as compound hypothesis testing; percentile invariance; mean ± s.d. worked examples

## Connections
- [[uncertainty-quantification]] — uses
- [[bayesian-inference]] — instantiates
- [[confidence-interval]] — contrasts-with
- [[confidence-interval]] — contrasts-with: a confidence interval has frequency-coverage (pre-data) semantics; a credible interval is a direct posterior-probability (post-data) statement about the parameter.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]