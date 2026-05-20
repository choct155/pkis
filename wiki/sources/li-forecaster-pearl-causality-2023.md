---
title: "A Forecaster's Review of Judea Pearl's Causality: Models, Reasoning and Inference, Second Edition"
authors: "Feng Li"
year: 2023
type: paper
domain: [causal-analysis, forecasting, bayesian-stats]
tags: [causality, dag, do-calculus, counterfactuals, forecasting, bayesian-networks, time-series, back-door-criterion]
source_url: "https://arxiv.org/abs/2308.05451"
drive_id: "1r0KXuAEqbvL1Z11HmMmt-Dcyw4PlB1uM"
drive_path: "PKIS/sources/papers/A Forecaster's Review of Judea Pearl's Causality.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[structural-causal-models]]", "[[directed-graphical-models]]", "[[do-calculus]]", "[[counterfactuals]]", "[[confounding]]"]
---

## Summary

Feng Li's five-page arXiv preprint reviews the second edition of Pearl's *Causality* (2009) from the standpoint of a practicing forecaster. The review is notable for being — by the author's own observation — the only review of Pearl's book from a forecasting perspective despite Pearl collecting reviews across many disciplines. Li provides a chapter-by-chapter summary of the second edition, then illustrates Pearl's core machinery (DAGs, do-calculus, back-door criterion, counterfactuals) through a concrete retail sales forecasting scenario from the M5 competition.

The paper's central contribution is bridging Pearl's causal framework to time-series forecasting practice. Li argues that forecasters traditionally had difficulty incorporating causality analysis, but modern data availability (as exemplified by the M5 competition dataset with rich external variables) makes it tractable. The retail example walks through constructing a DAG with store size, location, promotions, and sales; applying the do-operator for interventions; using the back-door criterion to identify valid adjustment sets; and estimating counterfactual outcomes to evaluate policy effects. The discussion section candidly identifies remaining challenges: causal inference requires more data than traditional forecasting; graphical models can be computationally intensive; the faithfulness assumption and no-unmeasured-confounders assumption may not hold in practice; and Pearl's framework may not directly accommodate modern ML forecasting architectures.

Li also recommends the CausalNex Python library as a practical companion for Bayesian network-based causal modeling and inference in time-series settings.

## Key Knowledge Objects

- [[structural-causal-models]] (framework, high) — Pearl's SCM framework (DAGs + structural equations) is the central subject of the reviewed book and the analytical foundation of the forecasting illustration
- [[do-calculus]] (technique, high) — the do-operator is applied to the retail sales example to formalize interventions on store size; back-door criterion identifies valid adjustment sets
- [[directed-graphical-models]] (framework, high) — DAGs serve as the primary representational tool for causal structures in both the book review and the forecasting illustration
- [[counterfactuals]] (concept, high) — counterfactual reasoning is used to evaluate the causal effect of store-size interventions by comparing factual versus hypothetical sales outcomes
- [[confounding]] (concept, high) — the back-door criterion is presented as the tool for controlling confounding bias in causal estimation from observational data
- [[bayesian-networks]] (framework, high) — the book's causal networks are discussed as a class of DAG-based Bayesian networks extended with structural equations; CausalNex is cited as a practical implementation
- back-door-criterion (low — technique or result?) — the identification criterion for valid adjustment sets; it is both a procedural test (technique) and a mathematical theorem (result)

## Key Extractions

1. **Forecasting gap in Pearl literature:** The author notes that Pearl collected reviews of *Causality* across many disciplines, but no review from a forecasting perspective existed — motivating this paper as a bridge between the causal inference and forecasting communities.

2. **M5 competition as causal template:** The M5 hierarchical retail sales competition dataset (Makridakis et al. 2022) is used as the running example; the paper argues that datasets like M5 — which include external variables (store attributes, promotions, economic indicators) — make the causal DAG construction feasible where it historically was not.

3. **Back-door criterion in practice:** The back-door path from store size to sales through "promotional activities" is used to illustrate the criterion: a valid adjustment set must block all such paths without including post-treatment variables or descendants of the intervention.

4. **Data requirements:** Causal inference "requires more data than traditional forecasting methods" because it must identify causal relationships among multiple variables rather than just predict from a few series. This is a concrete limitation the review flags for practitioners.

5. **Computational challenges remain:** Building and analyzing graphical models and DAGs is "computationally intensive," and do-calculus algorithms "may require specialized software" — acknowledging that adoption barriers for forecasters remain, even with tools like CausalNex.

6. **Causal ML integration needed:** Li references Schölkopf (2022) and Kaddour et al. (2022) as evidence that the field is moving toward hybrid causal + ML approaches, but notes that the standard Pearl framework "may not be directly applicable" to modern deep learning forecasting architectures.

## Connection Candidates

- [[structural-causal-models]] — uses: the review's entire forecasting illustration is built on SCM machinery; this source adds a forecasting-domain reading path to the SCM node
- [[do-calculus]] — uses: the do-operator is applied in the retail example; this source connects do-calculus explicitly to the forecasting literature for the first time in the wiki
- [[directed-graphical-models]] — uses: DAGs are the primary representation; the paper situates DGMs within the practical constraints of time-series forecasting (data availability, confounding identification)
- [[counterfactuals]] — uses: counterfactual analysis is positioned as the mechanism for evaluating forecast-relevant interventions (what would sales have been under different store configurations?)
- [[confounding]] — uses: back-door criterion controls confounding; the review emphasizes this as the forecaster's key operational takeaway from Pearl's framework
- [[state-space-models]] — contrasts-with: implicit contrast — Pearl's static DAG framework does not naturally accommodate temporal dynamics, which is where state-space models excel; the review's discussion of "sequences of time-varying actions" gestures at this gap
- [[bayesian-networks]] — specializes: Pearl's causal networks are Bayesian networks augmented with structural equations; the review and the CausalNex recommendation reinforce this connection

## Awaiting Classification

- **back-door-criterion** — candidate types: technique or result
  - Case for technique: it is a procedure — check whether a set of variables satisfies three conditions relative to a DAG — applied to identify valid adjustment sets
  - Case for result: it is a mathematical theorem establishing sufficient conditions for non-parametric identification of causal effects from observational data
  - What makes this hard: it has a procedural use (technique: apply to identify adjustment sets) and a theoretical status (result: proven sufficient condition); both are load-bearing aspects of how the concept is used in the literature
