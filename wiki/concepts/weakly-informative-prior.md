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
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:concept:weakly-informative-prior
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch02
tags:
- prior
- regularization
- applied-bayes
title: Weakly Informative Prior
understanding: 0
---

## Definition
A **weakly informative prior** is a *proper* prior deliberately set up so that the information it carries is weaker than the actual prior knowledge available — enough to *regularize* the posterior (keep it within reasonable bounds) without attempting to encode one's full scientific knowledge.

It occupies the middle ground between a noninformative prior (which tries to model complete ignorance, often becoming improper) and a strongly informative prior (which fully encodes substantive beliefs). Two complementary construction strategies:

- **Start noninformative and add constraint:** begin with a flat prior, then add just enough information to rule out absurd values. E.g., for the sex-ratio problem, replace $U(0,1)$ with a prior concentrated between 0.4 and 0.6, such as $N(0.5,0.1^2)$ or — to keep conjugacy — $\mathrm{Beta}(20,20)$.
- **Start strong and broaden:** begin with a highly informative prior and widen it to acknowledge uncertainty in those beliefs and their transfer to new data.

A typical scale heuristic: for regression on the log or logit scale with standardized predictors, effects larger than ~10 are essentially impossible (a shift of 10 on the logit scale moves a probability from 0.01 to 0.99), so a $N(0, A^2)$ prior with moderate $A$ is weakly informative.

## Intuition
The goal is not to model ignorance but to install "soft guardrails." A purportedly noninformative $U(0,1)$ prior on a rare-disease probability is actually *too strong* — with weak data ($y=0$ out of $n=100$) it badly overestimates the rate; a weakly informative prior pulls the posterior into the plausible low range without committing to a precise value. Conversely, weak priors should not be tightened merely because the posterior is vague; sometimes the honest answer is to report the uncertainty.

### Why it matters
Weakly informative priors are the default recommendation in modern applied Bayesian workflow (Stan, Bambi, brms): they stabilize estimation, prevent pathological posteriors in sparse-data or separation problems, and remain robust because in data-rich settings the likelihood dominates anyway. They also support a *fairness/symmetry* role — e.g., a prior symmetric about zero for a treatment effect avoids pre-loading the analysis toward an experimenter's hypothesis.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]