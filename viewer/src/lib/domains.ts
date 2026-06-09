import type { DomainCount } from '../types'

// Family grouping for the domains. Folds the long flat list into a few scannable
// groups for the sidebar tree. Any live domain not listed here lands in "Other",
// so newly-introduced domains never silently disappear from navigation.
export const DOMAIN_FAMILIES: { family: string; domains: string[] }[] = [
  { family: 'AI & Learning', domains: [
    'deep-learning', 'statistical-learning', 'optimization', 'reinforcement-learning',
    'knowledge-representation', 'symbolic-subsymbolic', 'computer-vision',
    'robotics', 'search-and-planning',
  ] },
  { family: 'Agents & Safety', domains: [
    'agentic-ai', 'agentic-systems', 'multi-agent-systems', 'ai-safety', 'ai-alignment',
  ] },
  { family: 'Probability & Inference', domains: [
    'bayesian-stats', 'causal-analysis', 'information-theory', 'decision-theory',
    'time-series', 'state-space-models', 'forecasting', 'econometrics', 'signal-processing',
  ] },
  { family: 'Economics & Finance', domains: [
    'macroeconomics', 'monetary-economics', 'corporate-finance', 'economics', 'asset-pricing',
  ] },
  { family: 'Systems & Methods', domains: [
    'systems-theory', 'formal-methods', 'organizational-theory', 'computer-science',
    'social-choice', 'social-science-methods', 'neuroscience',
  ] },
]

const KNOWN = new Set(DOMAIN_FAMILIES.flatMap((f) => f.domains))

export interface DomainGroup {
  family: string
  items: DomainCount[]
}

// Group live domain counts into families, preserving the family order above and
// the curated within-family order. Unmapped domains collect into "Other".
export function groupDomains(domains: DomainCount[]): DomainGroup[] {
  const count = new Map(domains.map((d) => [d.domain, d.count]))
  const groups: DomainGroup[] = DOMAIN_FAMILIES
    .map((f) => ({
      family: f.family,
      items: f.domains
        .filter((d) => count.has(d))
        .map((d) => ({ domain: d, count: count.get(d)! })),
    }))
    .filter((g) => g.items.length > 0)

  const other = domains.filter((d) => !KNOWN.has(d.domain))
  if (other.length) groups.push({ family: 'Other', items: other })
  return groups
}
