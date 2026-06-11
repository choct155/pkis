import type { NodeType } from '../types'

const TYPES: { key: NodeType | 'all'; label: string }[] = [
  { key: 'all',       label: 'all' },
  { key: 'concept',   label: 'concept' },
  { key: 'technique', label: 'technique' },
  { key: 'result',    label: 'result' },
  { key: 'framework', label: 'framework' },
  { key: 'problem',   label: 'problem' },
  { key: 'principle', label: 'principle' },
  { key: 'source',    label: 'source' },
  { key: 'asset',     label: 'asset' },
]

interface Props {
  active: NodeType | 'all'
  onChange: (t: NodeType | 'all') => void
}

export default function FilterStrip({ active, onChange }: Props) {
  return (
    <div className="filter-strip">
      {TYPES.map(({ key, label }) => {
        const isAll = key === 'all'
        const isActive = active === key
        const chipClass = isAll
          ? `filter-chip chip-all${isActive ? '' : ' inactive'}`
          : `filter-chip chip-${key}${isActive ? ' active-type' : ''}`
        return (
          <div key={key} className={chipClass} onClick={() => onChange(key)}>
            {label}
          </div>
        )
      })}
    </div>
  )
}
