---
id: "pkis:source:abdelkader-distribution-relationships-2010"
aliases: []
title: "Probability Distribution Relationships"
authors: "Y.H. Abdelkader, Z.A. Al-Marzouq"
year: 2010
type: paper
domain: [bayesian-stats]
tags: [probability-theory, statistics]
source_url: ""
drive_id: "1FLPCjZ_vkOJtCXqfjP4BClJ_CL1hx3-Q"
drive_path: "PKIS/sources/papers/Probability Distribution Relationships - Abdelkader, Al-Marzouq.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[probability-distribution-relationships]]", "[[limiting-distributions]]", "[[inverse-transform-sampling]]"]
---

## Summary

Published in STATISTICA (2010), this short paper by Abdelkader and Al-Marzouq presents four diagrammatic networks summarizing transformation and limiting relationships among the most common probability distributions. The authors observe that virtually all probability distributions are related through either transformation or limiting/asymptotic operations, and that making these relationships explicit is pedagogically and practically useful — for example, knowing how to derive an Erlang deviate as a sum of exponentials directly supports simulation via the inverse transform.

The paper identifies three primary transformation techniques: the CDF technique, the transformation (Jacobian) technique, and the moment generating function technique. These can be applied to linear transformations (yielding, e.g., the additive stability of normals, gammas, and Poissons) or nonlinear transformations (yielding, e.g., log-normal × beta = log-normal). The four diagrams cover: (1) continuous distribution relationships; (2) discrete distributions and their continuous analogues (all rooted in Bernoulli trials); (3) limiting/asymptotic relationships (binomial→Poisson, binomial→Normal via CLT, gamma→Normal); and (4) the Balakrishnan skew-normal density SNB_n(λ) and its connections to standard normal, Cauchy, and Student's t.

An appendix provides concise reference PDFs for ~25 continuous and ~12 discrete distributions. The paper does not prove the relationships but functions as a navigational reference across the probability distribution ecosystem.

## Key Knowledge Objects

- [[probability-distribution-relationships]] (concept, high) — the structured network of transformation and limiting connections among common probability distributions
- [[limiting-distributions]] (concept, high) — asymptotic distributions arising when parameters in one distribution approach a limit, e.g., Binomial(n,p)→Poisson(np) as n→∞, p→0
- [[inverse-transform-sampling]] (technique, high) — generating random variates from a distribution F by computing F^{-1}(U) where U~Uniform(0,1); requires a tractable closed-form inverse CDF
- [[moment-generating-functions]] (technique, moderate — could be concept) — characterizing a distribution via E[e^{tX}]; used as a transformation technique to derive distribution of sums and functions of random variables
- [[balakrishnan-skew-normal]] (concept, moderate — could be result) — a generalized skew-normal family SNB_n(λ) introduced by Sharafi & Behboodian (2008), containing the standard skew-normal (n=1) as special case

## Key Extractions

1. **Two classes of relationships**: "The relationships among the probability distributions could be one of the two classifications: the transformations and limiting distributions."

2. **Additive stability examples**: Normal, gamma, chi-square, Cauchy, Poisson, binomial, and negative binomial are all stable under summation (with possibly different parameters); the sum of exponentials gives Erlang; sum of geometrics gives negative binomial; sum of Bernoullis gives binomial.

3. **Inverse transform recipe for simulation**: "to generate an Erlang deviate we only need the sum m exponential deviates each with expected value 1/m. Therefore, the Erlang variate x is expressed as x = Σ y_i = -Σ (1/θ) ln U_i."

4. **Balakrishnan skew-normal**: SNB_n(λ) has density f(x;λ) = c_n(λ)·ϕ(x)·Φ^n(λx); for n=1, c_1(λ)=2 and the distribution reduces to the standard skew-normal SN(λ).

5. **Root distributions**: "Bernoulli and uniform distributions form the bases to all distributions in discrete and continuous case, respectively." The uniform is the generator for all continuous distributions via inverse transform; Bernoulli via Bernoulli trials generates the discrete family.

## Connection Candidates

- [[gaussian-distribution]] — used-by (concept→concept): the normal distribution is central to limiting theory (CLT, Bernstein-von Mises) and appears in limiting relationships with chi-square, t, F distributions
- [[probability-theory]] — uses: provides the formal framework within which all transformation and limiting relationships are derived
- [[mcmc]] — uses: understanding distribution relationships is foundational for constructing MCMC proposal distributions and understanding stationary distributions

## Awaiting Classification

- **moment-generating-functions** — candidate types: technique or concept
  - Case for technique: it's a procedure applied to derive distribution of sums/functions
  - Case for concept: the MGF is also a mathematical object (the Laplace transform of the PDF) with its own definition
  - What makes this hard: MGFs play both a definitional and computational role depending on context
