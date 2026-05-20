---
title: "Ensemble Learning"
knowledge_type: framework
also_type: [concept]
domain: [statistical-learning]
tags: [ensemble-methods, model-selection]
related_concepts: ["[[bias-variance-tradeoff]]", "[[gradient-boosting]]", "[[random-forests]]"]
sources: ["[[hastie-esl]]", "[[domingos-useful-things]]", "[[castle-model-selection-algorithms]]", "[[friedman-rulefit-2005]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 4
understanding: 0
maturity: settled
---

## Reading Path
- [[hastie-esl]] (unread) — mathematical treatment: bagging variance reduction proof, AdaBoost, stacking
- [[domingos-useful-things]] (unread) — §10: intuitive rationale; BMA vs. ensembles distinction (ensembles change the hypothesis space; BMA weights collapse to the single best hypothesis)
- [[castle-model-selection-algorithms]] (unread) — model averaging / BMA as ensemble alternative; comparison with single-model selection under low signal-to-noise conditions
- [[friedman-rulefit-2005]] (unread) — RuleFit as ISLE-based rule ensemble; primary treatment of rule extraction from boosted trees followed by lasso fitting

The organizing framework for methods that combine multiple base learners to produce a single prediction, including bagging, boosting, stacking, and random forests. Classification note: assigned as framework because it organizes a family of techniques under a common rationale (variance reduction through aggregation), but may also function as a concept describing the general principle.
