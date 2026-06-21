---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 0
date_created: '2026-06-14'
date_updated: '2026-06-14'
domain:
- knowledge-representation
- bayesian-stats
id: pkis:framework:continuous-hardening-mixture-framework
illustrated-by:
- shimizu-modular-2023
- giglou-llms4ol-2024
- knowledge-infrastructure-explainer
knowledge_type: framework
maturity: evolving
needs_canonical_source: true
related_concepts: []
sources: []
tags:
- hardening
- amortization
- mixture-model
- graph-construction
- cold-start
- data-management
title: Continuous Hardening Mixture Framework
understanding: 0
---

## Definition
Any system transitioning from inference-based operation to structure-based operation passes through a continuous mixture state rather than a discrete before/after transition.

## Core Structure

Define a confidence weight λ(n, t) ∈ [0,1] for each node or edge n at time t, representing the degree to which the hardened representation is trusted over LLM fallback.

- At t=0: λ(n, 0) = 0 for all n — no graph, full LLM fallback
- As traversal evidence accumulates: λ(n, t) → 1 for well-evidenced nodes and edges

The retrieval strategy at any moment is a mixture:

R(q, n, t) = λ(n, t) · R_graph(q, n) + (1 − λ(n, t)) · R_LLM(q, n)

## Hardening Rate

λ(n, t) increases as a function of query volume hitting n, the quality threshold required before trusting log-based over LLM signal, and the convergence rate of traversal statistics. Hardening is not uniform — high-frequency concepts accumulate evidence fast; tail concepts may never fully harden.

## Differential Convergence: Nodes vs Edges

Nodes and edges carry separate λ values and harden at different rates. Concept nodes accumulate evidence on every retrieval. Edges accumulate evidence only when the specific (c1, τ, c2) triple is traversed — a sparser signal. Therefore the traversal ranking signal (edge-based) lags behind node content signal in the maturity curve.

## Amortization Implications

The discrete breakeven chart is a limiting case. The real amortization curve has three regions:

1. Cold start: λ ≈ 0 everywhere. Full LLM cost. Construction cost being paid. Net cost higher than pure inference baseline.
2. Transition: λ rising heterogeneously. Blended cost per query. Savings accumulate as λ rises across the concept population.
3. Mature: λ ≈ 1 for high-frequency concepts. Near-pure retrieval savings on covered query classes. LLM fallback handles the tail.

The aggregate amortization schedule is the integral over the concept frequency distribution weighted by query volume coverage — not a single crossover point but a distribution of crossover points indexed by concept frequency.

## Generality

Applies wherever a system transitions from inference-based to structure-based operation: concept graph hardening, instance graph hardening, edge type calibration, and any data management context where structured representations are built incrementally over inference fallback. The mixture model is the general case; the discrete step function is a convenient but inaccurate simplification.

## Open Questions

- What functional form does λ(n, t) take? Logistic in query count? Bayesian posterior over a Bernoulli success model?
- How do you set the quality threshold for transitioning from LLM to log-based signal?
- How does differential hardening rate (nodes vs edges) affect the shape of the aggregate amortization curve?
- Can the hardening rate be estimated in advance from query distribution priors, enabling amortization forecasting before deployment?

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[giglou-llms4ol-2024]] — illustrated-by: Empirically confirms LLM boundary decision failure rates — supports ontologist-as-boundary-arbitrator positioning.
- [[shimizu-modular-2023]] — illustrated-by: Inseparability criterion provides formal self-containment test for nodes — prerequisite for meaningful hardening decisions.
[To be populated during integration]

## Needs Canonical Source
This stub was created without a source. Suggested references:

**Already in corpus:**
[none in corpus]

**External candidates (Semantic Scholar):**
[none found]