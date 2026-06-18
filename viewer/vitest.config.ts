import { defineConfig } from 'vitest/config';

// B8: minimal vitest setup. api.ts is pure fetch-wrapping (no DOM), so the node
// environment is enough; smoke tests live next to the code as *.test.ts.
export default defineConfig({
  test: {
    environment: 'node',
    include: ['src/**/*.test.ts'],
  },
});
