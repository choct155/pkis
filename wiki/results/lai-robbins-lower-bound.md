---
aliases: []
also_type: []
applies:
- multi-armed-bandit
- thompson-sampling
- upper-confidence-bound-algorithm
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
- statistics
- machine learning
- information theory
id: pkis:result:lai-robbins-lower-bound
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch34
tags:
- regret
- lower bound
- bandit
- KL divergence
- information theory
- optimality
title: Lai-Robbins Regret Lower Bound
understanding: 0
uses:
- cumulative-regret
- kl-divergence
---

## Definition
$$\liminf_{T \to \infty} \frac{L_T}{\log T} \geq \sum_{a:\Delta_a > 0} \frac{\Delta_a}{D_{\mathrm{KL}}(p_R(a) \| p_R(a^*))}$$

where $\Delta_a = R(a^*) - R(a)$ is the reward gap and $D_{\mathrm{KL}}$ is the KL divergence between the reward distribution of arm $a$ and that of the optimal arm $a^*$.

Proved by Lai and Robbins (1985), this states that for any consistent policy in a stochastic multi-armed bandit, the cumulative regret must grow at least logarithmically in the time horizon $T$, with a problem-specific constant determined by how hard it is to statistically distinguish sub-optimal arms from the optimal arm.

### Why it matters
Establishes that $O(\log T)$ regret is the best achievable, and that UCB and Thompson sampling are *asymptotically optimal*. It also reveals a fundamental connection between statistical distinguishability (KL divergence) and the cost of exploration.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[upper-confidence-bound-algorithm]] — applies
- [[thompson-sampling]] — applies
- [[multi-armed-bandit]] — applies
- [[kl-divergence]] — uses
- [[cumulative-regret]] — uses
[To be populated during integration]