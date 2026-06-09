import { useEffect, useState } from 'react'
import { getDomains } from '../lib/api'
import { groupDomains } from '../lib/domains'
import type { DomainGroup } from '../lib/domains'
import type { DomainCount } from '../types'

interface Props {
  active: string
  onChange: (domain: string) => void
}

// Collapsible domain navigator for the sidebar: families fold the 17 domains
// into a few scannable groups. The family holding the active domain auto-opens.
export default function DomainTree({ active, onChange }: Props) {
  const [domains, setDomains] = useState<DomainCount[]>([])
  const [open, setOpen] = useState<Record<string, boolean>>({})

  useEffect(() => {
    let cancelled = false
    getDomains().then((d) => { if (!cancelled) setDomains(d) }).catch(() => {})
    return () => { cancelled = true }
  }, [])

  if (domains.length === 0) return null
  const groups = groupDomains(domains)

  const isOpen = (g: DomainGroup) =>
    open[g.family] ?? g.items.some((i) => i.domain === active)

  return (
    <div className="sidebar-section">
      <div className="sidebar-section-label">domains</div>
      {groups.map((g) => {
        const o = isOpen(g)
        return (
          <div key={g.family} className="domain-group">
            <div
              className="domain-group-head"
              onClick={() => setOpen((s) => ({ ...s, [g.family]: !o }))}
            >
              <span className="domain-group-caret">{o ? '▾' : '▸'}</span>
              <span className="domain-group-name">{g.family}</span>
            </div>
            {o && g.items.map((it) => (
              <div
                key={it.domain}
                className={`domain-row${active === it.domain ? ' active' : ''}`}
                onClick={() => onChange(active === it.domain ? 'all' : it.domain)}
              >
                <span className="domain-row-name">{it.domain}</span>
                <span className="domain-row-count">{it.count}</span>
              </div>
            ))}
          </div>
        )
      })}
    </div>
  )
}
