---
aliases: []
also_type: []
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
- deep-learning
- ensemble-methods
- uncertainty-quantification
id: pkis:technique:deep-ensembles
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch17
tags:
- multimodal-posterior
- diversity
- calibration
- OOD-robustness
title: Deep Ensembles
understanding: 0
---

## Definition
$$p(\theta|D) \approx \frac{1}{M}\sum_{m=1}^{M} \delta(\theta - \hat{\theta}_m)$$

Deep ensembles train $M$ independent neural networks from different random initialisations (and optionally different hyperparameters or architectures), then average their predictive distributions at test time.

### Why it matters
Because DNN loss landscapes are highly multimodal, single-basin inference methods underestimate uncertainty. Deep ensembles sample *across* basins of attraction, capturing functional diversity that within-basin methods miss. Empirically they outperform MC dropout and often match or exceed more principled Bayesian methods on uncertainty calibration and robustness to dataset shift.

### Relationship to Bayesian inference
In the large-sample limit, standard BMA concentrates on the single best model. Deep ensembles instead maintain $M$ equally weighted components—this is *model ensembling*, not BMA, and can strictly enlarge the expressive power of the posterior predictive.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]