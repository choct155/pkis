---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- bayesian-statistics
- information-theory
id: pkis:result:joint-predictive-evaluation
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch14
tags:
- Bayes-optimality
- sequential-prediction
- epistemic-uncertainty
- evaluation
- KL-divergence
title: Joint Predictive Evaluation via Environment-KL
understanding: 0
---

## Definition
For a learning agent using approximate belief state $Q_T = q(\mathbf{y}\mid\mathbf{x},D_T)$, define the environment-KL metric
$$d_{\mathcal{E},Q}^{\mathrm{KL}} = \mathbb{E}_{P(\mathbf{x},D_T,\mathcal{E})}\bigl[D_{\mathrm{KL}}(P(\mathbf{y}\mid\mathbf{x},\mathcal{E})\|Q(\mathbf{y}\mid\mathbf{x},D_T))\bigr].$$
**Claim:** $d_{\mathcal{E},Q}^{\mathrm{KL}} = d_{B,Q}^{\mathrm{KL}} + I(\mathcal{E};\mathbf{y}\mid D_T,\mathbf{x})$, where $d_{B,Q}^{\mathrm{KL}}$ is the KL to the Bayes-optimal posterior and $I(\mathcal{E};\mathbf{y}\mid D_T,\mathbf{x})$ is a constant w.r.t. the agent. Therefore ranking agents by $d_{\mathcal{E},Q}^{\mathrm{KL}}$ (or equivalently by cross-entropy NLL on held-out environment samples) is equivalent to ranking them by proximity to the Bayes-optimal joint predictor.

### Why it matters
This result justifies evaluating **joint** (multi-step) predictive distributions — not just marginals — as a proxy for Bayesian optimality. It underpins evaluation frameworks like the Neural Testbed and motivates why marginal calibration is insufficient for sequential decision-making.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]