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
id: pkis:concept:expected-utility-theory
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch36
tags:
- decision-theory
- utility
- preferences
- allais-paradox
- rationality
title: Expected Utility Theory
understanding: 0
---

## Definition
A normative model of choice under uncertainty in which a decision-maker, facing actions $a$ that induce a probability distribution $P(x\mid a)$ over world states $x$, picks the action maximising the expectation of a scalar **utility function** $U(x,a)$:
$$ a^* = \arg\max_a\; \mathcal{E}[U\mid a] = \arg\max_a \int d^K x\, U(x,a)\, P(x\mid a). $$
The utility function encodes *all* of the agent's preferences as a single real number per outcome; everything else is computation. A pessimist may equivalently work with a loss $L=-U$ and minimise expected loss.

### The utility function is the hard part
MacKay stresses that the machinery is trivial — the difficulty is choosing $U$. The utility of money, for instance, is notoriously nonlinear: people are risk-averse over gains, so $U(\text{money})$ is concave, not the naive identity. A linear utility makes optimal site-selection ignore variances entirely; only a nonlinear $U$ makes uncertainty matter to the decision.

### Coherence and the Allais paradox
The theory is *normative*: it claims a rational agent should behave *as if* maximising expected utility (von Neumann–Morgenstern axioms). Real preferences often violate this. In the **Allais paradox**, many people prefer a sure \u00a31M to a gamble, yet also prefer a 10% shot at \u00a32.5M over an 11% shot at \u00a31M — a pair of choices provably inconsistent with *any* utility function $U(x)$. Such intransitivities expose the gap between descriptive behaviour and the EU ideal.

### Why it matters
Expected utility is the substrate on which all of Bayesian decision theory rests: posteriors supply $P(x\mid a)$, the utility supplies preferences, and their product-integral collapses the choice to an $\arg\max$. Recognising when human or modelled preferences fail coherence is essential before trusting an EU-optimal recommendation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]