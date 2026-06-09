import type { View } from '../types'
import { NAV_ITEMS } from '../lib/nav'

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
