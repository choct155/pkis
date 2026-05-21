---
title: "Game Theory Models in Finance"
authors: "Franklin Allen and Stephen Morris"
year: 2001
type: paper
domain: [asset-pricing, corporate-finance]
tags: [game-theory, information-asymmetry, signaling, mechanism-design, higher-order-beliefs, informational-cascades]
source_url: ""
drive_id: "1o5Io4kQOvmTXY1SXFoN8PpypnRQ7GxPF"
drive_path: "PKIS/sources/papers/Game Theory Models in Finance - Allen, Morris.pdf"
status: unread
date_added: 2026-05-20
concepts: [capm, modigliani-miller-theorem, signaling-games, adverse-selection, principal-agent-problem, higher-order-beliefs, informational-cascades, market-microstructure, bank-runs]
---

## Summary

Allen and Morris (2001) provide a survey of game-theoretic contributions to finance, arguing that game theory revolutionized the field by allowing asymmetric information and strategic interaction to enter models where classical finance's symmetric-information, perfect-markets assumptions had failed. The paper is organized in three sections: (1) the main unresolved issues in pre-game-theoretic finance (CAPM, EMH, MM propositions, corporate finance puzzles); (2) first-generation game-theoretic solutions across corporate finance (dividends as signals, capital structure, takeovers, IPOs, banking) and asset pricing (market microstructure); and (3) a forward-looking section on richer informational models.

The third section is the most novel contribution to the literature. Allen and Morris argue that conventional models of asymmetric information implicitly assume common knowledge of beliefs — either by assuming independent signals or by assuming signals uniquely determine beliefs. This rules out a role for higher-order beliefs (what players believe about what others believe). Using a modified Diamond-Dybvig bank-run model, they show that when signals are correlated in a way that precludes common knowledge that fundamentals are good (even if each depositor knows and knows the other knows there is no liquidity crisis), the unique equilibrium is a run. The outcome is determined not by fundamentals or sunspots but by the structure of higher-order beliefs. This connects to the "global games" literature (Carlsson-van Damme, Morris-Shin), where small perturbations from common knowledge select unique equilibria in coordination games — with direct implications for currency attacks and asset price crashes.

## Key Knowledge Objects

- [[signaling-games]] (framework, high) — game-theoretic models where informed parties take costly actions to credibly communicate private information; applied to dividends, capital structure, IPOs
- [[adverse-selection]] (concept, high) — Myers-Majluf equity issuance problem; informed insiders avoid issuing equity when it is undervalued, creating a lemons equilibrium
- [[principal-agent-problem]] (concept, high) — Jensen-Meckling framework for conflicts between equity holders, bondholders, and managers; agency costs of debt and equity
- [[higher-order-beliefs]] (concept, high) — what players believe about others' beliefs; shown to determine equilibria in coordination games even when fundamentals are common knowledge up to any finite level
- [[informational-cascades]] (concept, high) — sequential decision-making where agents ignore private information and follow prior observed actions; Welch (1992) IPO model
- [[market-microstructure]] (framework, high) — strategic models of price formation under asymmetric information; Kyle (1985) and Glosten-Milgrom (1985) models of bid-ask spreads and informed trading
- [[bank-runs]] (concept, high) — Diamond-Dybvig (1983) self-fulfilling equilibria; extended here to show higher-order beliefs as a third coordination channel beyond fundamentals and sunspots
- [[free-rider-problem]] (concept, high) — Grossman-Hart (1980) takeover puzzle: each target shareholder has incentive to hold out for post-acquisition value improvements
- [[pecking-order-theory]] (framework, moderate — could be result) — Myers (1984) theory that firms prefer internal funds, then debt, then equity due to asymmetric information cost ordering
- common-prior-assumption (low — concept or principle?) — the assumption that all differences in beliefs are explained by differences in information, not priors; Allen and Morris argue this is neither justified nor necessary

## Key Extractions

1. "Game theory has provided a methodology that has brought insights into many previously unexplained phenomena by allowing asymmetric information and strategic interaction to be incorporated into the analysis." (p. 23)

2. Bhattacharya (1979) dividend signaling: managers signal future cash flow by committing to high dividends; the credibility cost is the transaction costs of outside financing if the project fails — making mimicry by low-quality firms unprofitable.

3. Myers-Majluf adverse selection (1984): firms prefer internal funds over debt over equity because equity issuance signals overvaluation; the resulting "pecking order" is consistent with observed corporate financing patterns.

4. Diamond-Dybvig (1983) bank runs: deposit contracts with sequential service (first-come-first-served) create two equilibria — a good equilibrium (only liquidity-needy withdraw) and a bad equilibrium (runs) eliminable by deposit insurance.

5. Higher-order beliefs example: Even when both depositors know their types are above the liquidity threshold, and know the other knows, and this is true to any finite level — it need not be common knowledge. Under correlated signals, the unique equilibrium is always a run. "What matters is depositors' higher order beliefs: what they believe about fundamentals, what they believe others believe, and so on." (p. 34–36)

6. On heterogeneous priors: Harrison and Kreps (1978) show that heterogeneous beliefs + short-sale constraints create a speculative premium — assets trade above any trader's fundamental value because of the option to resell to a more optimistic investor. This provides a rational formalization of "bubbles" without irrationality.

## Connection Candidates

- [[signaling-games]] — framework: paper surveys the full application of signaling theory to corporate finance puzzles
- [[higher-order-beliefs]] — concept: the novel section 3 is the primary treatment of this concept in finance
- [[bank-runs]] — concept: the paper extends Diamond-Dybvig to show higher-order beliefs as a coordination mechanism
- [[market-microstructure]] — framework: paper reviews Kyle (1985) and Glosten-Milgrom (1985) as the primary game-theoretic asset pricing contributions
- [[informational-cascades]] — concept: Welch (1992) IPO application surveyed; connection to sequential information aggregation
- [[multi-agent-systems]] — framework: the strategic interaction focus of the paper is the finance-domain application of multi-agent reasoning
- [[directed-graphical-models]] — framework: the information structure in these models (who knows what, who knows who knows) can be formalized as a graphical information structure — connection candidate for the Synthesizer
- [[structural-causal-models]] — framework: asymmetric information models assume specific causal structures about who has private information and how it enters equilibrium prices
