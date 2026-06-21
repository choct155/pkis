interface Props {
  onClick: () => void
}

// Capture & upload entry point (signed-in writers only). The label shows on
// desktop so it reads as an action, not a mystery "+"; on mobile it stays a
// compact round button to save space.
export default function Fab({ onClick }: Props) {
  return (
    <button
      className="fab"
      onClick={onClick}
      title="Capture & upload — register a source, upload a document"
      aria-label="Capture and upload"
    >
      <span className="fab-icon">＋</span>
      <span className="fab-label">capture</span>
    </button>
  )
}
