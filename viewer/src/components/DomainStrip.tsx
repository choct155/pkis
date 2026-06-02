import { useEffect, useState } from 'react'
import { getDomains } from '../lib/api'
import type { DomainCount } from '../types'

interface Props {
  active: string
  onChange: (domain: string) => void
}

export default function DomainStrip({ active, onChange }: Props) {
  const [domains, setDomains] = useState<DomainCount[]>([])

  useEffect(() => {
    let cancelled = false
    getDomains().then((d) => { if (!cancelled) setDomains(d) }).catch(() => {})
    return () => { cancelled = true }
  }, [])

  if (domains.length === 0) return null

  return (
    <div className="filter-strip domain-strip">
      <div
        className={`filter-chip chip-domain${active === 'all' ? ' active-type' : ''}`}
        onClick={() => onChange('all')}
      >
        all domains
      </div>
      {domains.map((d) => (
        <div
          key={d.domain}
          className={`filter-chip chip-domain${active === d.domain ? ' active-type' : ''}`}
          onClick={() => onChange(active === d.domain ? 'all' : d.domain)}
        >
          {d.domain} <span className="chip-count">{d.count}</span>
        </div>
      ))}
    </div>
  )
}
