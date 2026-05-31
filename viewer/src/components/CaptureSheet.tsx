import { useState } from 'react'
import { createBridgeNote, createSourceStub, addToQueue } from '../lib/api'

type Tab = 'bridge' | 'source' | 'queue'

interface Props {
  onClose: () => void
}

function BridgeTab({ onDone }: { onDone: (msg: string) => void }) {
  const [rationale, setRationale] = useState('')
  const [refs, setRefs] = useState('')
  const [edgeType, setEdgeType] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const submit = async () => {
    if (!rationale.trim()) { setError('Connection or insight is required'); return }
    setLoading(true); setError('')
    try {
      await createBridgeNote(
        rationale.trim(),
        refs.split(',').map((s) => s.trim()).filter(Boolean),
        edgeType.trim() || 'related',
        'viewer',
      )
      onDone('Bridge note staged')
    } catch (e) {
      setError(String(e))
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <div className="cap-field">
        <label className="cap-label">connection or insight</label>
        <textarea
          className="cap-textarea"
          placeholder="Describe the cross-domain connection or epiphany…"
          value={rationale}
          onChange={(e) => setRationale(e.target.value)}
        />
      </div>
      <div className="cap-field">
        <label className="cap-label">linked nodes (fuzzy refs ok)</label>
        <input
          className="cap-input"
          type="text"
          placeholder="e.g. MCMC, variational inference"
          value={refs}
          onChange={(e) => setRefs(e.target.value)}
        />
      </div>
      <div className="cap-field">
        <label className="cap-label">edge type</label>
        <input
          className="cap-input"
          type="text"
          placeholder="e.g. contrasts-with, equivalent-in-context"
          value={edgeType}
          onChange={(e) => setEdgeType(e.target.value)}
        />
      </div>
      {error && <div className="cap-error">{error}</div>}
      <button className="cap-submit" onClick={submit} disabled={loading}>
        {loading ? 'staging…' : 'stage bridge note →'}
      </button>
    </div>
  )
}

function SourceTab({ onDone }: { onDone: (msg: string) => void }) {
  const [input, setInput] = useState('')
  const [notes, setNotes] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const submit = async () => {
    if (!input.trim()) { setError('Title or URL is required'); return }
    setLoading(true); setError('')
    const isUrl = input.trim().startsWith('http')
    try {
      await createSourceStub(
        isUrl ? undefined : input.trim(),
        isUrl ? input.trim() : undefined,
        notes.trim() || undefined,
      )
      onDone('Source registered')
    } catch (e) {
      setError(String(e))
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <div className="cap-field">
        <label className="cap-label">title or URL</label>
        <input
          className="cap-input"
          type="text"
          placeholder="arXiv URL, DOI, or paper title"
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
      </div>
      <div className="cap-field">
        <label className="cap-label">notes</label>
        <textarea
          className="cap-textarea"
          placeholder="Why is this relevant?"
          value={notes}
          onChange={(e) => setNotes(e.target.value)}
        />
      </div>
      {error && <div className="cap-error">{error}</div>}
      <button className="cap-submit" onClick={submit} disabled={loading}>
        {loading ? 'registering…' : 'register source →'}
      </button>
    </div>
  )
}

function QueueTab({ onDone }: { onDone: (msg: string) => void }) {
  const [ref, setRef] = useState('')
  const [reason, setReason] = useState('')
  const [priority, setPriority] = useState<'high' | 'normal'>('normal')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const submit = async () => {
    if (!ref.trim()) { setError('Source is required'); return }
    setLoading(true); setError('')
    try {
      await addToQueue(ref.trim(), reason.trim(), priority)
      onDone('Added to queue')
    } catch (e) {
      setError(String(e))
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <div className="cap-field">
        <label className="cap-label">source</label>
        <input
          className="cap-input"
          type="text"
          placeholder="source slug or title"
          value={ref}
          onChange={(e) => setRef(e.target.value)}
        />
      </div>
      <div className="cap-field">
        <label className="cap-label">reason</label>
        <input
          className="cap-input"
          type="text"
          placeholder="why now?"
          value={reason}
          onChange={(e) => setReason(e.target.value)}
        />
      </div>
      <div className="cap-field">
        <label className="cap-label">priority</label>
        <div className="prio-toggle">
          {(['high', 'normal'] as const).map((p) => (
            <div
              key={p}
              className={`prio-btn${priority === p ? ` active ${p}` : ''}`}
              onClick={() => setPriority(p)}
            >
              {p}
            </div>
          ))}
        </div>
      </div>
      {error && <div className="cap-error">{error}</div>}
      <button className="cap-submit" onClick={submit} disabled={loading}>
        {loading ? 'adding…' : 'add to queue →'}
      </button>
    </div>
  )
}

export default function CaptureSheet({ onClose }: Props) {
  const [tab, setTab] = useState<Tab>('bridge')
  const [toast, setToast] = useState<string | null>(null)

  const handleDone = (msg: string) => {
    setToast(msg)
    setTimeout(() => { setToast(null); onClose() }, 1400)
  }

  return (
    <div className="sheet-overlay open">
      <div className="sheet-backdrop" onClick={onClose} />
      <div className="sheet" style={{ maxHeight: '80vh' }}>
        <div className="sheet-handle" />
        <div className="capture-sheet-inner">
          <div className="capture-title">
            quick capture
            <span className="capture-close" onClick={onClose}>×</span>
          </div>
          <div className="capture-tabs">
            {(['bridge', 'source', 'queue'] as Tab[]).map((t) => (
              <div
                key={t}
                className={`cap-tab${tab === t ? ' active' : ''}`}
                onClick={() => setTab(t)}
              >
                {t === 'bridge' ? 'bridge note' : t === 'source' ? 'source stub' : 'add to queue'}
              </div>
            ))}
          </div>

          {tab === 'bridge' && <BridgeTab onDone={handleDone} />}
          {tab === 'source' && <SourceTab onDone={handleDone} />}
          {tab === 'queue'  && <QueueTab  onDone={handleDone} />}

          {toast && <div className="cap-success">{toast}</div>}
        </div>
      </div>
    </div>
  )
}
