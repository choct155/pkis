import type { View } from '../types'

// Shared by BottomNav (mobile) and Sidebar (desktop) so the nav set stays DRY.
export const NAV_ITEMS: { view: View; icon: string; label: string }[] = [
  { view: 'browse',     icon: '◈', label: 'browse' },
  { view: 'clusters',   icon: '◎', label: 'clusters' },
  { view: 'priority',   icon: '▲', label: 'priority' },
  { view: 'graph',      icon: '⬡', label: 'graph' },
  { view: 'staged',     icon: '⊞', label: 'staged' },
  { view: 'explainers', icon: '▦', label: 'explain' },
  { view: 'discover',   icon: '✦', label: 'discover' },
]
