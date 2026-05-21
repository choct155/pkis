---
title: "Counterfactuals"
knowledge_type: concept
also_type: []
domain: [causal-analysis, bayesian-stats]
tags: [causality, potential-outcomes, counterfactual-reasoning, rubin-causal-model]
related_concepts: ["[[structural-causal-models]]", "[[do-calculus]]", "[[confounding]]", "[[probability-theory]]"]
sources: ["[[pearl-causality]]", "[[cunningham-causal-inference-mixtape]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: evolving
---

## Reading Path
- [[pearl-causality-ch07]] (unread) — logic of structure-based counterfactuals; formal definition via SCM
- [[pearl-causality-ch08]] (unread) — bounding counterfactual effects in imperfect experiments
- [[pearl-causality-ch09]] (unread) — probability of causation; necessity and sufficiency
- [[cunningham-causal-inference-mixtape-ch05]] (unread) — potential outcomes formalization: Y(0), Y(1), ATE/ATT, the fundamental problem of causal inference

Counterfactual reasoning asks: "What would Y have been had X been different, given that we observed X=x?" In the SCM framework, the counterfactual Y_x(u) denotes the value Y takes when X is set to x via do(X=x) in a world with background context U=u. This is Level 3 of Pearl's Ladder of Causation — strictly above both association (Level 1) and intervention (Level 2) — requiring knowledge of the full structural equations, not just the graph topology. Connects to Rubin's potential outcomes framework, which Pearl shows is a special case of SCM counterfactuals.
