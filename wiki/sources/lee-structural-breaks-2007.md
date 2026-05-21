---
title: "Forecasting with Structural Breaks: The District of Columbia Before and After the Financial Crisis"
authors: ["Fitzroy Lee"]
year: 2007
type: paper
domain: [time-series, forecasting]
tags: [structural-breaks, parameter-stability, quandt-andrews-test, cusum, revenue-forecasting, local-government]
source_url: ""
drive_id: "1hV12sPF_XsC0XcqyqvEK7m-VtGnZLKMt"
drive_path: "PKIS/sources/papers/lee-structural-breaks-2007.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[structural-breaks]]"]
---

## Summary

A practical applied paper examining structural breaks in DC withholding tax forecasting models, presented at the 100th National Tax Association conference. The paper addresses the central assumption of parameter constancy in statistical forecasting — that model parameters remain stable over the estimation and forecast periods — and tests this assumption for ten alternative model specifications using DC fiscal data from FY1983Q1–FY2007Q3.

The paper applies two structural break testing frameworks: the Quandt-Andrews (QLR) test for a single break at an unknown date (using Andrews 1993 critical values and the Andrews-Ploberger family of tests) and CUSUM analysis for continuous parameter stability. Among ten models tested (four univariate: trend, AR, differenced AR, AR-with-trend; six multivariate), the QLR test finds significant breaks in only two: the trend model and the simple bivariate regression — both of which also show evidence of serial correlation suggesting model misspecification. A key empirical finding is that the simple trend model, despite being flagged for a structural break, produces the best out-of-sample forecast performance (lowest RMSE), while the more complex "well-specified" models perform worse. The paper offers three lessons: (1) structural break testing should be integrated with broader misspecification testing; (2) good specification does not guarantee good forecasting; (3) simpler models may dominate more complex ones.

## Key Knowledge Objects

- [[structural-breaks]] (concept, high) — shifts in the parameter values of a forecasting model due to institutional, policy, or economic regime changes; the central subject of this paper

## Key Extractions

1. **Quandt-Andrews (QLR) test**: Maximizes the Chow test statistic over all possible breakpoints in a trimmed sample (default trimming λ₀=0.15, λ₁=0.85). Unlike the standard Chow test, does not require prior knowledge of the breakdate. Andrews (1993) critical values are larger than chi-square critical values because the breakdate is now a nuisance parameter.
2. **CUSUM analysis**: Cumulative sum of recursive residuals plotted against 5% significance bands. Movement outside the bands indicates parameter instability. Noted as primarily a test of intercept stability and low-power, but useful as a visual complement to QLR.
3. **Surprising forecast competition result**: Despite the trend model having a detected structural break, it ranks first in RMSE and top-5 in MAPE among 10 competing models. The authors attribute this to either (a) parsimony advantage or (b) the trend model being the most faithful representation of the withholding series, which "is essentially a trend with seasonal variations."
4. **Differencing as robustness**: Citing Clements and Hendry (1999), differencing transforms intercept breaks into blips that structural break tests cannot detect — a feature, not a bug, for forecasting under regime shifts.
5. **Stock-Watson precedent**: Stock and Watson (1996) tested 608 univariate equations for structural breaks in 76 monthly macro series; "a substantial fraction of forecasting relations are unstable (p. 23)."

## Connection Candidates

- [[structural-breaks]] — creates: this paper is a primary applied treatment of structural breaks in forecasting
- [[var-models]] — uses: one of the ten models tested (Model 10) is a single-equation VAR specification with lagged dependent and lagged explanatory variables
- [[model-selection-problem]] — deepens: the forecast competition illustrates that model selection criteria (QLR test results, DW statistics) do not reliably predict forecast performance — a real-world instance of the model selection problem
