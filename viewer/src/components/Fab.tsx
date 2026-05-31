interface Props {
  onClick: () => void
}

export default function Fab({ onClick }: Props) {
  return (
    <button className="fab" onClick={onClick} aria-label="Quick capture">
      +
    </button>
  )
}
