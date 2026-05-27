---
id: "pkis:technique:model-averaging"
aliases: []
title: "Model Averaging"
knowledge_type: technique
also_type: [framework]
domain: [statistical-learning, bayesian-stats]
tags: [bayesian-model-averaging, bma, model-selection, ensemble-methods, portfolio-models, uncertainty-quantification]
related_concepts: ["[[model-selection-problem]]", "[[information-criteria]]", "[[ensemble-learning]]", "[[directed-graphical-models]]", "[[inductive-bias]]"]
sources: ["[[castle-model-selection-algorithms]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Rather than selecting a single best model, model averaging constructs a composite estimate by taking a weighted combination of estimates from multiple models, with weights proportional to each model's posterior probability (BMA) or information-criterion-based likelihood. In Bayesian Model Averaging the composite coefficient estimate for variable k is the BMA-weighted average of its estimates across all 2^L candidate models, with zero contributed by models that exclude the variable.

Classification note: assigned as technique but `also_type: framework` because BMA provides a coherent probabilistic framework for reasoning about model uncertainty, not just a procedure. The distinction from ensemble learning is that model averaging operates over a space of model specifications sharing the same predictor set, while ensemble methods combine distinct estimators trained independently.

## Reading Path
- [[castle-model-selection-algorithms]] (unread) — BMA via log-likelihood weights compared to IC-based portfolio models; LLWeighted_All (averaging over all 2^L models) outperforms LLWeighted_Selected; BMA weights tend to concentrate on a single model in practice, echoing Domingos' finding
