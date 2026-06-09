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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:concept:stochastic-dominance
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch16
tags:
- decision-theory
- utility
- cumulative-distribution
- qualitative-reasoning
- multiattribute-utility
title: Stochastic Dominance
understanding: 0
---

## Definition
## Definition
Action $A_1$ **stochastically dominates** $A_2$ on attribute $X$ if, for the induced distributions $p_1,p_2$,
$$ \forall x \quad \int_{-\infty}^{x} p_1(x')\,dx' \le \int_{-\infty}^{x} p_2(x')\,dx', $$
i.e. $A_1$'s cumulative distribution lies everywhere to the right of $A_2$'s. The decisive property: if $A_1$ stochastically dominates $A_2$, then **for every monotonically nondecreasing utility function** $U(x)$ the expected utility of $A_1$ is at least that of $A_2$. Hence a stochastically dominated action can be discarded without knowing the agent's exact $U$ (R&N Section 16.4.2).

### Why it beats comparing means
Stochastic dominance is strictly stronger than comparing expected values: it lets you decide *without* committing to a utility curve. Paradoxically, learning the *exact* value of an attribute (collapsing its distribution to a point) can make the decision harder, because the dominance argument no longer applies and you then need the utility-of-money curve. Strict dominance (dominance on *all* attributes, all outcomes) is a special deterministic case that rarely yields a unique choice; stochastic dominance is the more useful generalization that occurs frequently in real problems.

### Qualitative reasoning
Stochastic dominance often holds for obvious physical reasons (falling 3 mm vs. 3 m onto concrete) and can be propagated through **qualitative probabilistic networks** — algorithms that let a system make rational decisions from monotone qualitative relationships among uncertain variables, using no numeric values at all.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- A core technique within multiattribute utility theory.
- Reasons about cumulative distribution functions of attributes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]