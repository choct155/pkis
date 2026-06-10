import { useState } from 'react'
import { createBridgeNote, createSourceStub, addToQueue, uploadDocument } from '../lib/api'

type Tab = 'bridge' | 'source' | 'upload' | 'queue'

interface Props {
  onClose: () => void
  canWrite: boolean
  onSignIn: () => void
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

function UploadTab({ onDone }: { onDone: (msg: string) => void }) {
  const [file, setFile] = useState<File | null>(null)
  const [slug, setSlug] = useState('')
  const [readwise, setReadwise] = useState(false)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const pick = (f: File | null) => {
    setFile(f)
    if (f && !slug.trim()) {
      const stem = f.name.replace(/\.[^.]+$/, '')
      setSlug(stem.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 55))
    }
  }

  const submit = async () => {
    if (!file) { setError('Choose a file'); return }
    setLoading(true); setError('')
    try {
      const b64 = await new Promise<string>((resolve, reject) => {
        const r = new FileReader()
        r.onload = () => resolve(String(r.result).split(',')[1] ?? '')
        r.onerror = () => reject(r.error)
        r.readAsDataURL(file)
      })
      const res = await uploadDocument(file.name, b64, slug.trim() || undefined, readwise)
      onDone(`Uploaded → ${res.slug}${res.source_auto_created ? ' (node created)' : ''}`)
    } catch (e) {
      setError(String(e))
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <div className="cap-field">
        <label className="cap-label">document (pdf, epub, md, html, txt, docx)</label>
        <input
          className="cap-file"
          type="file"
          accept=".pdf,.epub,.md,.html,.txt,.docx"
          onChange={(e) => pick(e.target.files?.[0] ?? null)}
        />
      </div>
      <div className="cap-field">
        <label className="cap-label">source slug</label>
        <input
          className="cap-input"
          type="text"
          placeholder="auto-derived from filename"
          value={slug}
          onChange={(e) => setSlug(e.target.value)}
        />
      </div>
      <label className="cap-check">
        <input type="checkbox" checked={readwise} onChange={(e) => setReadwise(e.target.checked)} />
        push to Readwise Reader
      </label>
      {error && <div className="cap-error">{error}</div>}
      <button className="cap-submit" onClick={submit} disabled={loading || !file}>
        {loading ? 'uploading…' : 'upload document →'}
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

export default function CaptureSheet({ onClose, canWrite, onSignIn }: Props) {
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

          {!canWrite ? (
            <div className="capture-signin">
              <p className="capture-signin-msg">
                Capturing and uploading require a signed-in writer. Reading stays open.
              </p>
              <button className="cap-submit" onClick={onSignIn}>sign in →</button>
            </div>
          ) : (
          <>
          <div className="capture-tabs">
            {(['bridge', 'source', 'upload', 'queue'] as Tab[]).map((t) => (
              <div
                key={t}
                className={`cap-tab${tab === t ? ' active' : ''}`}
                onClick={() => setTab(t)}
              >
                {t === 'bridge' ? 'bridge note'
                  : t === 'source' ? 'source stub'
                  : t === 'upload' ? 'upload doc'
                  : 'add to queue'}
              </div>
            ))}
          </div>

          {tab === 'bridge' && <BridgeTab onDone={handleDone} />}
          {tab === 'source' && <SourceTab onDone={handleDone} />}
          {tab === 'upload' && <UploadTab onDone={handleDone} />}
          {tab === 'queue'  && <QueueTab  onDone={handleDone} />}

          {toast && <div className="cap-success">{toast}</div>}
          </>
          )}
        </div>
      </div>
    </div>
  )
}
