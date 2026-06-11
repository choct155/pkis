---
aliases: []
also_type: []
analogous-to:
- annealed-importance-sampling
applies:
- partition-function
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
- machine-learning
- statistics
- probabilistic-graphical-models
extends:
- importance-sampling
id: pkis:technique:bridge-sampling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch18
tags:
- partition-function
- importance-sampling
- model-evaluation
- Monte-Carlo
title: Bridge Sampling
understanding: 0
---

## Definition
**Bridge Sampling** (Bennett, 1976) estimates the ratio $Z_1/Z_0$ using a single **bridge distribution** $p_*$ with support overlapping both $p_0$ and $p_1$:
$$\frac{Z_1}{Z_0} \approx \frac{\sum_{k=1}^K \tilde{p}_*(x_0^{(k)})/\tilde{p}_0(x_0^{(k)})}{\sum_{k=1}^K \tilde{p}_*(x_1^{(k)})/\tilde{p}_1(x_1^{(k)})}, \quad x_0^{(k)}\sim p_0,\; x_1^{(k)}\sim p_1.$$
The optimal bridge is $p_*^{(\text{opt})}(x) \propto \tilde{p}_0(x)\tilde{p}_1(x)/(r\tilde{p}_0(x)+\tilde{p}_1(x))$ where $r=Z_1/Z_0$, which can be estimated iteratively. **Linked importance sampling** (Neal, 2005) combines bridge sampling with AIS to bridge consecutive intermediate distributions, improving overall efficiency.

### Why it matters
Bridge sampling is more efficient than AIS when $D_{\text{KL}}(p_0\|p_1)$ is moderate (the two distributions are not too far apart), as a single well-chosen bridge can capture the overlap. It provides variance reduction over standard importance sampling. The iterative estimation of the optimal bridge makes it self-refining. When combined with AIS via linked importance sampling, it achieves the benefits of both methods.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[partition-function]] — applies
- [[annealed-importance-sampling]] — analogous-to
- [[importance-sampling]] — extends
[To be populated during integration]