---
title: "Causal Inference: The Mixtape"
authors: "Scott Cunningham"
year: 2021
type: book
domain: [causal-analysis, bayesian-stats]
tags: [causal-inference, potential-outcomes, dag, identification, econometrics, program-evaluation, observational-studies]
source_url: "https://mixtape.scunning.com"
drive_id: "1OAZSDDbVNCPumzvalpKXVcPBSkUB8PZ2"
drive_path: "PKIS/sources/books/cunningham-causal-inference-mixtape.pdf"
isbn: "978-0-300-25168-5"
toc_source: "manual"
status: unread
date_added: 2026-05-20
concepts: [[[potential-outcomes-framework]], [[average-treatment-effect]], [[selection-bias]], [[regression-discontinuity]], [[instrumental-variables]], [[difference-in-differences]], [[synthetic-control]], [[matching-estimators]], [[propensity-score]], [[parallel-trends]], [[local-average-treatment-effect]], [[collider-bias]], [[identification-strategy]], [[counterfactuals]], [[confounding]], [[directed-graphical-models]], [[structural-causal-models]]]
---

## Summary

*Causal Inference: The Mixtape* is an applied econometrics textbook covering the major identification strategies used to estimate causal effects in observational data. Cunningham wrote the book to bridge the gap between theoretical causal inference frameworks and practical social science research, combining intuition-first exposition with replications of canonical empirical studies in Stata. The book integrates two distinct but complementary traditions: the potential outcomes (Rubin) framework, which formalizes causal effects as comparisons of counterfactual outcomes under treatment and control; and directed acyclical graphs (DAGs, Pearl), which provide a graphical language for reasoning about identification and confounding.

The book progresses from probability and regression review through increasingly sophisticated identification strategies. It covers: DAGs and backdoor/front-door identification (Pearl); the potential outcomes model and SUTVA; matching and propensity score methods; regression discontinuity (sharp and fuzzy); instrumental variables with LATE interpretation; panel data and fixed effects; difference-in-differences with parallel trends; and synthetic control. Each chapter is anchored by a classic empirical application — Krueger (1999) class size experiments, Angrist and Lavy (1999) on Maimonides' Rule, Card and Krueger on minimum wage, and Abadie et al. on California tobacco laws — making the identification logic concrete and practice-ready.

A distinctive feature is Cunningham's use of hip-hop epigraphs throughout, reinforcing the book's ethos: causal inference is for practitioners who care about getting the right answer, not for mathematical formalism as an end in itself. The published version (Yale University Press, 2021) is an expanded revision of the freely distributed v1.7 preprint. The drive file is v1.7 and contains the full treatment through the DAGs chapter with rich detail, with remaining chapters covered at summary level.

## Key Knowledge Objects

- [[potential-outcomes-framework]] (framework, high) — Rubin's model formalizing causal effects as Y(1)−Y(0); the fundamental problem of causal inference
- [[average-treatment-effect]] (concept, high) — ATE, ATT, ATU: the estimands of causal inference; defined over different subpopulations
- [[local-average-treatment-effect]] (concept, high) — LATE: causal effect identified by IV for compliers only; Angrist-Imbens-Rubin interpretation
- [[selection-bias]] (concept, high) — Non-random treatment assignment creating systematic differences between treated and control groups
- [[identification-strategy]] (concept, high) — The research design argument linking an estimator to a causal quantity under stated assumptions
- [[regression-discontinuity]] (technique, high) — Identification using discontinuous jumps in treatment assignment at a threshold of a running variable
- [[instrumental-variables]] (technique, high) — Identification using exogenous variation that affects treatment but not outcome directly
- [[difference-in-differences]] (technique, high) — Identification via pre-post within-group change minus pre-post control change; requires parallel trends
- [[synthetic-control]] (technique, high) — Comparative case studies using a weighted combination of controls to construct a counterfactual
- [[matching-estimators]] (technique, high) — Conditioning on observed covariates to equate treated and control units and estimate ATT
- [[propensity-score]] (concept, high) — P(D=1|X): sufficient statistic for selection on observables; enables matching without curse of dimensionality
- [[parallel-trends]] (principle, high) — DiD identifying assumption: treated and control would have had the same trend absent treatment
- [[collider-bias]] (concept, high) — Conditioning on a variable that is caused by both treatment and outcome opens spurious paths
- [[omitted-variable-bias]] (concept, high) — Bias from excluding a confounder correlated with both treatment and outcome
- [[sutva]] (principle, moderate — could be concept) — Stable Unit Treatment Value Assumption: no interference between units, one version of treatment
- [[backdoor-criterion]] (concept, moderate — could be technique) — Pearl's graphical condition identifying sufficient adjustment sets for causal identification
- [[counterfactuals]] (concept, existing) — Already in wiki from pearl-causality ingest
- [[confounding]] (concept, existing) — Already in wiki from pearl-causality ingest
- [[directed-graphical-models]] (framework, existing) — Already in wiki
- [[structural-causal-models]] (framework, existing) — Already in wiki

## Key Extractions

1. **Fundamental problem of causal inference**: We can never observe both Y(1) and Y(0) for the same unit simultaneously. "Either you went to college or you didn't. Either you smoked or you didn't." The causal effect for any individual is therefore inherently unobservable; all identification strategies recover average effects over groups.

2. **Selection bias decomposition**: The naive OLS comparison E[Y|D=1] − E[Y|D=0] = ATE + selection bias. Selection bias equals E[Y(0)|D=1] − E[Y(0)|D=0] — the difference in baseline outcomes between treated and control. Eliminating selection bias is the goal of every identification strategy in the book.

3. **DAG backdoor criterion**: A set Z satisfies the backdoor criterion for (D,Y) if it blocks all backdoor paths from D to Y and contains no descendant of D. When Z satisfies the backdoor criterion, we can identify the causal effect of D on Y by adjusting for Z.

4. **Collider bias**: A collider is a node X on a path where both arrows point *into* X (D→X←Y). Unlike confounders, colliders *block* backdoor paths when uncontrolled. Conditioning on a collider *opens* a previously blocked path, creating spurious correlation — "Berkson's paradox" in epidemiology.

5. **RDD identification**: In a sharp RDD, treatment switches discontinuously at a threshold c of running variable R. Since units just above and below the threshold are similar on observed and unobserved characteristics, the discontinuity in outcomes at c identifies the local average treatment effect for units at the threshold.

6. **IV LATE interpretation**: IV estimates the local average treatment effect (LATE) — the average effect for *compliers* only (units whose treatment status is changed by the instrument). LATE is not the ATE unless treatment effect heterogeneity is zero or all units are compliers.

7. **Synthetic control logic**: The synthetic control method constructs a weighted combination of control units (the "donor pool") that matches the treated unit's pre-treatment outcome trajectory. Post-treatment divergence between the treated unit and its synthetic counterpart estimates the treatment effect, validated via placebo tests on all control units.

## Connection Candidates

- [[structural-causal-models]] — extends: Cunningham introduces Pearl's SCMs as a DAG language for identification; the potential outcomes framework is shown as complementary (both are Level 2 of the Ladder of Causation)
- [[counterfactuals]] — uses: the potential outcomes framework formalizes counterfactuals as Y(1) and Y(0); Cunningham's whole book is about recovering comparisons between them
- [[confounding]] — uses: confounding via back-door paths is the central obstacle; each identification strategy is a solution to confounding under specific assumptions
- [[d-separation]] — uses: backdoor criterion relies on d-separation logic; Cunningham presents a practitioner-accessible subset of Pearl's full calculus
- [[do-calculus]] — specializes: Cunningham's identification strategies are special cases of do-calculus: matching adjusts for Z, IV uses front-door-like structure, RDD exploits discontinuity as natural experiment
- [[lasso]] — contrasts-with: matching/IV/DiD/RDD are design-based causal estimators; lasso is a prediction method that cannot identify causal effects without further assumptions
- [[bias-variance-tradeoff]] — contrasts-with: causal inference prioritizes bias elimination (identification) over variance reduction; the tradeoff is different from prediction
- [[omitted-variable-bias]] (if new node created) — prerequisite-of: understanding OVB is prerequisite for understanding why each strategy works

## Chapters

| Ch | Stub | Title |
|---|---|---|
| 1 | [[cunningham-causal-inference-mixtape-ch01]] | Introduction |
| 2 | [[cunningham-causal-inference-mixtape-ch02]] | Probability Theory and Statistics Review |
| 3 | [[cunningham-causal-inference-mixtape-ch03]] | Properties of Regression |
| 4 | [[cunningham-causal-inference-mixtape-ch04]] | Directed Acyclical Graphs |
| 5 | [[cunningham-causal-inference-mixtape-ch05]] | Potential Outcomes Causal Model |
| 6 | [[cunningham-causal-inference-mixtape-ch06]] | Matching and Subclassification |
| 7 | [[cunningham-causal-inference-mixtape-ch07]] | Regression Discontinuity |
| 8 | [[cunningham-causal-inference-mixtape-ch08]] | Instrumental Variables |
| 9 | [[cunningham-causal-inference-mixtape-ch09]] | Panel Data |
| 10 | [[cunningham-causal-inference-mixtape-ch10]] | Differences-in-Differences |
| 11 | [[cunningham-causal-inference-mixtape-ch11]] | Synthetic Control |
| 12 | [[cunningham-causal-inference-mixtape-ch12]] | Conclusion |

## Awaiting Classification

- **sutva** — candidate types: principle or concept
  - Case for principle: SUTVA is a foundational *assumption* required to use the potential outcomes framework at all — it constrains what the framework can mean, like exchangeability constrains Bayesian inference
  - Case for concept: SUTVA is also a precisely defined *idea* (no interference + single treatment version) that one can reason about, test for violations of, and partially relax
  - What makes this hard: the line between "principle" (guiding constraint on inference) and "concept" (defined idea with properties) is blurry when the object is an untestable identifying assumption

- **backdoor-criterion** — candidate types: concept or technique
  - Case for concept: it is a *defined property* of a set of variables Z relative to a DAG — you check whether Z satisfies it
  - Case for technique: it is also *used as a procedure* — you apply it to choose an adjustment set and then adjust
  - What makes this hard: Pearl defines it as a criterion (concept), but practitioners use it as a recipe (technique)
