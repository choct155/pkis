---
title: "The Value Premium"
authors: "Eugene F. Fama and Kenneth R. French"
year: 2020
type: paper
domain: [asset-pricing]
tags: [factor-models, value-investing, book-to-market, return-predictability, forecasting-regressions]
source_url: "https://ssrn.com/abstract=3525096"
drive_id: "1sAy5Npbj3fmMysF7dsAleuSHqgCUY57q"
drive_path: "PKIS/sources/papers/The Value Premium.pdf"
status: unread
date_added: 2026-05-20
concepts: [value-premium, book-to-market-ratio, fama-french-three-factor-model, forecasting-regressions, return-predictability]
---

## Summary

Fama and French (2020) revisit the value premium — the excess return of high book-to-market (value) stocks over the value-weight market portfolio — using data from July 1963 through June 2019 (56 years). The paper is motivated by the near-disappearance of value premiums in the second half (1991–2019) of the sample following the original Fama-French (1992, 1993) documentation, and asks whether this decline represents a permanent reduction in expected value premiums or is merely sampling noise.

The central methodological finding is a structural insight about forecasting regressions: the ability to reliably infer that conditional expected value premiums have declined depends critically on the assumption that regression coefficients are constant across periods. Using a univariate regression of excess value portfolio returns on lagged excess book-to-market ratios (BM-BMM), the full-period slopes are more than six standard errors from zero for the three value portfolios, and since BM-BMM declined from 1963–1991 to 1991–2019, the constant-coefficient model implies lower expected premiums in the second half. However, if the coefficients are allowed to change across sub-periods (regression (2)), the coefficient uncertainty expands standard errors by roughly fivefold, eliminating reliable inference. Unconditional tests are equally inconclusive: the largest declines in average premiums (0.31–0.32% per month for big value) are only 1.4 standard errors from zero due to the high volatility of monthly value returns (SD ~3%). The paper concludes that neither average returns nor forecasting regressions can confidently distinguish between a structural decline in expected value premiums and persistence of premiums at lower levels.

## Key Knowledge Objects

- [[value-premium]] (result, high) — value stocks outperform the market; magnitude may have declined post-1991 but statistical evidence is inconclusive
- [[book-to-market-ratio]] (concept, high) — ratio of accounting book equity to market capitalization; primary sorting variable for value/growth classification
- [[forecasting-regressions]] (technique, high) — time-series regressions of returns on lagged predictive variables; paper clarifies that reliable inference from sub-period comparisons requires constant-coefficient assumption
- [[fama-macbeth-procedure]] (technique, moderate) — not the main technique here, but BM-BMM forecasting regressions build on the Fama-French empirical asset pricing program
- [[in-sample-out-of-sample-comparison]] (technique, moderate — could be concept) — the paper's primary analytical device: comparing 1963–1991 in-sample period with 1991–2019 out-of-sample period
- [[structural-stability]] (concept, moderate — could be result) — the question of whether regression coefficients are constant over time; lack of statistical power prevents confident conclusions

## Key Extractions

1. Full-period results: Average monthly premiums over the market are 0.26% (t=2.37) for all value stocks, 0.21% (t=1.81) for big value, and 0.45% (t=3.21) for small value. Premium for growth portfolios is statistically indistinguishable from zero in all periods.

2. Second-half decline: Average value premium for big value falls from 0.36% (t=2.91) in 1963–1991 to 0.05% (t=0.24) in 1991–2019. "But the high volatility of monthly premiums prevents us from rejecting the hypothesis that expected premiums are the same in both halves of the sample."

3. Key structural insight: "Our focus is whether changes in market conditions lead to lower expected premiums in the second half of the sample, so it seems appropriate to allow the regression coefficients in (1) to change from 1963–1991 to 1991–2019. When we use regression (2) to accommodate the changes, noise in the coefficient estimates rules out confident inferences about whether or how much conditional expected premiums change."

4. The t-statistic for the difference between subperiod conditional forecasts from the constant-slope regression (1) equals the t-statistic for the full-period slope — a clean mathematical result showing that inference power comes entirely from slope precision.

5. "Since we can't reject the hypothesis that expected premiums over RM are the same for the two halves of the sample, average return premiums for the full sample are arguably the best evidence on long-run expected premiums."

## Connection Candidates

- [[value-premium]] — result: this paper is the most recent direct examination of the value premium's persistence
- [[fama-french-three-factor-model]] — uses: the value and growth portfolios here are the basis for HML in the three-factor model
- [[identification-strategy]] — concept: the paper's core insight is an identification argument — you cannot distinguish structural change from sampling noise without restrictive assumptions
- [[structural-breaks]] — concept: the question of whether the value premium declined post-1991 is a structural break question; connects to existing PKIS node
- [[forecasting-regressions]] — technique: the paper makes a fundamental methodological point about what forecasting regressions can and cannot identify
- [[bayesian-model-averaging]] — technique: the tension between constant-slope and variable-slope specifications is conceptually related to model uncertainty and averaging
