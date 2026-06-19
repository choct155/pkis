import type { View } from '../types'
import { navFor } from '../lib/nav'
import DomainTree from './DomainTree'
import ClusterList from './ClusterList'

interface Props {
  view: View
  onNavigate: (v: View) => void
  isOwner: boolean
  domainFilter: string
  onDomain: (d: string) => void
  clusterFilter: string
  onCluster: (slug: string) => void
  onClusterAgenda: () => void
}

// Persistent desktop navigation rail (CSS-hidden below the sidebar breakpoint;
// mobile uses BottomNav instead). Holds the views plus the domain + cluster
// navigators that feed the unified faceted browse.
export default function Sidebar({
  view, onNavigate, isOwner, domainFilter, onDomain, clusterFilter, onCluster, onClusterAgenda,
}: Props) {
  return (
    <aside className="sidebar">
      <div className="sidebar-logo">PKIS</div>
      <nav className="sidebar-nav">
        {navFor(isOwner).map(({ view: v, icon, label }) => (
          <div
            key={v}
            className={`sidebar-nav-item${view === v ? ' active' : ''}`}
            onClick={() => onNavigate(v)}
          >
            <span className="sidebar-nav-icon">{icon}</span>
            <span className="sidebar-nav-label">{label}</span>
          </div>
        ))}
      </nav>
      <DomainTree active={domainFilter} onChange={onDomain} />
      <ClusterList active={clusterFilter} onChange={onCluster} onAgenda={onClusterAgenda} />
    </aside>
  )
}
