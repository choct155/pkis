import type { View } from '../types'

const NAV_ITEMS: { view: View; icon: string; label: string }[] = [
  { view: 'browse',   icon: '◈', label: 'browse' },
  { view: 'clusters', icon: '◎', label: 'clusters' },
  { view: 'priority', icon: '▲', label: 'priority' },
  { view: 'graph',    icon: '⬡', label: 'graph' },
  { view: 'staged',   icon: '⊞', label: 'staged' },
]

interface Props {
  active: View
  onNavigate: (v: View) => void
}

export default function BottomNav({ active, onNavigate }: Props) {
  return (
    <nav className="bottom-nav">
      {NAV_ITEMS.map(({ view, icon, label }) => (
        <div
          key={view}
          className={`nav-item${active === view ? ' active' : ''}`}
          onClick={() => onNavigate(view)}
        >
          <div className="nav-icon">{icon}</div>
          <div className="nav-label">{label}</div>
        </div>
      ))}
    </nav>
  )
}
