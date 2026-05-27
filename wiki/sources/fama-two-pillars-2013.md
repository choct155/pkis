---
id: "pkis:source:fama-two-pillars-2013"
aliases: []
title: "Two Pillars of Asset Pricing"
authors: "Eugene F. Fama"
year: 2013
type: paper
domain: [asset-pricing]
tags: [efficient-markets, capm, factor-models, event-studies, empirical-finance]
source_url: ""
drive_id: "1Ryu_3t-QOQvXWLDvYWTzt6_xorpP78cT"
drive_path: "PKIS/sources/papers/Two Pillars of Asset Pricing - Fama.pdf"
status: unread
date_added: 2026-05-20
concepts: [efficient-markets-hypothesis, joint-hypothesis-problem, capm, fama-french-three-factor-model, event-study-methodology, value-premium, size-effect]
---

## Summary

This is Fama's 2013 Nobel Prize lecture covering the two "pillars" of asset pricing: the efficient markets hypothesis (EMH) and empirical asset pricing models. Fama traces the development of EMH from early random walk tests through event studies and predictive regressions to the modern behavioral finance debate. A central methodological contribution is the formalization of the **joint hypothesis problem**: market efficiency can only be tested jointly with a model of market equilibrium, so test rejections are ambiguous between market inefficiency and a misspecified asset pricing model.

The second pillar covers the development of empirical asset pricing from the CAPM through the identification of anomalies (size, value, momentum) to the Fama-French three-factor model (1993). The three-factor model adds SMB (small-minus-big) and HML (high-minus-low book-to-market) factors to the market factor, motivated empirically as a response to the failure of the CAPM to explain cross-sectional return patterns. Fama interprets these factors through Merton's ICAPM lens — as proxies for unspecified state variable risks — while acknowledging the behavioral alternative (overreaction/correction). The lecture surveys evidence on time-varying expected returns (dividend yields, default spreads, term spreads), the "bubbles" debate, and active vs. passive fund management, consistently defending rational-risk interpretations over behavioral explanations.

## Key Knowledge Objects

- [[efficient-markets-hypothesis]] (concept, high) — markets fully incorporate available information into prices; above-average returns require above-average risk
- [[joint-hypothesis-problem]] (concept, high) — tests of market efficiency are always joint tests of efficiency and the assumed asset pricing model
- [[fama-french-three-factor-model]] (framework, high) — empirical asset pricing model adding size and value factors to the CAPM market factor
- [[event-study-methodology]] (technique, high) — method for aggregating price responses to corporate events using event time and cumulative average residuals
- [[value-premium]] (result, high) — high book-to-market stocks earn higher average returns than low book-to-market stocks
- [[size-effect]] (result, high) — small-capitalization stocks earn higher average returns than large-capitalization stocks, unexplained by CAPM beta
- [[fama-macbeth-procedure]] (technique, high) — period-by-period cross-section regressions with time-series averaging of slopes to handle residual cross-correlation
- [[capm]] (framework, high) — capital asset pricing model: expected returns linear in market beta

## Key Extractions

1. "We can't test whether the market does what it is supposed to do unless we specify what it is supposed to do. In other words, we need an asset pricing model." The joint hypothesis problem is that test rejections cannot distinguish market inefficiency from a bad equilibrium model. (p. 366)

2. Formal statement of efficiency: f(P_{t+1}|Θ_tm) = f(P_{t+1}|Θ_t) — the distribution of payoffs implied by market prices equals that from all available information. This is not testable without an equilibrium model. (pp. 365–366)

3. The FFJR (1969) event study on stock splits introduced cumulative average residuals in event time — a methodology "that has done much to shape the development of the field." (p. 368)

4. "The three-factor model [Fama-French 1993] is an empirical asset pricing model. Standard asset pricing models work forward from assumptions about investor tastes... Empirical asset pricing models work backward. They take as given the patterns in average returns, and propose models to capture them." (p. 381)

5. On "bubbles": "The available research provides no reliable evidence that stock market price declines are ever predictable. Thus, at least as the literature now stands, confident statements about 'bubbles' and what should be done about them are based on beliefs, not reliable evidence." (p. 375)

6. Behavioral finance criticism: "The behavioral literature has not put forth a full blown model for prices and returns that can be tested and potentially rejected — the acid test for any model proposed as a replacement for another model." (p. 378)

## Connection Candidates

- [[efficient-markets-hypothesis]] — grounds: the EMH grounds all tests of asset pricing; this paper is its most authoritative retrospective defense
- [[joint-hypothesis-problem]] — concept: this paper is the definitive exposition of why EMH is always tested jointly with an equilibrium model
- [[identification-strategy]] — concept: the joint hypothesis problem is an identification problem — you cannot separately identify the efficiency component from the model component
- [[capm]] — contrasts-with/extends: the three-factor model extends CAPM by adding size and value factors
- [[value-premium]] — the paper surveys and defends risk-based interpretations of the value premium
- [[structural-causal-models]] — concept: Fama's insistence on an equilibrium model before testing efficiency parallels the identification requirement in causal inference
- [[potential-outcomes-framework]] — concept: the behavioral finance challenge to EMH is implicitly a counterfactual argument about what returns "would have been" under efficiency
