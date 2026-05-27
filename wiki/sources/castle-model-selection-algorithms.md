---
id: "pkis:source:castle-model-selection-algorithms"
aliases: []
title: "How To Pick The Best Regression Equation: A Review And Comparison Of Model Selection Algorithms"
authors: ["Jennifer L. Castle", "Xiaochuan Qin", "W. Robert Reed"]
year: 2009
type: paper
domain: [statistical-learning, bayesian-stats]
tags: [model-selection, information-criteria, regression, variable-selection, general-to-specific, bayesian-model-averaging, monte-carlo]
source_url: ""
drive_id: "1vBpOfyylYf3FzMEcJBrCUcRNll_Og6aO"
drive_path: "PKIS/sources/papers/castle-model-selection-algorithms.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[model-selection-problem]]", "[[information-criteria]]", "[[general-to-specific-modeling]]", "[[model-averaging]]", "[[bias-variance-tradeoff]]", "[[cross-validation]]", "[[regularization]]"]
---

## Summary

This working paper reviews and compares twenty-one model selection algorithms (MSAs) for regression, spanning six broad families: (i) information criteria (AIC, SIC and corrected variants AICc, SICc); (ii) portfolio models that average over subsets of near-optimal models; (iii) general-to-specific algorithms (Autometrics); (iv) forward-stepwise regression; (v) Bayesian Model Averaging; and (vi) inclusion of all variables. The performance measure is unconditional mean-squared error (UMSE) of coefficient estimates — chosen because it decomposes cleanly into bias and variance components and is relevant for policy-analytic use cases where individual coefficient accuracy matters as much as predictive accuracy.

Using Monte Carlo experiments across 360 environments varying in number of relevant variables (K), total candidate variables (L), sample size (N), and non-centrality parameter (ψ, measuring signal-to-noise), the paper demonstrates that MSA performance is primarily governed by each MSA's effective penalty function, operationalized as its gauge (null rejection frequency). MSAs with tight penalty functions perform best when irrelevant variables dominate; MSAs with loose penalties perform best when most candidate variables are relevant. No single MSA dominates in all environments.

When focus is restricted to the practically important case where K/L ≤ 0.5 and ψ ≤ 2 (many irrelevant variables, low signal), the Autometrics general-to-specific algorithm at 1% and variable significance levels outperforms all other MSAs in over 90% of experiments. This result is partially attributable to Autometrics' post-selection bias correction in addition to its penalty function behavior. The results have important implications for applied econometrics and policy research, where automatic variable selection is frequently needed precisely in low signal-to-noise conditions.

## Key Knowledge Objects

- [[information-criteria]] (concept, high) — AIC and SIC as loss-penalized model scoring rules; their asymptotic properties (AIC: efficient, SIC: consistent) and small-sample corrections
- [[general-to-specific-modeling]] (technique, high) — Autometrics: multi-path tree search from general to specific model with bias correction; dominates in low signal/high irrelevant-variable environments
- [[model-averaging]] (technique, high) — Bayesian Model Averaging and portfolio models as alternatives to single-model selection; BMA with log-likelihood weights included
- [[model-selection-problem]] (problem, high) — the paper is a direct treatment of this problem; connects penalty functions to bias-variance tradeoff
- [[bias-variance-tradeoff]] (concept, high) — UMSE decomposes into bias and variance; penalty functions govern this tradeoff across MSAs
- [[regularization]] (concept, high) — penalty functions in IC MSAs are a form of regularization; lasso-type methods are implicit comparators

## Key Extractions

1. **Gauge as a unified penalty proxy**: The gauge (null rejection frequency, i.e., probability of retaining an irrelevant variable) serves as a universal measure of an MSA's effective penalty function regardless of whether the MSA is IC-based, stepwise, or BMA-based. The rank ordering AIC > SIC on gauge corresponds precisely to AIC > SIC on irrelevant-variable performance.

2. **Bias-variance decomposition of MSA performance**: MSAs with larger penalty functions reduce variance (by zero-ing out irrelevant coefficients) at the cost of increased bias (omitting relevant variables). As K increases relative to L, the variance benefit declines and the bias cost dominates, explaining the K-dependent rank reversal between AIC and SIC.

3. **AIC is asymptotically efficient; SIC is consistent**: SIC selects the true DGP with probability approaching 1 as N → ∞ if the true model is in the candidate set. AIC minimizes expected prediction error; it is not consistent but is asymptotically efficient.

4. **Autometrics dominates under practical conditions**: Under K/L ≤ 0.5 and ψ ≤ 2, AUTO_1% performs as well or better than all non-Autometrics MSAs in 93.1% of 58 experiments; AUTO_Variable achieves 91.4%. Their advantage over forward-stepwise methods with identical nominal significance levels is attributed to post-selection bias correction.

5. **Model averaging over all models outperforms selective averaging**: LLWeighted_All (averaging over all 2^L models) generally outperforms LLWeighted_Selected (averaging over only models containing the variable) even though the former produces biased estimates, because the latter has gauge = 100% and therefore high variance.

## Connection Candidates

- [[model-selection-problem]] — grounds: this paper is a systematic empirical investigation of the problem, establishing which approaches work under which conditions
- [[bias-variance-tradeoff]] — extends: applies the bias-variance framework to coefficient estimation in variable-selection contexts, not just prediction error
- [[regularization]] — uses: IC penalty functions are a form of complexity regularization; connects to lasso and ridge as alternative regularizers
- [[lasso]] — contrasts-with: lasso provides continuous coefficient shrinkage while IC MSAs perform hard thresholding; both are forms of penalized regression
- [[cross-validation]] — contrasts-with: CV estimates predictive risk while UMSE targets coefficient accuracy; the two performance criteria can disagree
- [[ensemble-learning]] — contrasts-with: model averaging (portfolio/BMA) is related to ensemble methods but operates at the model-selection level rather than combining predictions from fixed estimators
