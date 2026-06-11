import type { DiscoveryCandidate } from '../types'

interface Props {
  c: DiscoveryCandidate
  busy: boolean
  onClose: () => void
  onSelectNode: (iri: string) => void
  onAct: (action: 'accept' | 'dismiss', chip?: string) => void
}

const DISMISS_CHIPS = ['too applied', 'off-topic', 'already know', 'low quality']

function Facet({ label, text }: { label: string; text?: string }) {
  if (!text) return null
  return (
    <div className="disc-facet">
      <div className="disc-facet-label">{label}</div>
      <div className="disc-facet-text">{text}</div>
    </div>
  )
}

export default function DiscoverDetailSheet({ c, busy, onClose, onSelectNode, onAct }: Props) {
  const r = c.rationale ?? {}
  return (
    <div className="sheet-overlay open">
      <div className="sheet-backdrop" onClick={onClose} />
      <div className="sheet">
        <div className="sheet-handle" />

        <div className="sheet-header">
          <div className="sheet-type-row">
            {c.priority && <span className="disc-prio-badge">priority #{c.priority}</span>}
            <span className="domain-tag">{c.field}</span>
            <span className="domain-tag">cited {c.cited_by}×</span>
          </div>
          <div className="sheet-title">{c.title}</div>
          <div className="discover-meta">{[c.authors, c.venue || 'preprint', c.year].filter(Boolean).join(' · ')}</div>
        </div>

        <div className="sheet-body">
          {/* WHY READ IT — the lead */}
          {r.why && (
            <div className="body-section">
              <div className="disc-why">{r.why}</div>
            </div>
          )}

          {/* PRIORITY / GAP */}
          <div className="body-section">
            <div className="body-section-title">priority · gap it fills</div>
            {c.priority_note && <div className="disc-prio-note">{c.priority_note}</div>}
            <div
              className="discover-gap"
              style={{ marginTop: 8, display: 'inline-block' }}
              onClick={() => onSelectNode(c.nearest_frontier.iri)}
            >
              ◓ {c.nearest_frontier.title} (cov {c.nearest_frontier.coverage}/5)
            </div>
            <Facet label="what it closes" text={r.gap} />
          </div>

          {/* RESEARCH AGENDA — most important */}
          {(c.clusters?.length || r.agenda) && (
            <div className="body-section disc-agenda">
              <div className="body-section-title">research agenda</div>
              {c.clusters?.map((cl) => (
                <div key={cl.slug} className="disc-cluster">
                  <span className="disc-cluster-title">◎ {cl.title}</span>
                  <span className="disc-cluster-rel">{Math.round(cl.relevance * 100)}% match</span>
                  {cl.thesis && <div className="disc-cluster-thesis">{cl.thesis}</div>}
                </div>
              ))}
              {c.hypotheses && c.hypotheses.length > 0 && (
                <div className="disc-hyps">
                  {c.hypotheses.map((h, i) => (
                    <div key={i} className="disc-hyp"><span className="disc-hyp-dot">›</span> {h.title}</div>
                  ))}
                </div>
              )}
              <Facet label="how it bears on the agenda" text={r.agenda} />
            </div>
          )}

          {/* FITS / QUESTIONS */}
          <div className="body-section">
            <Facet label="how it fits your graph" text={r.fits} />
            <Facet label="questions it could answer" text={r.questions} />
          </div>

          {/* LINKS to existing nodes */}
          {c.links && c.links.length > 0 && (
            <div className="body-section">
              <div className="body-section-title">links to your nodes</div>
              {c.links.map((l) => (
                <div key={l.iri} className="conn-item" onClick={() => onSelectNode(l.iri)}>
                  <span className="conn-predicate">{l.type}</span>
                  <div className="conn-detail"><div className="conn-target">{l.title}</div></div>
                </div>
              ))}
            </div>
          )}

          {/* FULL ABSTRACT */}
          {c.abstract && (
            <div className="body-section">
              <div className="body-section-title">abstract</div>
              <div className="disc-abstract-full">{c.abstract}</div>
            </div>
          )}
        </div>

        <div className="sheet-actions">
          <a className="action-btn" href={c.url} target="_blank" rel="noreferrer">↗ paper</a>
          <div style={{ flex: 1 }} />
          <div className={`action-btn primary${busy ? ' disabled' : ''}`} onClick={() => !busy && onAct('accept')}>✓ add</div>
          <div className={`action-btn${busy ? ' disabled' : ''}`} onClick={() => !busy && onAct('dismiss')}>✗ dismiss</div>
        </div>

        <div className="disc-chip-row">
          {DISMISS_CHIPS.map((chip) => (
            <span key={chip} className="discover-chip" onClick={() => !busy && onAct('dismiss', chip)}>{chip}</span>
          ))}
        </div>
      </div>
    </div>
  )
}
