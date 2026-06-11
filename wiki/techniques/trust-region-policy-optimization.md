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
- reinforcement-learning
- optimization
extends:
- reinforce
id: pkis:technique:trust-region-policy-optimization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- proximal-policy-optimization
related_concepts: []
sources:
- murphy-pml2-advanced-ch35
tags:
- natural-gradient
- KL-constraint
- monotonic-improvement
- policy-search
title: Trust Region Policy Optimization (TRPO)
understanding: 0
uses:
- natural-gradient
- kl-divergence
- policy-gradient-theorem
- lagrangian-duality
---

## Definition
TRPO finds a new policy $\pi'$ by solving
$$\arg\max_{\pi'}\; L(\pi') \quad\text{s.t.}\quad \mathbb{E}_{p_\pi^\infty(s)}\!\left[D_{\mathrm{KL}}(\pi(s)\|\pi'(s))\right] \leq \delta$$
where $L(\pi') = \frac{1}{1-\gamma}\mathbb{E}_{p_\pi^\infty(s)\,\pi(a|s)}\!\left[\frac{\pi'(a|s)}{\pi(a|s)}A_\pi(s,a)\right]$ is the surrogate objective and $\delta>0$ is the trust-region radius. This is equivalent to natural policy gradient with an adaptive step size.

### Why it matters
TRPO provides a monotonic improvement guarantee: each update provably does not decrease $J(\pi)$ up to higher-order residuals. It overcomes the instability of vanilla policy gradient caused by large parameter updates that destroy previously learned behaviour. TRPO introduced the practical use of conjugate-gradient / Fisher-vector products to solve the constrained optimisation without explicitly forming the Fisher information matrix.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[lagrangian-duality]] — uses
- [[reinforce]] — extends
- [[proximal-policy-optimization]] — prerequisite-of
- [[policy-gradient-theorem]] — uses
- [[kl-divergence]] — uses
- [[natural-gradient]] — uses
[To be populated during integration]