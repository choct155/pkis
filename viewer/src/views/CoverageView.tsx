import { useEffect, useState } from 'react'
import type { ReaderCoverage } from '../types'
import { getReaderCoverage, buildReader } from '../lib/api'

// Owner-only "which content is narrated" panel. Shows overall coverage, the
// per-state breakdown, and the outstanding (narratable-but-unbuilt) backlog with a
// one-tap build button per paper. Book chapters narrate on demand and are excluded
// from the backlog by the endpoint.
const STATE_LABEL: Record<string, string> = {
  ready: 'ready', building: 'building', error: 'failed', none: 'not built', unknown: 'unknown',
}

export default function CoverageView({ onSelectNode }: { onSelectNode: (iri: string) => void }) {
  const [cov, setCov] = useState<ReaderCoverage | null>(null)
  const [err, setErr] = useState<string | null>(null)
  const [kicked, setKicked] = useState<Record<string, boolean>>({})

  const load = () => getReaderCoverage().then(setCov).catch(() => setErr('Could not load coverage.'))
  useEffect(() => { load() }, [])

  const build = async (slug: string) => {
    setKicked((k) => ({ ...k, [slug]: true }))
    try { await buildReader(slug) } catch { /* leave marked; retry refreshes */ }
  }

  if (err) return <div className="cov-view"><div className="cov-empty">{err}</div></div>
  if (!cov) return <div className="cov-view"><div className="cov-empty">loading coverage…</div></div>

  const pct = Math.round((100 * cov.ready) / Math.max(cov.total_sources, 1))
  const order = ['ready', 'building', 'error', 'none', 'unknown']
  const states = Object.entries(cov.by_state).sort((a, b) => order.indexOf(a[0]) - order.indexOf(b[0]))

  return (
    <div className="cov-view">
      <div className="cov-head">
        <h2 className="cov-title">Narration coverage</h2>
        <button className="cov-refresh" onClick={() => { setCov(null); load() }}>↻ refresh</button>
      </div>

      <div className="cov-summary">
        <div className="cov-bignum">{cov.ready}<span className="cov-bignum-sub">/{cov.total_sources}</span></div>
        <div className="cov-bar" aria-label={`${pct}% narrated`}>
          <div className="cov-bar-fill" style={{ width: `${pct}%` }} />
        </div>
        <div className="cov-pct">{pct}% of sources narrated</div>
      </div>

      <div className="cov-states">
        {states.map(([s, n]) => (
          <span key={s} className={`cov-chip cov-chip-${s}`}>{STATE_LABEL[s] || s}: {n}</span>
        ))}
      </div>

      <div className="cov-backlog-head">
        Outstanding — narratable, not yet built ({cov.outstanding_count})
      </div>
      {cov.outstanding.length === 0 ? (
        <div className="cov-empty">Everything narratable is built. 🎧</div>
      ) : (
        <ul className="cov-list">
          {cov.outstanding.map((r) => (
            <li key={r.slug} className="cov-row">
              <button className="cov-row-title" onClick={() => onSelectNode(`pkis:source:${r.slug}`)}
                title={r.slug}>{r.title}</button>
              <span className={`cov-state cov-state-${r.state}`}>{STATE_LABEL[r.state] || r.state}</span>
              <button className="cov-build" disabled={kicked[r.slug] || r.state === 'building'}
                onClick={() => build(r.slug)}>
                {kicked[r.slug] || r.state === 'building' ? 'building…' : 'build →'}
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}
