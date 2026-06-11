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
- machine-learning
- semi-supervised-learning
- deep-learning
id: pkis:technique:consistency-regularization
instantiates:
- semi-supervised-learning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch19
tags:
- semi-supervised
- virtual-adversarial-training
- smoothness
- augmentation
- perturbation
title: Consistency Regularization
understanding: 0
uses:
- data-augmentation
- kl-divergence
- adversarial-examples
---

## Definition
Consistency regularization penalises the model for producing different outputs on a datapoint $x$ and its stochastic perturbation $x'\sim q(x'|x)$. For a semi-supervised batch of labeled $(x_i,y_i)$ and unlabeled $x_j$ examples:
$$L(\theta) = -\sum_{i=1}^M \log p_\theta(y=y_i|x_i) + \lambda\sum_{j=1}^N \|p_\theta(y|x_j)-p_\theta(y|x'_j)\|^2$$
The unlabeled loss can also use KL divergence $D_{KL}(p_\theta(y|x)\|p_\theta(y|x'))$, which avoids gradient saturation when predictions are highly discordant. *Virtual adversarial training* (VAT) finds the worst-case perturbation
$$\delta \approx \arg\max_\delta D_{KL}(p_\theta(y|x)\|p_\theta(y|x+\delta))$$
analytically via a single power-iteration step.

### Why it matters
Consistency regularization formalises the **smoothness assumption**: a good classifier should not change its output in regions of high data density. Combined with strong augmentations or adversarial perturbations it achieves state-of-the-art SSL results. Stochastic weight averaging (SWA) further exploits the resulting geometric properties of the loss landscape.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[adversarial-examples]] — uses: Virtual adversarial training finds the input perturbation maximally changing the model output.
- [[kl-divergence]] — uses: VAT uses KL divergence to find worst-case adversarial perturbation.
- [[data-augmentation]] — uses
- [[semi-supervised-learning]] — instantiates
[To be populated during integration]