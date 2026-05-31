import { useEffect, useRef, useState } from 'react'
import { getNode, commitStaged } from '../lib/api'
import { renderMarkdown } from '../lib/markdown'
import { renderMath } from '../lib/katex'
import type { FullNode, NodeType } from '../types'
import { TypeBadge } from './NodeCard'

interface Props {
  iri: string
  onClose: () => void
}

function PreviewPane({ md }: { md: string }) {
  const ref = useRef<HTMLDivElement>(null)
  const html = renderMarkdown(md)
  useEffect(() => { renderMath(ref.current) }, [md])
  return (
    <div
      ref={ref}
      className="body-preview body-text"
      dangerouslySetInnerHTML={{ __html: html }}
    />
  )
}

export default function EditSheet({ iri, onClose }: Props) {
  const [node, setNode] = useState<FullNode | null>(null)
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [success, setSuccess] = useState(false)

  const [understanding, setUnderstanding] = useState(0)
  const [body, setBody] = useState('')
  const [vizSlug, setVizSlug] = useState('')
  const [previewMode, setPreviewMode] = useState<'edit' | 'preview'>('edit')

  useEffect(() => {
    let cancelled = false
    setLoading(true)
    getNode(iri).then((n) => {
      if (cancelled) return
      setNode(n)
      setUnderstanding(n.frontmatter.understanding ?? 0)
      setBody(n.content ?? '')
      setVizSlug(n.frontmatter.viz ?? '')
      setLoading(false)
    }).catch((e) => {
      if (!cancelled) { setError(String(e)); setLoading(false) }
    })
    return () => { cancelled = true }
  }, [iri])

  const fm = node?.frontmatter
  const nodeType = (fm?.knowledge_type ?? fm?.type ?? 'concept') as NodeType
  const title = fm?.title ?? iri

  const handleSave = async () => {
    setSaving(true); setError(null)
    try {
      await commitStaged('', 'edit', {
        understanding,
        body,
        viz: vizSlug || undefined,
      })
      setSuccess(true)
      setTimeout(onClose, 1200)
    } catch (e) {
      setError(String(e))
    } finally {
      setSaving(false)
    }
  }

  return (
    <div className="sheet-overlay open">
      <div className="sheet-backdrop" onClick={onClose} />
      <div className="sheet">
        <div className="sheet-handle" />
        <div className="sheet-header">
          <div className="sheet-type-row">
            <TypeBadge type={nodeType} sheet />
          </div>
          <div className="sheet-title" style={{ fontSize: 15 }}>{title}</div>
        </div>

        <div className="sheet-body">
          {loading && (
            <div className="loading-row">
              <div className="loading-spinner" /> loading…
            </div>
          )}

          {!loading && node && (
            <>
              {/* Understanding stepper */}
              <div className="edit-field">
                <label className="edit-label">understanding (0–5)</label>
                <div className="understanding-stepper">
                  <div
                    className="stepper-btn"
                    onClick={() => setUnderstanding((v) => Math.max(0, v - 1))}
                  >
                    −
                  </div>
                  <span className="stepper-val">{understanding}</span>
                  <div
                    className="stepper-btn"
                    onClick={() => setUnderstanding((v) => Math.min(5, v + 1))}
                  >
                    +
                  </div>
                  <div className="stepper-pips">
                    {Array.from({ length: 5 }, (_, i) => (
                      <div
                        key={i}
                        className={`sheet-pip${i < understanding ? ' on u' : ''}`}
                        style={{ cursor: 'pointer' }}
                        onClick={() => setUnderstanding(i + 1)}
                      />
                    ))}
                  </div>
                </div>
              </div>

              {/* Body editor */}
              <div className="edit-field">
                <label className="edit-label">body (markdown + LaTeX)</label>
                <div className="preview-toggle">
                  {(['edit', 'preview'] as const).map((m) => (
                    <div
                      key={m}
                      className={`prev-btn${previewMode === m ? ' active' : ''}`}
                      onClick={() => setPreviewMode(m)}
                    >
                      {m}
                    </div>
                  ))}
                </div>
                {previewMode === 'edit' ? (
                  <textarea
                    className="body-textarea"
                    value={body}
                    onChange={(e) => setBody(e.target.value)}
                    spellCheck={false}
                  />
                ) : (
                  <PreviewPane md={body} />
                )}
              </div>

              {/* Viz slug */}
              <div className="edit-field">
                <label className="edit-label">visualization slug (optional)</label>
                <input
                  className="viz-field-input"
                  type="text"
                  placeholder="e.g. mcmc-sampling-trace"
                  value={vizSlug}
                  onChange={(e) => setVizSlug(e.target.value)}
                />
              </div>

              {error && <div className="cap-error">{error}</div>}
              {success && <div className="cap-success">Saved — staged for review</div>}
            </>
          )}
        </div>

        <div className="sheet-actions">
          <div className="action-btn" onClick={onClose}>← back</div>
          <div
            className="action-btn primary"
            onClick={handleSave}
            style={{ opacity: saving ? 0.6 : 1 }}
          >
            {saving ? 'saving…' : '✓ stage edits'}
          </div>
        </div>
      </div>
    </div>
  )
}
