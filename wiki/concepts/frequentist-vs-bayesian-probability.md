---
aliases: []
also_type: []
analogous-to:
- physical-vs-epistemic-probability
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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probability-theory
- statistics
- philosophy-of-science
id: pkis:concept:frequentist-vs-bayesian-probability
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- bayesian-inference
related_concepts: []
sources:
- goodfellow-deeplearning-ch03
specializes:
- probability-vs-frequency
tags:
- interpretation
- Bayesian
- frequentist
- epistemology
title: Frequentist vs. Bayesian Probability
understanding: 0
uses:
- probability-theory
---

## Definition
**Frequentist probability** interprets $P(A)$ as the long-run relative frequency of event $A$ in a repeatable experiment. **Bayesian probability** interprets $P(A)$ as a degree of belief or epistemic uncertainty about $A$, applicable even to one-off events.

Both interpretations obey the same Kolmogorov axioms and yield identical computational rules (Bayes' rule, the chain rule, etc.). The difference is philosophical and affects how parameters and hypotheses are treated: frequentists treat parameters as fixed unknowns, Bayesians treat them as random variables with prior distributions.

### Why it matters
The distinction shapes the entire methodology of statistical inference. In deep learning, recognizing that probabilistic models can encode epistemic uncertainty (Bayesian) rather than only aleatory/frequency-based uncertainty is essential for calibration, active learning, and safe deployment.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[probability-vs-frequency]] — specializes
- [[physical-vs-epistemic-probability]] — analogous-to
- [[probability-theory]] — uses
- [[bayesian-inference]] — prerequisite-of
[To be populated during integration]