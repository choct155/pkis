---
aliases: []
also_type: []
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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:concept:value-of-information
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch36
tags:
- decision-theory
- experimental-design
- exploration-exploitation
- bayesian-inference
- sequential-decision
title: Value of Information
understanding: 0
---

## Definition
The **value of information** is the increase in expected utility obtained by acquiring data $d$ before acting, net of the cost of acquisition. Because the datum is not yet observed, its value is computed by averaging over all possible outcomes and the actions each would trigger:
$$ \text{VoI} = \Big(\;\mathbb{E}_{d}\big[\max_a \mathcal{E}[U\mid a, d]\big]\Big) - \max_a \mathcal{E}[U\mid a] - c, $$
where $c$ is the cost of the experiment. Information has value only if its outcomes might *change* which action is taken.

### MacKay's prospecting example
Choosing among $N$ mining sites with Gaussian returns $x_n\sim\mathrm{Normal}(\mu_n,\sigma_n^2)$: with no data the optimal action is simply $n_a=\arg\max_n \mu_n$ with expected utility $\max_n\mu_n$. Prospecting at site $n$ yields a noisy datum, shrinking the posterior; the updated mean $\mu_n'$ is itself Gaussian about $\mu_n$ with variance $s^2=\sigma_n^2\,\sigma^2/(\sigma^2+\sigma_n^2)$. The expected gain (vs. the runner-up mean $\mu_1$) is
$$ -c_n + \int_{\mu_1}^{\infty} d\mu_n'\,(\mu_n'-\mu_1)\,\mathrm{Normal}(\mu_n';\mu_n,s^2), $$
worth doing only when this exceeds zero. The integral is large precisely when the data are likely to flip the decision.

### Why it matters
Value of information formalises *exploration vs. exploitation*: prospecting, A/B tests, active learning, and Bayesian optimisation all pay a cost now for posterior sharpening that may improve later choices. When experiments can be iterated with uncertain cost, the exact computation explodes combinatorially — the regime where reinforcement learning supplies approximations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]