---
title: "Regression Discontinuity"
knowledge_type: technique
also_type: []
domain: [causal-analysis]
tags: [rdd, sharp-rdd, fuzzy-rdd, running-variable, threshold, local-linear-regression, bandwidth, mccrary-test, natural-experiment]
related_concepts: [[[identification-strategy]], [[local-average-treatment-effect]], [[instrumental-variables]], [[potential-outcomes-framework]]]
sources: [[[cunningham-causal-inference-mixtape]]]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Regression discontinuity (RDD) identifies causal effects by exploiting a discontinuous jump in treatment assignment at a known threshold of a running variable; sharp RDD (deterministic assignment) identifies the ATE at the threshold, fuzzy RDD (probabilistic jump) identifies LATE via an IV-like first stage — validity requires continuity of potential outcomes at the threshold and no manipulation of the running variable.

## Reading Path
- [[cunningham-causal-inference-mixtape-ch07]] (unread) — primary treatment: sharp vs. fuzzy RDD, local linear regression, bandwidth selection, McCrary density test, Angrist-Lavy and Card et al. applications
