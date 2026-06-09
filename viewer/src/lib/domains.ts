import type { DomainCount } from '../types'

// Family grouping for the domains. Folds the long flat list into a few scannable
// groups for the sidebar tree. Any live domain not listed here lands in "Other",
// so newly-introduced domains never silently disappear from navigation.
export const DOMAIN_FAMILIES: { family: string; domains: string[] }[] = [
  { family: 'AI & Learning', domains: [
    'agentic-ai', 'ai-safety', 'deep-learning', 'statistical-learning',
    'optimization', 'symbolic-subsymbolic', 'knowledge-representation',
  ] },
  { family: 'Probability & Inference', domains: [
    'bayesian-stats', 'causal-analysis', 'forecasting', 'time-series',
  ] },
  { family: 'Economics & Finance', domains: [
    'macroeconomics', 'monetary-economics', 'corporate-finance',
  ] },
  { family: 'Systems & Methods', domains: [
    'formal-methods', 'systems-theory', 'organizational-theory',
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
