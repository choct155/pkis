import { useMemo, useState } from 'react'
import { classifyShare, RESOURCE_TYPES, type ShareInput, type IngestKind } from '../lib/shareClassify'
import { createResourceStub, createSourceStub } from '../lib/api'

// Review card shown when content is shared into PKIS from the Android share sheet.
// The share target is general: the classifier proposes a kind (source/resource), and
// the user can override it and edit fields before committing. Nothing is written until
// Commit — mirroring the two-phase staging discipline.
export default function ShareIngestView({ input, onDone }: { input: ShareInput; onDone: () => void }) {
  const guess = useMemo(() => classifyShare(input), [input])
  const [kind, setKind] = useState<Exclude<IngestKind, 'capture'>>(guess.kind === 'resource' ? 'resource' : 'source')
  const [title, setTitle] = useState(guess.title)
  const [url, setUrl] = useState(guess.url)
  const [resourceType, setResourceType] = useState(guess.resourceType || 'tool')
  const [tags, setTags] = useState('')
  const [note, setNote] = useState(input.text && input.text !== url ? input.text : '')
  const [busy, setBusy] = useState(false)
  const [msg, setMsg] = useState('')

  async function commit() {
    setBusy(true); setMsg('')
    try {
      if (kind === 'resource') {
        if (!url) throw new Error('A resource needs a URL.')
        const r = await createResourceStub({
          title: title || url, resource_url: url, resource_type: resourceType,
          tags: tags.split(',').map((t) => t.trim()).filter(Boolean),
          summary: note,
        })
        setMsg(`Staged resource · ${r.slug}. Review & commit on the workstation.`)
      } else {
        await createSourceStub(title || url, url, note)
        setMsg('Staged source. Review & commit on the workstation.')
      }
      setTimeout(onDone, 1400)
    } catch (e) {
      setMsg((e as Error).message || 'Failed to stage.')
    } finally {
      setBusy(false)
    }
  }

  return (
    <div style={S.wrap}>
      <h2 style={S.h}>Save to PKIS</h2>

      <div style={S.seg}>
        {(['source', 'resource'] as const).map((k) => (
          <button key={k} onClick={() => setKind(k)}
            style={{ ...S.segBtn, ...(kind === k ? S.segOn : {}) }}>{k}</button>
        ))}
      </div>

      <label style={S.lab}>Title</label>
      <input style={S.inp} value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Title" />

      <label style={S.lab}>URL</label>
      <input style={S.inp} value={url} onChange={(e) => setUrl(e.target.value)} placeholder="https://…" />

      {kind === 'resource' && (
        <>
          <label style={S.lab}>Resource type</label>
          <select style={S.inp} value={resourceType} onChange={(e) => setResourceType(e.target.value)}>
            {RESOURCE_TYPES.map((t) => <option key={t} value={t}>{t}</option>)}
          </select>
          <label style={S.lab}>Tags (comma-separated)</label>
          <input style={S.inp} value={tags} onChange={(e) => setTags(e.target.value)} placeholder="coding-agents, docs" />
        </>
      )}

      <label style={S.lab}>Note / summary</label>
      <textarea style={{ ...S.inp, height: 96, resize: 'vertical' }} value={note}
        onChange={(e) => setNote(e.target.value)} placeholder="Why did I save this?" />

      {msg && <div style={S.msg}>{msg}</div>}

      <div style={S.row}>
        <button style={S.discard} onClick={onDone} disabled={busy}>Discard</button>
        <button style={S.commit} onClick={commit} disabled={busy}>{busy ? 'Saving…' : 'Commit'}</button>
      </div>
      <p style={S.foot}>Staged for review — nothing goes live until you commit on the workstation.</p>
    </div>
  )
}

const S: Record<string, React.CSSProperties> = {
  wrap: { maxWidth: 520, margin: '0 auto', padding: '20px 16px 40px', color: '#0f172a',
    fontFamily: '-apple-system, Segoe UI, Roboto, sans-serif' },
  h: { fontSize: 20, margin: '4px 0 16px' },
  seg: { display: 'flex', gap: 8, marginBottom: 14 },
  segBtn: { flex: 1, padding: '10px 0', borderRadius: 10, border: '1px solid #cbd5e1',
    background: '#fff', textTransform: 'capitalize', fontWeight: 600, color: '#475569' },
  segOn: { background: '#2563eb', color: '#fff', borderColor: '#2563eb' },
  lab: { display: 'block', fontSize: 12, color: '#64748b', margin: '12px 0 4px', fontWeight: 600 },
  inp: { width: '100%', padding: '10px 12px', borderRadius: 10, border: '1px solid #cbd5e1',
    fontSize: 15, boxSizing: 'border-box', background: '#fff', color: '#0f172a' },
  row: { display: 'flex', gap: 10, marginTop: 20 },
  discard: { flex: 1, padding: '12px 0', borderRadius: 10, border: '1px solid #cbd5e1',
    background: '#fff', color: '#475569', fontWeight: 600 },
  commit: { flex: 2, padding: '12px 0', borderRadius: 10, border: 'none',
    background: '#2563eb', color: '#fff', fontWeight: 700 },
  msg: { marginTop: 14, padding: '10px 12px', borderRadius: 10, background: '#eff6ff', color: '#1d4ed8', fontSize: 14 },
  foot: { fontSize: 12, color: '#94a3b8', marginTop: 14 },
}
