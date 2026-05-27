---
id: "pkis:source:bernanke-financial-intermediation-2022"
aliases: []
title: "Financial Intermediation and the Economy"
authors: "Royal Swedish Academy of Sciences Nobel Committee"
year: 2022
type: article
domain: [macroeconomics, monetary-economics]
tags: [banks, financial-intermediation, bank-runs, Great-Depression, Global-Financial-Crisis, credit-channel, maturity-transformation, delegated-monitoring, deposit-insurance, lender-of-last-resort, shadow-banking, macroprudential]
source_url: "https://www.kva.se"
drive_id: "14QE06eTEhwgFyEM_aWiG4amr7SOfhFj2"
drive_path: "PKIS/sources/papers/Financial Intermediation and the Economy - Bernanke.pdf"
status: unread
date_added: 2026-05-20
concepts: [maturity-transformation, bank-run, delegated-monitoring, credit-channel, financial-intermediation, bank-fragility]
---

## Summary

This is the official scientific background document prepared by the Nobel Committee for the 2022 Sveriges Riksbank Prize in Economic Sciences, awarded jointly to Ben S. Bernanke, Douglas W. Diamond, and Philip H. Dybvig "for their research on banks and financial crises." The document synthesises three foundational contributions and their subsequent influence.

Diamond and Dybvig (1983) showed that maturity transformation — a bank's transformation of short-term liquid deposits into long-term illiquid loans — is the most efficient institutional arrangement for channeling savings into investment, but that this same structure creates an inherent vulnerability to self-fulfilling bank runs: if depositors believe other depositors will withdraw, rational self-interest demands that they withdraw first, creating the very crisis they feared. Deposit insurance and lender-of-last-resort facilities can prevent such coordination failures.

Diamond (1984) showed that banks perform delegated monitoring: by pooling loans across many borrowers and financing them with essentially risk-free debt, banks gain the right incentives to monitor borrowers on behalf of dispersed savers. This explains why banks exist as institutions — they solve the "who monitors the monitor" problem by making depositors' ability to force bankruptcy the disciplinary mechanism.

Bernanke (1983) provided the empirical counterpart: examining the Great Depression, he demonstrated that bank failures were not merely a side-effect of the downturn (as had been assumed since Keynes and Friedman-Schwartz), nor did they matter only via money-supply contraction. The destruction of banking relationships per se — the credit channel — was the primary mechanism deepening and prolonging the depression, as documented by the severe credit crunch hitting households, farms, and small businesses.

The document also covers the 2007–2009 Global Financial Crisis, showing that shadow-banking runs triggered by fundamental housing-sector shocks reproduced the Diamond–Dybvig mechanism on a modern institutional substrate (repo markets, money-market funds), and documents how the laureates' frameworks guided policy responses.

## Key Knowledge Objects

- [[maturity-transformation]] (concept, high) — the process by which banks take short-maturity liabilities (demand deposits) and create long-maturity assets (loans), generating liquidity for the economy but creating inherent run vulnerability
- [[bank-run]] (concept, high) — a self-fulfilling coordination failure in which depositors' rational anticipation that others will withdraw leads all to withdraw, collapsing a solvent institution
- [[delegated-monitoring]] (concept, high) — Diamond's theory that banks resolve information asymmetry between lenders and borrowers by monitoring borrowers on behalf of dispersed savers, using depositors' bankruptcy threat as the bank's disciplinary mechanism
- [[credit-channel]] (concept, high) — Bernanke's mechanism by which bank-failure-induced destruction of lending relationships causes real economic harm, distinct from the monetary channel emphasised by Friedman–Schwartz
- [[bank-fragility]] (concept, high) — the structural vulnerability of financial intermediaries arising from maturity transformation: the same architecture that creates liquidity also enables self-fulfilling runs
- [[shadow-banking]] (concept, moderate — could be framework) — the set of non-bank financial intermediaries (repo markets, money-market funds, ABS) that perform maturity transformation without formal deposit insurance, replicating bank-run vulnerability in new institutional forms

## Key Extractions

1. **Diamond–Dybvig bank-run mechanism (Section 1.2):** "A particularly troubling situation is a bank run or (bank panic), where depositors rush to the bank to withdraw their funds because they expect others to do the same, i.e., they hope to be first in line while there are still some funds left in the bank. Even fundamentally healthy banks may get into trouble if such bank runs become widespread."

2. **Delegated monitoring summary (Section 1.2):** "By using their expertise in evaluating and monitoring borrowers, and by pooling funds from many savers and diversifying across borrowers, banks reduce the aggregate monitoring costs that would otherwise have been borne by borrowers. This enables households' savings to be channeled to productive investments at a lower cost."

3. **Credit channel vs. monetary channel (Section 1.3):** "Bank failures destroyed valuable banking relationships, and the resulting credit supply contraction left significant scars in the real economy. These were new insights; earlier economic historians had viewed bank failures merely as a consequence of the downturn, or mattering to the rest of the economy only by contracting the money supply."

4. **Equity as monitoring incentive (Section 3, closely related research):** "Without [depositors' ability to force bankruptcy], savers would have to monitor the banks themselves and little gain would result from having banks as intermediaries. Pooling is thus key in solving the problem of 'who should monitor the monitor.'"

5. **2008 panic as Diamond–Dybvig (Section 5):** "Bernanke (2018) shows that the fundamental shock that started the crisis was the slump in the housing sector, but it did not lead to a dramatic economic downturn until panic arose in the financial markets. As in Diamond and Dybvig (1983), this panic led to self-perpetuating runs."

6. **Moral hazard caveat (Section 1.4):** "Policy interventions such as deposit insurance come not only with benefits, but also with potentially significant costs. Many observers have argued, for example, that excessive protection of banks can lead to moral hazard and may contribute to inequality."

## Connection Candidates

- [[identification-strategy]] — uses: Bernanke (1983) uses narrative and cross-sectional identification strategies to separate the credit channel from the monetary channel in Great Depression data; relates to broader econometric questions of causal identification
- [[markov-chains]] — prerequisite-of: the bank-run equilibrium selection problem in Diamond–Dybvig is formally a coordination game (global games extensions use Markov-like belief propagation structures)
- [[directed-graphical-models]] — contrasts-with: credit-channel propagation could be represented as a causal graph where bank failures are nodes transmitting economic distress; illustrates how macro network effects can be given causal structure
- [[var-models]] — uses: macroeconomic tests of the credit channel (post-Bernanke literature) typically use VAR decompositions to identify credit supply vs. demand shocks
- [[quantity-theory-of-money]] — contrasts-with: Bernanke (1983) explicitly disputes Friedman–Schwartz by showing that bank failures matter beyond their effect on money supply, directly contradicting the pure monetary-transmission account
