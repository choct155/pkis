import { useEffect, useState } from 'react'
import { getGraphGaps, graphGapsAct, ApiError } from '../lib/api'
import type { GraphGapInbox, GraphGapItem, GraphGapEdge } from '../types'

// Owner inbox lane: orphaned concept-side nodes (zero edges) with SUGGESTED typed edges.
// Each suggestion is editable — change the predicate (dropdown) or the target, add/remove
// rows — then Approve applies the edges (add_connections, server commits) or Dismiss drops it.
const slugOf = (iri: string) => iri.split(':').pop() || iri

export default function GraphGapsSection(
  { onSelectNode, onToast }: { onSelectNode: (iri: string) => void; onToast: (m: string) => void },
) {
  const [data, setData] = useState<GraphGapInbox | null>(null)
  const [loading, setLoading] = useState(true)
  const [busy, setBusy] = useState<string | null>(null)
  const [edits, setEdits] = useState<Record<string, GraphGapEdge[]>>({})

  useEffect(() => {
    let cancelled = false
    getGraphGaps('pending')
      .then((d) => {
        if (cancelled) return
        setData(d); setLoading(false)
        const seed: Record<string, GraphGapEdge[]> = {}
        d.items.forEach((it) => {
          seed[it.id] = it.suggestions.map((s) => ({
            target: slugOf(s.target), predicate: s.predicate, target_title: s.target_title,
          }))
        })
        setEdits(seed)
      })
      .catch(() => { if (!cancelled) setLoading(false) })   // 401/403 → silently absent
    return () => { cancelled = true }
  }, [])

  const preds = data?.predicates ?? []
  const rows = (id: string) => edits[id] ?? []
  const setRow = (id: string, i: number, field: keyof GraphGapEdge, val: string) =>
    setEdits((p) => { const r = [...rows(id)]; r[i] = { ...r[i], [field]: val }; return { ...p, [id]: r } })
  const addRow = (id: string) =>
    setEdits((p) => ({ ...p, [id]: [...rows(id), { target: '', predicate: preds[0] || 'related' }] }))
  const rmRow = (id: string, i: number) =>
    setEdits((p) => ({ ...p, [id]: rows(id).filter((_, j) => j !== i) }))

  const act = async (it: GraphGapItem, action: 'accept' | 'dismiss') => {
    setBusy(it.id)
    try {
      const edges = action === 'accept'
        ? rows(it.id).filter((e) => e.target.trim() && e.predicate)
        : undefined
      if (action === 'accept' && (!edges || edges.length === 0)) {
        onToast('add at least one edge (target + predicate)'); setBusy(null); return
      }
      const r = await graphGapsAct(it.id, action, edges)
      setData((prev) => prev && { ...prev, items: prev.items.filter((x) => x.id !== it.id) })
      onToast(action === 'accept' ? `wired ${it.slug} (${r.added?.length ?? 0} edge${r.added?.length === 1 ? '' : 's'})` : 'dismissed')
    } catch (e) {
      onToast(e instanceof ApiError && e.status === 401 ? 'sign in as the owner' : String(e))
    } finally {
      setBusy(null)
    }
  }

  if (loading) return null
  const items = data?.items ?? []
  if (items.length === 0) return null

  return (
    <div className="inbox-section">
      <div className="inbox-section-head">
        <span className="inbox-section-title">Graph gaps</span>
        <span className="inbox-section-count">{items.length}</span>
      </div>
      {items.map((it) => (
        <div key={it.id} className="gap-card">
          <div className="gap-titlerow">
            <span className="gap-type">{it.node_type}</span>
            <span className="gap-title" onClick={() => onSelectNode(it.iri)} title="open node">{it.title}</span>
            <span className="gap-orphan">orphaned · 0 edges</span>
          </div>
          <div className="gap-edges">
            {rows(it.id).map((e, i) => (
              <div key={i} className="gap-edge">
                <span className="gap-subj">{it.slug}</span>
                <select className="gap-pred" value={e.predicate} onChange={(ev) => setRow(it.id, i, 'predicate', ev.target.value)}>
                  {preds.map((p) => <option key={p} value={p}>{p}</option>)}
                </select>
                <input
                  className="gap-target" value={e.target}
                  placeholder={e.target_title || 'target slug'}
                  onChange={(ev) => setRow(it.id, i, 'target', ev.target.value)}
                />
                <span className="gap-rm" title="remove edge" onClick={() => rmRow(it.id, i)}>×</span>
              </div>
            ))}
            <span className="gap-add" onClick={() => addRow(it.id)}>+ add edge</span>
          </div>
          <div className="gap-actions">
            <button className="gap-btn approve" disabled={busy === it.id} onClick={() => act(it, 'accept')}>✓ approve</button>
            <button className="gap-btn dismiss" disabled={busy === it.id} onClick={() => act(it, 'dismiss')}>✕ dismiss</button>
          </div>
        </div>
      ))}
    </div>
  )
}
