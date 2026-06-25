import { useEffect, useState } from 'react'
import { getDocsDrift, docsDriftAct, ApiError } from '../lib/api'
import type { DocsDriftItem, DocsDriftInbox } from '../types'

// Owner-only inbox lane: the Architect's fortnightly doc-drift audit. Each item is
// ONE atomic anchor→replacement edit to a living doc. Accept applies just that edit
// (server commits it); dismiss records the decision so it won't resurface. Stays
// quiet when there's nothing to review.
export default function DocsDriftSection({ onToast }: { onToast: (m: string) => void }) {
  const [data, setData] = useState<DocsDriftInbox | null>(null)
  const [loading, setLoading] = useState(true)
  const [busy, setBusy] = useState<string | null>(null)

  useEffect(() => {
    let cancelled = false
    getDocsDrift('pending')
      .then((d) => { if (!cancelled) { setData(d); setLoading(false) } })
      .catch(() => { if (!cancelled) setLoading(false) })   // 401/403 → silently absent (non-owner)
    return () => { cancelled = true }
  }, [])

  const act = async (it: DocsDriftItem, action: 'accept' | 'dismiss') => {
    setBusy(it.id)
    try {
      const r = await docsDriftAct(it.id, action)
      setData((prev) => prev && { ...prev, items: prev.items.filter((x) => x.id !== it.id) })
      onToast(action === 'accept'
        ? `applied to ${it.doc.replace('docs/', '')}${r.sha ? ` (${r.sha.slice(0, 7)})` : ''}`
        : 'dismissed')
    } catch (e) {
      onToast(e instanceof ApiError && e.status === 401 ? 'sign in as the owner'
        : e instanceof ApiError && e.status === 400 ? 'the doc changed since the audit — item is stale'
        : String(e))
    } finally {
      setBusy(null)
    }
  }

  if (loading) return null
  const items = data?.items ?? []
  if (items.length === 0) return null   // stay quiet when nothing to review

  return (
    <div className="inbox-section">
      <div className="inbox-section-head">
        <span className="inbox-section-title">Docs drift</span>
        <span className="inbox-section-count">{items.length}</span>
      </div>
      {items.map((it) => (
        <div key={it.id} className="drift-card">
          <div className="drift-titlerow">
            <span className="drift-doc">{it.doc.replace('docs/', '')}</span>
            <span className="drift-title">{it.title}</span>
          </div>
          {it.rationale && <div className="drift-rationale">{it.rationale}</div>}
          <div className="drift-diff">
            <div className="drift-old">− {it.anchor}</div>
            <div className="drift-new">+ {it.replacement}</div>
          </div>
          <div className="drift-actions">
            <button className="drift-btn accept" disabled={busy === it.id} onClick={() => act(it, 'accept')}>
              ✓ apply
            </button>
            <button className="drift-btn dismiss" disabled={busy === it.id} onClick={() => act(it, 'dismiss')}>
              ✕ dismiss
            </button>
          </div>
        </div>
      ))}
    </div>
  )
}
