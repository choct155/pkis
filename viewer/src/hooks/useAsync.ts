import { useState, useEffect, useCallback, useRef } from 'react'

export interface AsyncState<T> {
  data: T | null
  loading: boolean
  error: string | null
}

export function useAsync<T>(
  fn: (() => Promise<T>) | null,
  deps: unknown[] = []
): AsyncState<T> & { reload: () => void } {
  const [state, setState] = useState<AsyncState<T>>({
    data: null,
    loading: false,
    error: null,
  })
  const counter = useRef(0)

  const run = useCallback(async () => {
    if (!fn) return
    const id = ++counter.current
    setState((s) => ({ ...s, loading: true, error: null }))
    try {
      const data = await fn()
      if (id === counter.current) {
        setState({ data, loading: false, error: null })
      }
    } catch (err) {
      if (id === counter.current) {
        setState({ data: null, loading: false, error: String(err) })
      }
    }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, deps)

  useEffect(() => { run() }, [run])

  return { ...state, reload: run }
}
