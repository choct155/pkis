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
- robotics
- machine-learning
id: pkis:technique:fastslam
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch13
tags:
- slam
- particle-filter
- rao-blackwellization
- robotics
- kalman-filter
- landmark-map
title: FastSLAM
understanding: 0
---

## Definition
FastSLAM is an RBPF algorithm for simultaneous localization and mapping (SLAM) that exploits the conditional independence of landmark locations given the robot trajectory:
$$p(l^{1:K}_t | r_{1:t}, y_{1:t}) = \prod_{k=1}^K p(l^k_t | r_{1:t}, y_{1:t})$$

Each particle represents a sampled robot path $r_{1:t}^n$, and maintains $K$ independent Kalman filters (or EKFs) for the landmark positions. The overall per-step cost is $O(NK)$, making the algorithm essentially linear in the number of landmarks.

### Why it matters
FastSLAM overcame the $O(K^3)$ bottleneck of the monolithic Kalman-filter SLAM approach, enabling real-time mapping in large environments. It is a canonical example of how Rao-Blackwellization combined with particle filtering yields both computational efficiency and probabilistic correctness.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]