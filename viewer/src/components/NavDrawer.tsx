import type { View, DocMeta } from '../types'
import { navFor } from '../lib/nav'
import DomainTree from './DomainTree'
import ClusterList from './ClusterList'
import DocsTree from './DocsTree'

interface Props {
  open: boolean
  onClose: () => void
  view: View
  onNavigate: (v: View) => void
  isOwner: boolean
  // faceting (scope) — the desktop sidebar's filter half, surfaced on mobile
  domainFilter: string
  onDomain: (d: string) => void
  clusterFilter: string
  onCluster: (slug: string) => void
  onClusterAgenda: () => void
  // docs — when in the Docs view the drawer also hosts the doc tree
  docManifest: DocMeta[] | null
  docKey: string | null
  onDocSelect: (key: string) => void
}

// The mobile nav surface (the desktop sidebar has no mobile twin otherwise).
// Holds everything: the view list (Ask excepted — it's a TopBar icon), the doc
// tree while in Docs, and the faceting navigators. Replaces the old bottom bar.
// Hidden at the sidebar breakpoint (≥900px) via CSS, where the real sidebar shows.
export default function NavDrawer({
  open, onClose, view, onNavigate, isOwner,
  domainFilter, onDomain, clusterFilter, onCluster, onClusterAgenda,
  docManifest, docKey, onDocSelect,
}: Props) {
  return (
    <>
      {open && <div className="nav-drawer-backdrop" onClick={onClose} />}
      <aside className={`nav-drawer${open ? ' open' : ''}`}>
        <div className="sidebar-logo">PKIS</div>

        <nav className="sidebar-nav">
          {navFor(isOwner).map(({ view: v, icon, label }) => (
            <div
              key={v}
              className={`sidebar-nav-item${view === v ? ' active' : ''}`}
              onClick={() => { onNavigate(v); onClose() }}
            >
              <span className="sidebar-nav-icon">{icon}</span>
              <span className="sidebar-nav-label">{label}</span>
            </div>
          ))}
        </nav>

        {/* While reading docs, the doc tree rides along so you can jump between docs. */}
        {view === 'docs' && docManifest && (
          <div className="nav-drawer-section">
            <DocsTree
              manifest={docManifest}
              selected={docKey}
              onSelect={(k) => { onDocSelect(k); onClose() }}
            />
          </div>
        )}

        <DomainTree active={domainFilter} onChange={(d) => { onDomain(d); onClose() }} />
        <ClusterList
          active={clusterFilter}
          onChange={(s) => { onCluster(s); onClose() }}
          onAgenda={() => { onClusterAgenda(); onClose() }}
        />
      </aside>
    </>
  )
}
