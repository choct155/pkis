# Explainer Roadmap

Tracks planned and in-progress explainers for the PKIS knowledge base.
Update this file directly or via Claude.ai sessions.

## Registered (live in pkis.dev/app/)

| Asset IRI | Title | Kind |
|---|---|---|
| pkis:asset:hmc-explainer | Hamiltonian Monte Carlo — A Complete Mechanical Account | explainer |
| pkis:asset:mcmc-trace-viz | Metropolis–Hastings sampling trace | visualization |
| pkis:asset:typical-set-explainer | Typical Sets — where the probability actually lives | explainer |
| pkis:asset:knowledge-infrastructure-explainer | The Knowledge Graph as Compounding Infrastructure | explainer |
| pkis:asset:mi-estimation-explainer | Mutual Information Estimation — Technical Reference | explainer |
| pkis:asset:accuracy-calibration-explainer | Accuracy Estimation — Silver/Gold Calibration | explainer |
| pkis:asset:retrieval-efficiency-example | Retrieval Efficiency — Interactive Worked Example | visualization |
| pkis:asset:retrieval-efficiency-explainer | Retrieval Efficiency — Concept Node vs Document | explainer |

## Planned

| Slug | Title | Priority | Blocks | Status |
|---|---|---|---|---|
| hardening-trajectory-explainer | The Hardening Trajectory — λ(n,t) and cost curve over time | HIGH | Position paper §2.2; external pitch | planned |
| quality-framework-explainer | Retrieval Quality — Seven Dimensions and Architecture Profiles | HIGH | Position paper §3; retrieval comparison experiment | planned |
| passive-instrumentation-explainer | Passive Instrumentation — Production and Client-Side Quality Signals | MEDIUM | Position paper §3.5; engineering manager pitch | planned |
| retrieval-comparison-explainer | Graph vs Vector — Side-by-Side Quality Differential (with real numbers) | HIGH | Position paper §5.2; external pitch | BLOCKED — needs intelligent layer empirical results |

## How to add a new explainer

1. Build the HTML file in Claude.ai or Claude Code
2. Copy to the viz serving directory as `<slug>.html`
3. Create `wiki/assets/<slug>.md` with canonical frontmatter (see hmc-explainer.md)
4. Add `illustrated-by` edges from the relevant wiki nodes via MCP `add_connections`
5. Commit and push — asset appears in pkis.dev/app/ immediately
6. Update this roadmap table

## Style guide

All explainers use the PKIS instrument aesthetic:
- Background: #07080a (near-black)
- Primary accent: #e8a045 (amber)
- Interactive elements: #4fc3c8 (cyan)
- Typography: IBM Plex Mono (math/code), IBM Plex Sans (prose), IBM Plex Serif (headings)
- Reference: wiki/assets/hmc-explainer.md and the HMC HTML source for canonical structure
