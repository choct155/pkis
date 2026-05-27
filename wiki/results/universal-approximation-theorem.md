---
id: "pkis:result:universal-approximation-theorem"
aliases: []
title: "Universal Approximation Theorem"
knowledge_type: result
also_type: []
domain: [deep-learning]
tags: [approximation-theory, neural-networks, expressiveness, sigmoid]
related_concepts: ["[[neural-networks]]", "[[activation-functions]]", "[[bias-variance-tradeoff]]"]
sources: ["[[nielsen-nndl]]", "[[liu-kan-2024]]", "[[marcus-dl-critical-appraisal-2018]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

A network with a single hidden layer of sigmoid (or other non-polynomial activation) neurons can approximate any continuous function f: [0,1]^m → R^n to arbitrary precision, given enough hidden neurons; the result establishes the expressive power of shallow networks but does not speak to whether such networks are efficiently learnable or whether depth provides advantages over width.

## Reading Path
- [[nielsen-nndl-ch04]] (unread) — constructive visual proof building step functions from neuron pairs with large weights, demonstrating the result intuitively for one and many input variables
- [[liu-kan-2024]] (unread) — contrasts UAT (MLP foundation) with KAT (KAN foundation); UAT guarantees approximation but not scaling rate; KAT provides explicit G^{-(k+1)} bound
- [[marcus-dl-critical-appraisal-2018]] (unread) — §2: distinguishes expressiveness (what UAT guarantees) from learnability (what gradient descent can find) and robustness; argues UAT provides false comfort — knowing a function class can approximate anything does not ensure efficient learning or out-of-distribution generalization
