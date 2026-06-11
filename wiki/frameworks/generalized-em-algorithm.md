---
aliases: []
also_type: []
analogous-to:
- coordinate-ascent-vi
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
- optimisation
extends:
- em-algorithm
id: pkis:framework:generalized-em-algorithm
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch09
tags:
- EM
- ECM
- incremental-EM
- online-learning
- convergence
title: Generalized EM (GEM) Algorithm
understanding: 0
uses:
- em-monotone-likelihood-increase
---

## Definition
The **generalised EM (GEM)** algorithm relaxes the M step of standard EM: instead of finding $\boldsymbol{\theta}^{\text{new}}=\arg\max_{\boldsymbol{\theta}}\mathcal{L}(q,\boldsymbol{\theta})$, it requires only that $\mathcal{L}(q,\boldsymbol{\theta}^{\text{new}})\geq\mathcal{L}(q,\boldsymbol{\theta}^{\text{old}})$, i.e., the lower bound is *increased* rather than maximised. Because $\mathrm{KL}(q\|p)\geq 0$, the incomplete-data log likelihood is still guaranteed to increase at each cycle.

Two prominent instantiations:
- **Expectation–Conditional Maximisation (ECM)**: the parameter vector $\boldsymbol{\theta}$ is partitioned into groups; each M step alternates constrained maximisations over one group at a time.
- **Incremental / online EM**: responsibilities are recomputed for a single data point per cycle and sufficient statistics are updated incrementally (e.g., $\boldsymbol{\mu}_k^{\text{new}}=\boldsymbol{\mu}_k^{\text{old}}+\frac{\gamma^{\text{new}}-\gamma^{\text{old}}}{N_k^{\text{new}}}(\mathbf{x}_m-\boldsymbol{\mu}_k^{\text{old}})$), achieving $O(1)$ cost per step.

### Why it matters
GEM is essential when the M step has no closed-form solution (e.g., non-exponential-family components or constrained covariance structures). The incremental variant can converge faster in practice than batch EM and connects EM to online stochastic optimisation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[coordinate-ascent-vi]] — analogous-to
- [[em-monotone-likelihood-increase]] — uses
- [[em-algorithm]] — extends
[To be populated during integration]