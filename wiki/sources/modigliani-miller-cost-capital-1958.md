---
id: "pkis:source:modigliani-miller-cost-capital-1958"
aliases: []
title: "The Cost of Capital, Corporation Finance and the Theory of Investment"
authors: "Franco Modigliani, Merton H. Miller"
year: 1958
type: paper
domain: [corporate-finance]
tags: [arbitrage, capital-structure, cost-of-capital, leverage, valuation, uncertainty]
source_url: "https://doi.org/10.2307/1809766"
drive_id: "1AzPpK5DrhjjwH_2CTJwy65_0n2tq033q"
drive_path: "PKIS/sources/papers/The Cost of Capital, Corporation Finance and the Theory of Investment - Modigliani, Miller.pdf"
status: unread
date_added: 2026-05-20
concepts: [modigliani-miller-theorem, capital-structure-irrelevance, no-arbitrage-pricing, cost-of-capital, leverage-risk-premium, homogeneous-risk-class]
---

## Summary

Modigliani and Miller's 1958 paper establishes the foundational theory of how financial structure affects (or fails to affect) firm value under uncertainty. Prior to MM, finance was largely prescriptive and atheoretic about the relationship between capital structure and firm value. MM show that under conditions of perfect capital markets (no taxes, no bankruptcy costs, symmetric information, competitive markets), a firm's value is determined solely by its earning power and asset risk — not by how those assets are financed.

**Proposition I**: The market value of any firm is independent of its capital structure. V = X/ρ_k, where X is expected return on assets and ρ_k is the capitalization rate for the risk class k. This is proved via an arbitrage argument: if two firms with identical assets had different values solely due to capital structure, investors could "undo" the leverage in their personal portfolios, earning a riskless profit — a money machine that cannot persist in equilibrium.

**Proposition II**: The expected rate of return on equity of a levered firm rises linearly with leverage. i_j = ρ_k + (ρ_k − r)(D/S). More debt means higher equity risk premium, exactly offsetting the apparent cheapness of debt — so the weighted average cost of capital remains constant.

The paper then extends to the case with corporate income taxes, where interest deductibility creates a tax shield that does raise firm value with leverage, implying an (unrealistically extreme) corner solution at 100% debt financing. MM recognize this creates a tension with observed corporate behavior and defer full resolution.

MM also develop a theory of investment: the criterion for accepting a project is that its expected yield exceeds the firm's cost of capital for its risk class, independently of how the project is financed. This separates investment from financing decisions.

The paper's proof method — arbitrage rather than equilibrium — was as influential as its substantive results, prefiguring the Black-Scholes approach and the general no-arbitrage paradigm in asset pricing.

## Key Knowledge Objects

- [[modigliani-miller-theorem]] (result, high) — firm value is independent of capital structure under perfect markets; proved by arbitrage
- [[capital-structure-irrelevance]] (result, high) — MM Proposition I: the specific debt-equity mix does not affect total firm value
- [[no-arbitrage-pricing]] (principle, high) — if two portfolios have identical payoffs, they must have the same price; violations imply money machines
- [[cost-of-capital]] (concept, high) — the required rate of return on a firm's assets, equal to the capitalization rate for its risk class (independent of leverage under MM)
- [[leverage-risk-premium]] (result, high) — MM Proposition II: equity yield rises linearly with debt-to-equity ratio, keeping WACC constant
- [[homogeneous-risk-class]] (concept, moderate — could be framework) — MM's classification of firms into groups whose returns are perfectly correlated and thus perfect substitutes; analogous to the Marshallian industry

## Key Extractions

1. Proposition I (no taxes): "The market value of any firm is independent of its capital structure and is given by capitalizing its expected return at the rate ρ_k appropriate to its class. V_j = (S_j + D_j) = X_j / ρ_k."

2. Proposition II: "The expected yield of a share of stock is equal to the appropriate capitalization rate ρ_k for a pure equity stream in the class, plus a premium related to financial risk equal to the debt-to-equity ratio times the spread between ρ_k and r." i_j = ρ_k + (ρ_k − r)(D_j/S_j).

3. The arbitrage proof: Investors can replicate any firm's capital structure on personal account at the same borrowing terms, so levered and unlevered firms in the same risk class must have equal value — "homemade leverage" drives out any price discrepancy.

4. With corporate taxes: Proposition I with taxes implies V_L = V_U + τD — the value of the levered firm exceeds the unlevered firm by the tax shield τD, pushing toward 100% debt, which MM acknowledge is unrealistic and triggers subsequent trade-off theory.

5. Investment criterion: An investment project should be accepted if its expected yield exceeds the cost of capital for its risk class, "entirely independent of the tastes of the current owners, since market prices will reflect not only their preferences but those of all potential owners as well."

6. On the proof method: MM chose arbitrage over equilibrium because the absence of arbitrage "does not require the economy to be in equilibrium, though a competitive equilibrium is invariably arbitrage-free." This proved more general and became the standard tool in derivatives pricing.

## Connection Candidates

- [[modigliani-miller-theorem]] — grounds: this paper is the primary source of the theorem
- [[no-arbitrage-pricing]] — uses: the MM proof relies on the no-arbitrage principle
- [[capital-structure-irrelevance]] — grounds: Proposition I is the capital structure irrelevance result
- [[pagano-mm-cornerstone-2005]] — extends: Pagano's paper reviews and contextualizes MM's contribution 50 years on
- Potential connection to [[potential-outcomes-framework]] — none; different domain
- The "risk class" concept connects to [[directed-graphical-models]] — none directly
- Connects strongly to option pricing (Black-Scholes) via arbitrage method

## Awaiting Classification

- **homogeneous-risk-class** — candidate types: concept or framework
  - Case for concept: it defines a property of firms (identical risk profile) used as a classification device
  - Case for framework: it provides the structural apparatus (analogous to the "industry") within which Propositions I and II are proved
  - What makes this hard: MM use it as an analytic convenience that straddles definitional concept and theoretical apparatus
