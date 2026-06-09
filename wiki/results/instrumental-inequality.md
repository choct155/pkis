---
aliases: []
also_type: []
applies:
- instrumental-variables
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
id: pkis:result:instrumental-inequality
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch08
tags:
- instrumental-inequality
- testable-implication
- exogeneity-test
- bells-inequality
- falsifiability
- instrument-validity
title: The Instrumental Inequality
understanding: 0
uses:
- partial-identification-bounds
---

## Definition
The instrumental inequality (Pearl 1995b,c) is the empirically *testable* constraint that the structure Z->X->Y with latent U->X, U->Y (the instrumental-variable / noncompliance model of Figure 8.1) imposes on any observed distribution. Insisting that each upper bound on ACE exceed the corresponding lower bound yields, for binary variables, four inequalities such as P(y0,x0|z0)+P(y1,x0|z1) <= 1 (Eq. 8.21). Generalized to multivalued variables it reads

    max_x  sum_y  max_z P(y, x | z)  <=  1.       (8.22)

It is violated precisely when the instrument Z produces large changes in the response Y while the treatment X is held fixed -- changes too large to be explained by any latent common cause. This gives exogeneity / instrument validity, long thought untestable because it concerns unobservable disturbances U, a partial empirical test: a violation implies at least one model assumption fails (direct Z->Y effect, or loss of exogeneity via Z-U correlation / assignment bias). The test is one-sided -- it can screen out very bad instruments but cannot certify a good one.

Pearl notes a deep analogy to **Bell's inequality** in quantum physics: both delineate correlations that no latent-common-cause model can produce; the instrumental inequality generalizes Bell's to the case where a *direct* causal link X->Y is also permitted. For continuous X the inequality imposes no constraint at all (conjectured by Pearl 1995c, proven by Bonet 2001). Under a *no-contrarian* (no-defier, monotonicity) assumption P(x1|z1,u) >= P(x1|z0,u), the inequalities tighten to (8.24).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[partial-identification-bounds]] — uses: derived by requiring upper bound >= lower bound on ACE
- [[instrumental-variables]] — applies: testable constraint that screens out invalid instruments / violations of exogeneity
[To be populated during integration]