import { useEffect, useState } from 'react'
import { getDiscovery, discoveryAct, ApiError } from '../lib/api'
import type { DiscoveryCandidate, DiscoveryInbox } from '../types'
import DiscoverDetailSheet from '../components/DiscoverDetailSheet'

interface Props {
  onSelectNode: (iri: string) => void
}

const DISMISS_CHIPS = ['too applied', 'off-topic', 'already know', 'low quality']

export default function DiscoverView({ onSelectNode }: Props) {
  const [inbox, setInbox] = useState<DiscoveryInbox | null>(null)
  const [loading, setLoading] = useState(true)
  const [busy, setBusy] = useState<string | null>(null)
  const [toast, setToast] = useState<string | null>(null)
  const [dismissing, setDismissing] = useState<string | null>(null) // id showing reason chips
  const [detail, setDetail] = useState<DiscoveryCandidate | null>(null)

  const load = () => {
    setLoading(true)
    getDiscovery('pending', 60)
      .then((d) => { setInbox(d); setLoading(false) })
      .catch(() => setLoading(false))
  }
  useEffect(() => { load() }, [])

  const showToast = (m: string) => { setToast(m); setTimeout(() => setToast(null), 2200) }

  const act = async (c: DiscoveryCandidate, action: 'accept' | 'dismiss', chip?: string) => {
    setBusy(c.id)
    try {
      const r = await discoveryAct(c.id, action, chip)
      // optimistic remove from the pending list
      setInbox((prev) => prev && { ...prev, candidates: prev.candidates.filter((x) => x.id !== c.id) })
      showToast(action === 'accept'
        ? `added → reading queue${r.source_slug ? ` (${r.source_slug})` : ''}`
        : 'dismissed — the prior will learn from this')
    } catch (e) {
      if (e instanceof ApiError && e.status === 401) showToast('sign in to triage discovery')
      else showToast(String(e))
    } finally {
      setBusy(null); setDismissing(null); setDetail(null)
    }
  }

  if (loading) {
    return <div className="loading-row"><div className="loading-spinner" /> loading discovery inbox…</div>
  }

  const cands = inbox?.candidates ?? []
  const counts = inbox?.counts ?? {}

  return (
    <div>
      <div className="discover-head">
        <div className="section-label" style={{ margin: 0 }}>discover · frontier-matched reads</div>
        <div className="discover-sub">
          {counts.accepted ? `${counts.accepted} accepted · ` : ''}
          {counts.dismissed ? `${counts.dismissed} dismissed · ` : ''}
          {inbox?.generated_at ? `updated ${inbox.generated_at.slice(0, 10)}` : ''}
        </div>
      </div>

      {cands.length === 0 && (
        <div className="empty-state">
          inbox empty — discovery runs weekly and surfaces papers that fill your current frontier gaps.
        </div>
      )}

      {cands.map((c) => (
        <div key={c.id} className="discover-card">
          <div className="discover-bar"><div className="discover-bar-fill" style={{ width: `${Math.min(100, c.sim * 100)}%` }} /></div>
          <div className="discover-titlerow" onClick={() => setDetail(c)}>
            {c.priority && <span className="disc-prio-badge sm">#{c.priority}</span>}
            <span className="discover-title">{c.title}</span>
          </div>
          <div className="discover-meta">
            {[c.authors, c.venue || 'preprint', c.year, c.field].filter(Boolean).join(' · ')} · cited {c.cited_by}×
          </div>
          <div className="discover-reason">
            <span
              className="discover-gap"
              onClick={() => onSelectNode(c.nearest_frontier.iri)}
              title="open the frontier concept this fills"
            >
              ◓ {c.nearest_frontier.title} (cov {c.nearest_frontier.coverage}/5)
            </span>
            <span className="discover-sim">sim {c.sim.toFixed(2)}</span>
            {c.prior_mult !== undefined && c.prior_mult !== 1 && (
              <span className="discover-prior">×{c.prior_mult}</span>
            )}
          </div>
          {(c.rationale?.why || c.abstract) && (
            <div className="discover-abstract" onClick={() => setDetail(c)}>
              {c.rationale?.why || c.abstract.slice(0, 240)}
              <span className="discover-more"> details →</span>
            </div>
          )}

          <div className="discover-actions">
            <a className="discover-link" href={c.url} target="_blank" rel="noreferrer">↗ paper</a>
            <span className="discover-link" onClick={() => setDetail(c)}>⊕ why read it</span>
            <div style={{ flex: 1 }} />
            {dismissing === c.id ? (
              <>
                {DISMISS_CHIPS.map((chip) => (
                  <span key={chip} className="discover-chip" onClick={() => act(c, 'dismiss', chip)}>{chip}</span>
                ))}
                <span className="discover-chip" onClick={() => act(c, 'dismiss')}>✕</span>
              </>
            ) : (
              <>
                <button className="action-btn primary discover-btn" disabled={busy === c.id} onClick={() => act(c, 'accept')}>✓ add</button>
                <button className="action-btn discover-btn" disabled={busy === c.id} onClick={() => setDismissing(c.id)}>✗ dismiss</button>
              </>
            )}
          </div>
        </div>
      ))}
      {toast && <div className="toast">{toast}</div>}

      {detail && (
        <DiscoverDetailSheet
          c={detail}
          busy={busy === detail.id}
          onClose={() => setDetail(null)}
          onSelectNode={onSelectNode}
          onAct={(action, chip) => act(detail, action, chip)}
        />
      )}
    </div>
  )
}
