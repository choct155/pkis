---
aliases: []
also_type: []
applies:
- occams-razor
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:framework:evidence-framework
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch28
tags:
- model-comparison
- marginal-likelihood
- hierarchical-bayes
- model-selection
- bayesian-inference
title: The Bayesian Evidence Framework (Two Levels of Inference)
understanding: 0
uses:
- marginal-likelihood
---

## Definition
The **evidence framework** organizes data modelling into two nested applications of Bayes' theorem, distinguished by what is being inferred. The same normalizing constant — the *evidence* $P(D\mid H_i)$ — links the two levels: ignored at level one, it becomes the central quantity at level two.

### Level 1 — model fitting
Assuming model $H_i$ is true, infer its parameters $\mathbf{w}$:
$$P(\mathbf{w}\mid D, H_i) = \frac{P(D\mid \mathbf{w}, H_i)\,P(\mathbf{w}\mid H_i)}{P(D\mid H_i)}, \qquad \text{Posterior} = \frac{\text{Likelihood}\times\text{Prior}}{\text{Evidence}}.$$
The denominator is irrelevant here and usually dropped; one summarizes by $\mathbf{w}_{MP}$ and error bars from the posterior curvature.

### Level 2 — model comparison
Infer which model is most plausible:
$$P(H_i\mid D) \propto P(D\mid H_i)\,P(H_i).$$
The data-dependent factor is exactly the evidence that was the level-1 normalizer. With equal model priors, models are *ranked by their evidence*, which automatically embodies Occam's razor.

### Why it matters
The framework dissolves the myth that Bayesian methods merely add subjective priors at level one (where they often barely matter). The distinctive Bayesian contribution is the principled level-two computation, which orthodox best-fit selection cannot perform without ad hoc penalties.

### Scope and caveats
Both levels are inference, not **decision theory**: no loss function is involved, and model *comparison* does not imply model *choice* — ideal predictions marginalize over all models weighted by probability. The global normalizer $P(D)=\sum_i P(D\mid H_i)P(H_i)$ is omitted because the hypothesis space is open-ended: new models may be proposed after the data arrive. Proper priors are essential, since improper priors render evidences and Occam factors meaningless.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[marginal-likelihood]] — uses: The evidence (marginal likelihood) is the quantity linking the framework's two levels of inference.
- [[occams-razor]] — applies: Ranking models by evidence at level 2 automatically enforces Occam's razor without any subjective complexity bias.
[To be populated during integration]