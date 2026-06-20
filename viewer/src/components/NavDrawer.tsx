import type { View, DocMeta } from '../types'
import DomainTree from './DomainTree'
import ClusterList from './ClusterList'
import DocsTree from './DocsTree'

interface Props {
  open: boolean
  onClose: () => void
  view: View
  // faceting (scope) — the desktop sidebar's filter half, surfaced on mobile
  domainFilter: string
  onDomain: (d: string) => void
  clusterFilter: string
  onCluster: (slug: string) => void
  onClusterAgenda: () => void
  // docs — when in the Docs view the drawer holds the doc tree instead
  docManifest: DocMeta[] | null
  docKey: string | null
  onDocSelect: (key: string) => void
}

// One ever-present mobile left drawer (the desktop sidebar has no mobile twin
// otherwise). Contents are contextual: the Docs tree while reading docs, the
// faceting navigators (domains + clusters) everywhere else. View-switching
// stays in the BottomNav — this drawer is purely for scope/navigation within.
// Hidden at the sidebar breakpoint (≥900px) via CSS, where the real sidebar shows.
export default function NavDrawer({
  open, onClose, view,
  domainFilter, onDomain, clusterFilter, onCluster, onClusterAgenda,
  docManifest, docKey, onDocSelect,
}: Props) {
  const inDocs = view === 'docs' && !!docManifest
  return (
    <>
      {open && <div className="nav-drawer-backdrop" onClick={onClose} />}
      <aside className={`nav-drawer${open ? ' open' : ''}`}>
        {inDocs ? (
          <DocsTree
            manifest={docManifest!}
            selected={docKey}
            onSelect={(k) => { onDocSelect(k); onClose() }}
          />
        ) : (
          <>
            <DomainTree active={domainFilter} onChange={(d) => { onDomain(d); onClose() }} />
            <ClusterList
              active={clusterFilter}
              onChange={(s) => { onCluster(s); onClose() }}
              onAgenda={() => { onClusterAgenda(); onClose() }}
            />
          </>
        )}
      </aside>
    </>
  )
}
