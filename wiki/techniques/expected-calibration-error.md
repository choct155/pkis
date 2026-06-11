---
aliases: []
also_type: []
applies:
- calibration
- predictive-model
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:technique:expected-calibration-error
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch14
tags:
- calibration
- reliability-diagram
- deep-learning-evaluation
- MCE
title: Expected Calibration Error (ECE) and Reliability Diagram
understanding: 0
uses:
- brier-score
---

## Definition
$$\mathrm{ECE}(f) = \sum_{b=1}^B \frac{|B_b|}{N}\,|\mathrm{acc}(B_b) - \mathrm{conf}(B_b)|$$

ECE partitions predicted confidences into $B$ equally-spaced bins, and computes a sample-weighted average of the absolute gap between empirical accuracy and mean predicted confidence within each bin. Plotting accuracy vs. confidence produces a **reliability diagram**; perfect calibration corresponds to the identity line. The **marginal calibration error (MCE)** extends this to all $C$ classes by averaging class-wise squared calibration gaps.

### Why it matters
ECE is the dominant scalar summary of calibration in modern deep-learning evaluation pipelines. It reveals systematic over-confidence (common in DNNs) that neither accuracy nor NLL directly expose, motivating post-hoc recalibration methods.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[predictive-model]] — applies
- [[brier-score]] — uses
- [[calibration]] — applies
[To be populated during integration]