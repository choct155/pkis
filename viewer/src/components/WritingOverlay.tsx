import { useCallback, useEffect, useRef, useState } from 'react'
import { getNode } from '../lib/api'
import { renderMarkdown } from '../lib/markdown'
import { renderMath } from '../lib/katex'
import { buildStandaloneHtml, deliverExport } from '../lib/bundle'

interface Props {
  iri: string
  title?: string
  onClose: () => void
}

// Full-screen reader for `format: writing` assets (position papers, notes, …).
// Renders the asset node's markdown body, reusing the explainer-overlay chrome
// and the Docs prose styles. Esc closes.
export default function WritingOverlay({ iri, title, onClose }: Props) {
  const [md, setMd] = useState<string | null>(null)
  const [err, setErr] = useState<string | null>(null)
  const [t, setT] = useState(title || 'Document')
  // Download failures surface as a toast, never via setErr — that would swap the
  // article out for an error screen and throw away the document being read.
  const [toast, setToast] = useState<string | null>(null)
  const ref = useRef<HTMLDivElement>(null)

  // Re-pull the node so edits land while the overlay stays open — the writing
  // counterpart to the explainer overlay's cache-bust reload. Explainers bust a
  // published file's URL; here there is no file, so we just re-fetch the node.
  const load = useCallback(() => {
    setMd(null)
    setErr(null)
    getNode(iri)
      .then((n) => {
        setMd(n.content || '')
        const nt = n.frontmatter?.title
        if (nt) setT(nt)
      })
      .catch((e) => setErr(String(e)))
  }, [iri])

  useEffect(() => { load() }, [load])

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => { if (e.key === 'Escape') onClose() }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [onClose])

  useEffect(() => { if (md != null) renderMath(ref.current) }, [md])

  // Explainers download a published, self-contained HTML file; a writing asset
  // has no such file, so build one — the rendered article plus its referenced
  // nodes as appendices, so the document is readable by someone without PKIS
  // access. That walk does a handful of fetches, hence the pending state.
  const [saving, setSaving] = useState(false)
  const doDownload = async () => {
    const article = ref.current
    if (article == null || saving) return
    setSaving(true)
    try {
      const html = await buildStandaloneHtml(t, article)
      const { how } = await deliverExport(iri.split(':').pop() || 'document', t, html)
      // Name the route the export actually took. Where a platform completes
      // silently, an unlabelled no-op is indistinguishable from a broken button
      // — which is exactly how the first version of this was reported.
      if (how !== 'cancelled') {
        setToast(how === 'downloaded' ? 'Saved to your downloads'
          : how === 'shared' ? 'Shared'
          : how === 'copied' ? 'Link copied'
          : 'Could not save or share the export')
        setTimeout(() => setToast(null), 3000)
      }
    } catch {
      setToast('Export failed')
      setTimeout(() => setToast(null), 3000)
    } finally {
      setSaving(false)
    }
  }


  return (
    <div className="explainer-overlay">
      {toast && <div className="explainer-overlay-toast">{toast}</div>}
      <div className="explainer-overlay-bar">
        <span className="explainer-overlay-title">{t}</span>
        <button className="explainer-overlay-pop" onClick={load} title="Reload latest">⟳</button>
        <button className="explainer-overlay-pop" onClick={doDownload} disabled={md == null || saving}
          title="Download standalone HTML (includes referenced nodes)">{saving ? '…' : '⤓'}</button>
        <button className="explainer-overlay-close" onClick={onClose} title="Close (Esc)">✕</button>
      </div>
      <div className="writing-overlay-scroll">
        {err ? (
          <div className="empty-state">Couldn’t load: {err}</div>
        ) : md == null ? (
          <div className="empty-state">Loading…</div>
        ) : (
          <article
            ref={ref}
            className="body-text prose writing-article"
            dangerouslySetInnerHTML={{ __html: renderMarkdown(md) }}
          />
        )}
      </div>
    </div>
  )
}
