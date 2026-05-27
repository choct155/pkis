---
id: "pkis:concept:stochastic-discount-factor"
aliases: []
title: "Stochastic Discount Factor"
knowledge_type: concept
also_type: []
domain: [macroeconomics, bayesian-stats]
tags: [asset-pricing, pricing-kernel, sdf, no-arbitrage, euler-equation, risk-neutral-measure, dsge, epstein-zin]
related_concepts: []
sources:
  - "[[binsbergen-term-structure-dsge-2011]]"
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

The random variable M_{t+1} (also called the pricing kernel) such that the price of any asset today equals the expectation of M_{t+1} times the asset's payoff next period; under no-arbitrage, a positive SDF exists and is unique in complete markets, and in a representative-agent equilibrium model it equals the marginal rate of substitution between consumption today and consumption tomorrow, modified by the preference structure (e.g., the value-function ratio under Epstein-Zin preferences).

## Reading Path
- [[binsbergen-term-structure-dsge-2011]] (unread) — derives the SDF explicitly from the Epstein-Zin household's optimality conditions; uses it to price nominal bonds at all maturities recursively via the bond Euler equation; shows how the SDF couples the productivity shock and the inflation process to generate the term structure
