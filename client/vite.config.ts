import { fileURLToPath, URL } from 'node:url'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'
import { defineConfig } from 'vite'

const resolve = (path: string) => fileURLToPath(new URL(path, import.meta.url))

export const createAliasConfig = () => ({
  '~': resolve('./src'),
  $: resolve('..'),
})

export default defineConfig(() => {
  return {
    server: {
      port: 5001,
    },
    plugins: [
      vue(),
      vueJsx(),
    ],
    resolve: {
      alias: createAliasConfig(),
    },
  }
})
