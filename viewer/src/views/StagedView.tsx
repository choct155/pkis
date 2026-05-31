import { useEffect, useState } from 'react'
import { getStagedNodes, commitStaged } from '../lib/api'
import type { StagedNode } from '../types'
import { TypeBadge } from '../components/NodeCard'

interface Props {
  onSelectNode: (iri: string) => void
}

export default function StagedView({ onSelectNode }: Props) {
  const [nodes, setNodes] = useState<StagedNode[]>([])
  const [loading, setLoading] = useState(true)
  const [committing, setCommitting] = useState<string | null>(null)
  const [toast, setToast] = useState<string | null>(null)

  const load = () => {
    setLoading(true)
    getStagedNodes({ limit: 20 }).then((s) => {
      setNodes(s); setLoading(false)
    }).catch(() => setLoading(false))
  }

  useEffect(() => { load() }, [])

  const showToast = (msg: string) => {
    setToast(msg)
    setTimeout(() => setToast(null), 2000)
  }

  const handleAction = async (node: StagedNode, action: 'accept' | 'discard') => {
    setCommitting(node.staged_id)
    try {
      await commitStaged(node.staged_id, action)
      showToast(action === 'accept' ? 'Node accepted' : 'Node discarded')
      load()
    } catch (e) {
      showToast(String(e))
    } finally {
      setCommitting(null)
    }
  }

  if (loading) {
    return (
      <div className="loading-row">
        <div className="loading-spinner" /> loading staged nodes…
      </div>
    )
  }

  if (nodes.length === 0) {
    return <div className="empty-state">no staged nodes — all clear</div>
  }

  return (
    <div>
      <div className="section-label">staged · awaiting review</div>
      {nodes.map((n) => (
        <div key={n.staged_id} className="staged-item">
          <div className="staged-header">
            <TypeBadge type={n.node_type} sheet />
            <span className="staged-title">{n.title}</span>
          </div>
          {n.description && <div className="staged-desc">{n.description}</div>}
          <div className="staged-meta">
            <span className="staged-by">{n.staged_by}</span>
            <span>{n.staged_at?.slice(0, 10)}</span>
            <span
              style={{ color: 'var(--accent)', marginLeft: 'auto', cursor: 'pointer' }}
              onClick={() => onSelectNode(`pkis:${n.node_type}:${n.slug}`)}
            >
              view →
            </span>
          </div>
          <div style={{ display: 'flex', gap: 6, marginTop: 10 }}>
            <div
              className="action-btn primary"
              style={{ flex: 1, fontSize: 10, padding: '6px', opacity: committing === n.staged_id ? 0.5 : 1 }}
              onClick={() => handleAction(n, 'accept')}
            >
              ✓ accept
            </div>
            <div
              className="action-btn danger"
              style={{ flex: 1, fontSize: 10, padding: '6px', opacity: committing === n.staged_id ? 0.5 : 1 }}
              onClick={() => handleAction(n, 'discard')}
            >
              ✕ discard
            </div>
          </div>
        </div>
      ))}
      {toast && <div className="toast">{toast}</div>}
    </div>
  )
}
